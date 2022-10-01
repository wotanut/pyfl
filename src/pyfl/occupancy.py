# local imports
from array import array
from .errors import *
from .helper import Helper

class Occupancy():
    """ Occupancy class"""
    def __init__(self):
        """ Initialise the Occupancy class """
        pass

    def get_car_park_occupancy(self,id=""):
        """ 
        Returns the current occupancy of a car park

        :param id: The id of the car park, defualts to all
        :type id: string
        :return: The occupancy of the car park.
        :rtype: dict
        """
        if id == "":
            endpoint = f"/Occupancy/CarPark/{id}"
        else:
            endpoint = f"/Occupancy/CarPark"
        return Helper.make_raw_api_call(endpoint)

    def get_charge_point_occupancy(self,id=[]):
        """ 
        Returns the current occupancy of a charge point

        :param id: The id of the charge point, defualts to all
        :type id: array
        :return: The occupancy of the charge point.
        :rtype: dict
        """
        if len(id) < 0:
            endpoint = f"/Occupancy/ChargePoint/{id}"
        else:
            endpoint = f"/Occupancy/ChargePoint"
        return Helper.make_raw_api_call(endpoint)
    
    def get_bike_point_occupancy(self,id:list):
        """
        Returns the current occupancy of a bike point

        :param id: The id of the bike point, defualts to all
        :type id: list
        :return: The occupancy of the bike point.
        :rtype: dict
        """
        endpoint = f"/Occupancy/BikePoint/{id}"
        return Helper.make_raw_api_call(endpoint)