from .errors import *
from .helper import Helper

class Place():
    def __init__(self):
        pass

    def get_place_catagories(self):
        """
        Get all the place catagories

        :return: The place catagories
        :rtype: dict
        """
        endpoint = f"/Place/Meta/Categories"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_place_types(self):
        """
        Get all the place types

        :return: The place types
        :rtype: dict
        """
        endpoint = f"/Place/Meta/PlaceTypes"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_street(self,postcode):
        """
        Get the street for a given postcode

        :param postcode: The postcode to get the street for
        :type postcode: str
        :return: The street
        :rtype: dict
        """
        endpoint = f"/Place/Address/Streets/{postcode}"
        return Helper.make_raw_api_call(endpoint)
    
    def get_places_by_type(self, type=[], activeOnly=False):
        """
        Get all the places of a given type

        :param type: The type of place to get
        :type type: list
        :param activeOnly: Only return active places, defaults to False
        :return: The places
        :rtype: dict
        """
        endpoint = f"/Place/{type}?activeOnly={activeOnly}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))
    
    def get_places_by_id(self, id:str):
        """
        Get a place by it's id

        :param id: The id of the place
        :type id: str
        :return: The place
        :rtype: dict
        """
        endpoint = f"/Place/{id}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))
    
    def get_places_by_location(self, radius:int,lat:float, long:float, type="", catagories=[], includeChildren=False, activeOnly=False,max=20):
        """
        Get all the places of a given type within a given radius of a given location

        :param radius: The radius to search in
        :type radius: int
        :param lat: The latitude of the location
        :type lat: float
        :param long: The longitude of the location
        :type long: float
        :param type: The type of place to get (optional)
        :type type: str
        :param catagories: The catagories of place to get (optional)
        :type catagories: list
        :param includeChildren: Include child places, defaults to False
        :type includeChildren: bool
        :param activeOnly: Only return active places, defaults to False
        :type activeOnly: bool
        :param max: The maximum number of places to return, defaults to 20
        :type max: int
        :return: The places
        :rtype: dict
        """
        endpoint = f"/Place?radius={radius}&lat={lat}&lon={long}&type={type}&categories={catagories}&includeChildren={includeChildren}&activeOnly={activeOnly}&max={max}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_place_by_type_and_location(self,type:list,lat:float,long:float):
        """
        Get all the places of a given type within a given radius of a given location

        :param type: The type of place to get
        :type type: list
        :param lat: The latitude of the location
        :type lat: float
        :param long: The longitude of the location
        :type long: float
        :return: The places
        :rtype: dict
        """
        endpoint = f"/Place/{type}/At/{lat}/{long}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_place_by_type(self,name:str):
        """
        Get a place by it's name

        :param name: The name of the place
        :type name: str
        :return: The place
        :rtype: dict
        """
        endpoint = f"/Place/Search?name={name}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))
    
    def get_place_overlay(self,z:int, type:list,width:int,height:int,lat:int,long:int):
        """
        Get the overlay for a given place

        :param z: The zoom level
        :type z: int
        :param type: The type of place to get
        :type type: list
        :param width: The width of the overlay
        :type width: int
        :param height: The height of the overlay
        :type height: int
        :param lat: The latitude of the location
        :type lat: int
        :param long: The longitude of the location
        :type long: int
        :return: The overlay
        :rtype: dict
        """
        endpoint = f"/Place/{type}/overlay/{z}/{lat}/{long}/{width}/{height}"
        return Helper.make_raw_api_call(endpoint)