# local imports
from ast import Str
from .errors import *
from .helper import Helper

class journeys():
    """ Journey class"""
    def __init__(self):
        """ Initialise the Journey class """
        pass

    def get_available_modes(self):
        """ 
        Get's a list of all the available modes of transport

        :return: The available modes of transport.
        :rtype: dict
        """
        endpoint = f"/Journey/Meta/Modes"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def perform_journey(self, fromcoord:str, tocoord:str):
        """"
        Perform a journey between two points, note: there are many more parameters that need to be added to this function at a later date. Please refer to the docs for more information (https://api.tfl.gov.uk/swagger/ui/index.html?url=/swagger/docs/v1#!/Journey/Journey_JourneyResults).

        :param fromcoord: The starting location
        :type fromcoord: str
        :param tocoord: The destination
        :type tocoord: str
        :return: The journey
        :rtype: dict
        """
        endpoint = f"/Journey/JourneyResults/{fromcoord}/to/{tocoord}"
        return Helper.make_raw_api_call(endpoint)