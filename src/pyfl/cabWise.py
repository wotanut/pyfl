# local imports
from .errors import *
from .helper import Helper

class cab():
    """ Cab class"""
    def __init__(self):
        """ Initialise the Cab class """
        pass

    def get_taxi_information(self, lat:float, long:float, optype="", wheelchair=False,radius=0,name="",maxResults=20, legacyFormat=False, twentyFourSevenOnly=False):
        """
        Returns taxi and minicabs contact information

        :param lat: latitude
        :type lat: float
        :param long: longitude
        :type long: float
        :param optype: Operator Type e.g Minicab, Executive, Limousine
        :type optype: str
        :param wheelchair: Wheelchair accessible
        :type wheelchair: bool
        :param radius: The radius in metres to search for operators
        :type radius: int
        :param name: The trading name of the operating company
        :type name: str
        :param maxResults: max results to search for, defualts to 20
        :type maxResults: int
        :param legacyFormat: Legacy format [NOT RECOMMENDED], defualts to False
        :type legacyFormat: bool
        :param twentyFourSevenOnly: To only search for operators which are 24/7, defualts to False
        :type twentyFourSevenOnly: bool
        :return: The taxi information.
        :rtype: dict
        """
        if maxResults > 20:
            raise invalid_parameter("maxResults cannot be greater than 20")

        # possiblity to add optype to helper

        endpoint = f"/Cabwise/search?lat={lat}&long={long}&optype={optype}&wheelchair={wheelchair}&radius={radius}&name={name}&maxResults={maxResults}&legacyFormat={legacyFormat}&twentyFourSevenOnly={twentyFourSevenOnly}"
        return Helper.make_raw_api_call(endpoint)