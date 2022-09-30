# local imports
from .errors import *
from .helper import Helper

class bike():
    """ bike class"""
    def __init__(self):
        """ Initialise the Bike class """
        pass

    def get_all_bike_points(self):
        """ 
        Returns all the bike points

        :return: all the bike points in london.
        :rtype: str
        """
        endpoint = f"/BikePoint/"
        return Helper.parse(Helper.make_raw_api_call(endpoint))