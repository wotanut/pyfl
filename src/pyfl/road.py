from .errors import *
from .helper import Helper

class Road():
    """ Road Class """
    def __init__(self):
        """ Initialises the road class"""
        pass

    def get_road(self,road_id=""):
        """ 
        Gets the road with the given id 


        :param road_id: The id of the road (optional)
        :type: str
        :return: All the roads managed by TFL
        :rtype: dict 
        """
        endpoint = f"/Road/{road_id}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_road_status(self,road_id:str,dataRangeNullableStart:str,dataRangeNullableEnd:str):
        """
        Gets the status of the road with the given id

        :param road_id: The id of the road
        :type: str
        :param dataRangeNullableStart: The start date  (optional)
        :type: str
        :param dataRangeNullableEnd: The end date (optional)
        :type: str
        :return: The status of the road
        :rtype: dict
        """
        endpoint = f"/Road/{road_id}/Status?start={dataRangeNullableStart}&end={dataRangeNullableEnd}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_active_disruptions(self,road_id:str,stripContent=False,severities="",catagories="",closures=True):
        """
        Get's a list of all the active disruptions, filtered by the road ID

        :param: road_id: The id of the road
        :type: str
        :param: stripContent: Optional, defaults to false. When true, removes every property/node except for id, point, severity, severityDescription, startDate, endDate, corridor details, location, comments and streets
        :type: bool
        :param: severities: Optional, defaults to empty string. When set, filters the results by severity. Can be comma separated list of severities.  (a valid list of severities can be obtained from the road.get_road_disruption_severities() function)
        :type: str
        :param: catagories: Optional, defaults to empty string. When set, filters the results by category. Can be comma separated list of categories. (a valid list of categories can be obtained from the road.get_road_disruption_catagories() function)
        :type: str
        :param: closures: Optional, defaults to true. When true, always includes disruptions that have road closures, regardless of the severity filter. When false, the severity filter works as normal.
        :type: bool
        :return: A list of all the active disruptions
        :rtype: dict
        """
        endpoint= f"/Road/{road_id}/Disruption?stripContent={stripContent}&severities={severities}&categories={catagories}&closures={closures}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_all_disruptions(self,startDate="",endDate=""):
        """
        Gets a list of all the disruptions

        :param: startDate: Optional, defaults to empty string. When set, filters the results by start date. Must be in the format YYYY-MM-DD
        :type: str
        :param: endDate: Optional, defaults to empty string. When set, filters the results by end date. Must be in the format YYYY-MM-DD
        :type: str
        :return: A list of all the disruptions
        :rtype: dict
        """
        endpoint = f"/Road/Disruption?startDate={startDate}&endDate={endDate}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))
    
    def get_road_disruption_catagories(self):
        """
        Get a list of all the road disruption catagories

        :return: A list of all the road disruption catagories
        :rtype: dict
        """
        endpoint = "/Road/Meta/categories"
        return Helper.parse(Helper.make_raw_api_call(endpoint))
    
    def get_road_disruption_severities(self):
        """
        Get a list of all the road disruption severities
        
        :return: A list of all the road disruption severities
        :rtype: dict
        """
        endpoint = "/Road/Meta/severities"
        return Helper.parse(Helper.make_raw_api_call(endpoint))