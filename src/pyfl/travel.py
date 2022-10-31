from .errors import *
from .helper import Helper

class Travel():
    """ Travel class"""
    def __init__(self):
        """ Initialises the travel class"""
        pass

    def get_travel_time_overlay(self,z:int,pin_lat:float,pin_long:float,mapCenterLat:float,mapCenterLon:float,scenarioTitle:str,timeOfDay:str,modeID:str,width:int,height:int,direction:str,travelTime:int):
        """
        Generates a travel time overlay

        :param z: Zomm level
        :type z: int
        :param pin_lat: Latitude of the pin
        :type pin_lat: float
        :param pin_long: Longitude of the pin
        :type pin_long: float
        :param mapCenterLat: Latitude of the map center
        :type mapCenterLat: float
        :param mapCenterLon: Longitude of the map center
        :type mapCenterLon: float
        :param scenarioTitle: Title of the scenario
        :type scenarioTitle: str
        :param timeOfDay: Time of day
        :type timeOfDay: str
        :param modeID: Mode ID
        :type modeID: str
        :param width: The width of the requested overlay
        :type width: int
        :param height: The height of the requested overlay
        :type height: int
        :param direction: Direction of travel (From, To, Average) (optional, default to Average)
        :type direction: str
        :param travelTime: The total minutes between the travel time bands
        :type travelTime: int
        :return: The travel time overlay
        :rtype: dict
        """
        endpoint = f"/TravelTimes/overlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pin_lat}/{pin_long}/dimensions/{width}/{height}?scenarioTitle={scenarioTitle}&timeOfDayId={timeOfDay}&modeId={modeID}&direction={direction}&travelTimeInterval={travelTime}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def compare_travel_time_overlay(self,z:int,pin_lat:float,pin_long:float,mapCenterLat:float,mapCenterLon:float,scenarioTitle:str,timeOfDay:str,modeID:str,width:int,height:int,direction:str,travelTime:int,compareType:str,compareValue:str):
        """
        Generates a travel time overlay

        :param z: Zomm level
        :type z: int
        :param pin_lat: Latitude of the pin
        :type pin_lat: float
        :param pin_long: Longitude of the pin
        :type pin_long: float
        :param mapCenterLat: Latitude of the map center
        :type mapCenterLat: float
        :param mapCenterLon: Longitude of the map center
        :type mapCenterLon: float
        :param scenarioTitle: Title of the scenario
        :type scenarioTitle: str
        :param timeOfDay: Time of day
        :type timeOfDay: str
        :param modeID: Mode ID
        :type modeID: str
        :param width: The width of the requested overlay
        :type width: int
        :param height: The height of the requested overlay
        :type height: int
        :param direction: Direction of travel (From, To, Average) (optional, default to Average)
        :type direction: str
        :param travelTime: The total minutes between the travel time bands
        :type travelTime: int
        :param compareType: The type of comparison (Scenario, TimeOfDay, Mode)
        :type compareType: str
        :return: The travel time overlay
        :rtype: dict
        """
        endpoint = f"/TravelTimes/overlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pin_lat}/{pin_long}/dimensions/{width}/{height}?scenarioTitle={scenarioTitle}&timeOfDayId={timeOfDay}&modeId={modeID}&direction={direction}&travelTimeInterval={travelTime}/{compareType}/{compareValue}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))