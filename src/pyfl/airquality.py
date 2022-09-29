# local imports
from .errors import *
from .helper import Helper

class AirQuality():
    """ AirQuality class"""
    def __init__(self):
        """ Initialise the Air Quality class """
        pass

    def get_air_quality(self):
        """ 
        Returns the current air quality in london

        :return: The air quality in london.
        :rtype: str
        """
        endpoint = f"/AirQuality"
        return Helper.make_raw_api_call(endpoint)