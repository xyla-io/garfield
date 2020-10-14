import os

from typing import Optional

class AdjustAPI:
  class RScriptError(Exception):
    code: int
    script: str
    message: Optional[str]

    def __init__(self, code: int, script: str, message: Optional[str]=None):
      description = f'R script error in file "{script}"" with exit code {code}'
      if message is not None:
        description += f': {message}'
      super().__init__(description)
      self.code = code
      self.script = script
      self.message = message

  rscript_command: str = 'Rscript'
  r_directory: str = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'r'))
  user_token: str
  app_token: str

  def __init__(self, user_token: str, app_token: str):
    self.user_token = user_token
    self.app_token = app_token
