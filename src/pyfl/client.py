# required imports
import requests

# local imports
from .errors import *
from .helper import Helper
from .tube import LU

class client():
    """Base PYFL class"""
    def __init__(self, api_key):
        """
        Creates the client object
        
        :param kinda: str
        :type kind: str
        :raise errors.invalid_api_key: If the API key is invalid
        :return: client object
        :rtpe: object
        """
        self.api_key = api_key
        self.tube = LU()
        self.helper = Helper()