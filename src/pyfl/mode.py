# local imports
from .errors import *
from .helper import Helper

class Mode():
    """ Mode class"""
    def __init__(self):
        """ Initialise the Mode class """
        pass

    def get_mode(self):
        """ 
        Returns the service type for a given mode

        :return: The service type for a given mode.
        :rtype: dict
        """
        endpoint = f"/Mode/ActiveServiceTypes"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_arrival_predictions(self, mode:str, count=-1):
        """
        Get's the arrival predictions for all stops of a given mode

        :param mode: The mode to get the arrival predictions for.
        :type mode: str
        :param count: The number of arrivals to return, defaults to -1 (all)
        :type count: int
        :return: The arrival predictions.
        :rtype: dict
        """
        endpoint = f"/Mode/{mode}/Arrivals"
        return Helper.parse(Helper.make_raw_api_call(endpoint))