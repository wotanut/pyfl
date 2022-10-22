import requests
from .errors import *

class Helper():
    """ Utility class to help with developing the library."""
    victoria = "victoria"
    circle = "circle"
    district = "district"
    HammersmithCity = "hammersmith-city"
    Piccadilly = "piccadilly"
    Metropolitan = "metropolitan"
    Northern = "northern"
    Jubilee = "jubilee"
    Central = "central"
    Bakerloo = "bakerloo"
    WaterlooCity = "waterloo-city"
    DLR = "dlr"
    Overground = "overground"
    TfL_Rail = "tfl-rail"
    LondonOverground = "london-overground"


    def __init__(self):
        """Initialises the helper class. .. warning:: Given that this class is mostly staticmethod's, this function is essentially useless and is merely for internal use"""
        pass

    @staticmethod
    def make_raw_api_call(endpoint):
        """ 
        Make a raw API call to the TFL API
        
        :param endpoint: The endpoint to call
        :type endpoint: str
        :return: The json response from the API
        """
        try:
            r = requests.get("https://api.tfl.gov.uk/" + endpoint)
        except Exception as e:
            raise invalid_response(f"Invalid response from TFL API: {e}")
            return
        return r.json()

    @staticmethod
    def parse(json_data):
        """
        removes the data from the response
        
        :param json_data: The json data to parse
        :type json_data: dict
        :return: The parsed data
        :rtype: dict
        """
        try:
            raw_data = json_data[0]
        except Exception as e:
            raise invalid_response(f"Invalid response from TFL API: {e}")
        return json_data[0]