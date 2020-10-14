import unittest
import subprocess
import os
import pandas as pd
import json

from importlib import reload

def test_r_subprocess():
  r_directory = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'r'))
  args = {
    'app_token': 'APP_TOKEN',
    'user_token': 'USER_TOKEN',
    'r_directory': r_directory,
    'report_type': 'cohort',
    'report_parameters': {
      'cohort_start': '2018-12-10',
      'cohort_end': '2018-12-16',
      'period': 'week'
    }
  }
  path = os.path.join(r_directory, 'run_report.r')
  p = subprocess.Popen(['Rscript', '--vanilla', str(path), json.dumps(args)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  df = pd.read_csv(p.stdout)
  _, error = p.communicate()
  return_code = p.returncode
  print(df)
  import pdb; pdb.set_trace()
  assert not error
  assert return_code == 0
  assert not df.empty

# class Test_R(unittest.TestCase):

#   def test_r_runs(self):
#     """
#     Test that the R evaluator can execute R code.
#     """
#     rpy2.robjects.r('x <- 4')
#     x = rpy2.robjects.r('x')
#     print('x:', x)
#     self.assertEqual(x[0], 4)
    
#   def test_clear_environment(self):
#     """
#     Test whether the R evaluator uses the same instance across test cases.
#     """
#     rpy2.robjects.r('x <- 4')
#     rpy2.robjects.r('rm(list=ls())')
#     x = None
#     try:
#       x = rpy2.robjects.r('x')
#     except:
#       print('x does not exist in R.')
#     self.assertIsNone(x, 'x exists in R.')

  # def test_r_instance(self):
  #   """
  #   WARNING: This test currently seems to corrupt the rpy2 package. Test whether the R environment can be cleared.
  #   """
  #   rpy2.robjects.r('x <- 4')
  #   x = rpy2.robjects.r('x')
  #   self.assertEqual(x[0], 4)

  #   # del rpy2.robjects.__dict__['r']
  #   reload(rpy2.robjects)
  #   reload(rpy2)

  #   self.assertEqual(x[0], 4)
