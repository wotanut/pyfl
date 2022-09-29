import requests
from .errors import *

class Helper():
    victoria = "victoria"
    def __init__(self):
        pass

    @staticmethod
    def make_raw_api_call(endpoint):
        """ Make a raw API call to the TFL API """
        try:
            r = requests.get("https://api.tfl.gov.uk/" + endpoint)
        except Exception as e:
            raise invalid_response(f"Invalid response from TFL API: {e}")
            return
        return r.json()

    @staticmethod
    def parse(json_data):
        """A lot of the TFL API returns a lot of crap, this function removes it..."""
        return json_data[0]

    #@staticmethod
    #def victoria():
    #    return "victoria"