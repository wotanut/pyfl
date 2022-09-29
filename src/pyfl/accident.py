# local imports
from .errors import *
from .helper import Helper

class Accident():
    """ Accident class"""
    def __init__(self):
        """ Initialise the Accident class """
        pass

    def get_accident_stats(self, year:int):
        """ 
        Returns the accident statistics for a given year

        :param kind: Year for the stats to get.
        :type kind: str
        :return: The stats for that year.
        :rtype: str
        """
        endpoint = f"//AccidentStats/{year}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))