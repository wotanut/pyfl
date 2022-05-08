from pyfl.lines import line
from pyfl.helper import helper

class underground():
  """
  represents every action related to the underground
  """
  def __init__(self,api_key):
    self.api_key = api_key

  def getLineStatus(self,route: line):
    """
    Return the status of a line as string as strings.

    :param kind: the tube line to get the status of.
    :type kind: pyfl.line
    :return: The status of the line.
    :rtype: str

    """
    return helper(api_key=self.api_key).send_request(url=f"Line/Mode/{route}/Status")