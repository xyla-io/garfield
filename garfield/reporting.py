import pandas as pd
import os
import subprocess
import json
import time

from . import AdjustAPI
from typing import Optional, Dict
from datetime import datetime
from enum import Enum

class AdjustReportPeriod(Enum):
  day = 'day'
  week = 'week'
  month = 'month'

  @property
  def days(self) -> int:
    if self is AdjustReportPeriod.day:
      return 1
    elif self is AdjustReportPeriod.week:
      return 7
    elif self is AdjustReportPeriod.month:
      return 30
    else:
      raise ValueError('Unsupported adjust report period', self)

  @property
  def max_period(self) -> Optional[int]:
    if self is AdjustReportPeriod.day:
      return 30
    elif self is AdjustReportPeriod.week:
      return 12
    elif self is AdjustReportPeriod.month:
      return None
    else:
      raise ValueError('Unsupported adjust report period', self)

class AdjustReporter:
  api: AdjustAPI

  def __init__(self, api: AdjustAPI):
    self.api = api
    
  def fetch_events_report(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
    parameters = {
      'start_date': start_date.strftime('%Y-%m-%d'),
      'end_date': end_date.strftime('%Y-%m-%d'),
    }
    return self.run_report(report_type='events', report_parameters=parameters)

  def fetch_deliverables_report(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
    parameters = {
      'start_date': start_date.strftime('%Y-%m-%d'),
      'end_date': end_date.strftime('%Y-%m-%d'),
    }
    return self.run_report(report_type='deliverables', report_parameters=parameters)

  def fetch_cohort_report(self, cohort_start: datetime, cohort_end: datetime, period: AdjustReportPeriod) -> pd.DataFrame:
    parameters = {
      'cohort_start': cohort_start.strftime('%Y-%m-%d'),
      'cohort_end': cohort_end.strftime('%Y-%m-%d'),
      'period': period.value,
    }
    return self.run_report(report_type='cohort', report_parameters=parameters)

  def run_report(self, report_type: str, report_parameters: Dict[str, any]={}):
    tries = 2
    current_try = 0
    while True:
      current_try += 1
      try:
        arguments = {
          'app_token': self.api.app_token,
          'user_token': self.api.user_token,
          'r_directory': self.api.r_directory,
          'report_type': report_type,
          'report_parameters': report_parameters,
        }
        path = os.path.join(self.api.r_directory, 'run_report.r')
        p = subprocess.Popen([self.api.rscript_command, '--vanilla', str(path), json.dumps(arguments)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        read_csv_error = None
        try:
          df = pd.read_csv(p.stdout)
        except KeyboardInterrupt:
          raise
        except Exception as e:
          read_csv_error = e
        _, error = p.communicate()
        return_code = p.returncode

        if return_code != 0 or error or read_csv_error:
          message = f'{f"R script error: {error}" if error else ""}{f" CSV error: {read_csv_error}" if read_csv_error else ""}'.strip() if error or read_csv_error else None
          raise AdjustAPI.RScriptError(code=return_code, script=path, message=message)

        return df
      except AdjustAPI.RScriptError as e:
        if current_try < tries:
          print(f'Retrying after R script error on attempt {current_try} of {tries}: {e}')
          time.sleep(3)
        else:
          raise
