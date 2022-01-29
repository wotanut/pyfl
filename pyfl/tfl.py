import urllib.parse
import requests
import http.client
import json

class TFL( object ):
  """
  the base class for the TFL wrapper
  """
  def __init__(self,api_key: str):
    self.api_key = api_key

  def send_request(self,url: str):
    """
    Sends a request to the api provided a url to use
    """
    base_url = f"https://api.tfl.gov.uk/{url}?{urllib.parse.urlencode({'app_key': self.api_key})}"

    try:
      response = requests.get(base_url)
      return response.json()[0]

    except Exception as e:
      return e