# required imports
import requests

# local imports
from errors import *
from helper import Helper
from tube import LU

class pyfl():
    """Base PYFL class"""
    def __init__(self, api_key):
        """ Initialise the PYFL class """
        self.api_key = api_key
        self.tube = LU()
        self.helper = Helper()