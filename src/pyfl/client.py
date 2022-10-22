# required imports
from multiprocessing.resource_sharer import stop
import requests

# local imports
from .errors import *
from .helper import Helper
from .accident import Accident
from .air import AirQuality
from .bikePoint import bike
from .cabWise import cab
from .journeys import journeys
from .mode import Mode
from .occupancy import Occupancy
from .place import Place
from .road import Road
from .search import Search
from .stop import Stop
from .travel import Travel
from .tube import LU
from .vehicle import Vehicle


class client():
    """ Synchronous client class """
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
        self.bike = bike()
        self.cab = cab()
        self.journey = journeys()
        self.mode = Mode()
        self.occupancy = Occupancy()
        self.place = Place()
        self.search = Search()
        self.vehicle = Vehicle()
        self.stop = Stop()
        self.travel = Travel()
        self.vehicle = Vehicle