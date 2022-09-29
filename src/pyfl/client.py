# required imports
import requests

# local imports
from .errors import *
from .helper import Helper
from .tube import LU
from .accident import Accident
from .airquality import AirQuality

class client():
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
        self.accident = Accident()
        self.AirQuality = AirQuality()