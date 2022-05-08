from pyfl.tfl import TFL
from pyfl.lines import line

class underground(TFL):
  """
  represents every action related to the underground
  """
  def __init__(self,api_key):
    self.api_key = api_key
#    TFL.__init__(self,api_key=api_key)

  def getLineStatus(self,route: line):
    """
    Return the status of a line as string as strings.

    :param kind: the tube line to get the status of.
    :type kind: pyfl.line
    :return: The status of the line.
    :rtype: str

    """
    return TFL(api_key=self.api_key).send_request(url=f"Line/Mode/{route}/Status")