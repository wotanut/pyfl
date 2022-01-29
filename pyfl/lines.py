from .tfl import TFL

class line(TFL):
  """
  Helper class to allow you to write line.Victoria instead of having to write it's line ID each time
  """
  def __init__(self):
    TFL.__init__(self,api_key)

  Victoria = "victoria"
  Central = "central"
  District = "district"
  DLR = "dlr"
  Metropolitan = "metropolitan"
  Northern = "northern"
  Piccadilly = "piccadilly"
  Waterloo = "waterloo-city"
  Bakerloo = "bakerloo"
  Circle = "circle"
  Hammersmith = "hammersmith-city"
  Jubilee = "jubilee"
  Victoria = "victoria"
  Overground = "london-overground"
  TfL-Rail = "tfl-rail"
  Tram = "tram"
  Tube = "tube"