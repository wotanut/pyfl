# local imports
from .errors import *
from .helper import Helper

class LU():
    """ Line class"""
    def __init__(self):
        """ Initialise the Line class """
        pass

    def get_line_status(self, line:str):
        """ Get the status of a line """
        endpoint = f"/line/{line}/status"
        return Helper.remove_crap(Helper.make_raw_api_call(endpoint))