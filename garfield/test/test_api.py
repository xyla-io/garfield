import unittest
import code

from ..api import AdjustAPI

class Test_AdjustAPI(unittest.TestCase):
    def setUp(self):
      self.api = AdjustAPI(user_token='u', app_token='a')

    def test_api_exists(self):
      """
      Test that the AdjustAPI class can be instanced.
      """
      self.assertIsNotNone(self.api)
    
    def test_api_preparation(self):
      """
      Test that the AdjustAPI class can prepare its adjust client.
      """
      self.api.prepare()
      self.assertIsNotNone(self.api.api)
      self.api.clear()
      self.assertIsNone(self.api.api)

    def test_api_connection(self):
      """
      Test that the AdjustAPI class can connect its adjust client.
      """
      self.api.prepare()
      # code.interact(local=locals())
      self.api.connect()
      self.api.disconnect()
      self.api.clear()
