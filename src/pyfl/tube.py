# local imports
from .errors import *
from .helper import Helper

# PLEASE NOTE: THIS FILE NEEDS A LOT OF WORK, IT IS NOT COMPLETE

class LU():
    """ Line class"""
    def __init__(self):
        """ Initialise the Line class """
        pass

    def get_line_status(self, line:str):
        """ 
        Returns the status of a line

        :param kind: Status of the line to get.
        :type kind: str
        :return: The line status.
        :rtype: dict
        """
        endpoint = f"/line/{line}/status"
        return Helper.parse(Helper.make_raw_api_call(endpoint))