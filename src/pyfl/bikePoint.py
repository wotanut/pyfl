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
        :rtype: dict
        """
        endpoint = f"/BikePoint/"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_bike_point(self, id:int):
        """
        Returns a specfic bike point
            
        :param id: id of the bike point to get.
        :type id: int
        :return: the bike point.
        :rtype: dict
        """
        endpoint = f"/BikePoint/{id}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_bike_point_by_name(self, name:str):
        """
        Returns a specfic bike point
            
        :param name: name of the bike point to get.
        :type name: str
        :return: the bike point.
        :rtype: dict
        """
        endpoint = f"/BikePoint/Search?query={name}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))