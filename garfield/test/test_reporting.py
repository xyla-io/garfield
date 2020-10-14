import unittest
import code

from ..api import AdjustAPI
from ..reporting import AdjustReporter, AdjustReportPeriod
from datetime import datetime, timedelta

class Test_AdjustReporter(unittest.TestCase):
  def setUp(self):
    api = AdjustAPI(user_token='USER_TOKEN', app_token='APP_TOKEN')
    self.reporter = AdjustReporter(api=api)
    self.reporter.api.prepare()
    self.reporter.api.connect()
  
  def tearDown(self):
    self.reporter.api.disconnect()
    self.reporter.api.clear()

  def test_preparation(self):
    """
    Test that the AdjustReporter class can prepare its R reporter.
    """
    self.reporter.prepare()
    self.assertIsNotNone(self.reporter.reporter)
    self.reporter.clear()
    self.assertIsNone(self.reporter.reporter)

  def test_cohort_report(self):
    """
    Test that the AdjustReporter class can prepare its R reporter.
    """
    self.reporter.prepare()
    report = self.reporter.fetch_cohort_report(datetime.utcnow() - timedelta(days=90), AdjustReportPeriod.week)

    import pdb; pdb.set_trace()
    self.assertIsNotNone(report)
    self.assertIn('revenue', report.columns.values.tolist())

    self.reporter.clear()
