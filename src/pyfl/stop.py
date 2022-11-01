from .errors import *
from .helper import Helper

class Stop():
    """ Stop class """
    def __init__(self):
        """Initialises the stop class"""
        pass

    def get_stop_catagories(self):
        """
        Returns a list of all available stop catagories

        :return: A list of all available stop catagories
        :rtype: dict
        """
        endpoint = "/StopPoint/Meta/Categories"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_stop_types(self):
        """
        Returns a list of all available stop types

        :return: A list of all available stop types
        :rtype: dict
        """
        endpoint = "/StopPoint/Meta/StopTypes"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_stop_modes(self):
        """
        Returns a list of all available stop modes

        :return: A list of all available stop modes
        :rtype: dict
        """
        endpoint = "/StopPoint/Meta/Modes"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_stop_by_id(self,stopID:str,includeCrowding=False):
        """
        Returns a stop by its ID

        :param stopID: A comma-separated list of stop point ids (station naptan code e.g. 940GZZLUASL). Max. approx. 20 ids. You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name.
        :type stopID: str
        :param includeCrowding: Include the crowding data (static). To Filter further use: /StopPoint/{ids}/Crowding/{line} (optional, default to False)
        :type includeCrowding: bool
        :return: The stop
        :rtype: dict
        """
        endpoint = f"/StopPoint/{stopID}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_place_by_id(self,placeID:str,placeType:str):
        """
        Returns a place by its ID

        :param placeID: A naptan id for a stop point (station naptan code e.g. 940GZZLUASL).
        :type placeID: str
        :param placeType: A comcomma-separated value representing the place types
        :type placeType: str
        :return: The place
        :rtype: dict
        """
        endpoint = f"/StopPoint/{id}/placeTypes?placeType={placeType}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))
    
    def get_crowding_data(self,placeID:str,line="",direction=""):
        """
        Gets all the Crowding data (static) for the StopPointId, plus crowding data for a given line and optionally a particular direction.

        :param placeID: The Naptan id of the stop
        :type placeID: str
        :param line: A particular line e.g. victoria, circle, northern etc. Optionally you can use in helper.victora (optional, default to None)
        :type line: str
        :param direction: The direction of travel. Can be inbound or outbound. (optional, default to None)
        :type direction: str
        :return: The crowding data
        :rtype: dict
        """
        endpoint = f"/StopPoint/{placeID}/Crowding/{line}/{direction}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_all_stop_points_by_type(self,type:str,page:int=0):
        """
        Returns all stop points of a given type

        :param type: A comma-separated list of the types to return. Max. approx. 12 types. A list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint.
        :type type: str
        :param page: The page number to return (optional, default to None)
        :type page: int
        :return: All stop points of a given type
        :rtype: dict
        """
        if page==0:
            endpoint = f"/StopPoint/Type/{type}"
        else:
            endpoint = f"/StopPoint/Type/{type}/page/{page}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))
    
    def get_service_type_of_stoppoint(self,id:str,lineID=[],modes=[]):
        """
        Gets the service types for a given stoppoint

        :param id: The Naptan id of the stop
        :type id: str
        :param lineID: A particular line e.g. victoria, circle, northern etc. Optionally you can use in helper.victora (optional, default to None)
        :type lineID: array
        :param modes: The modes which the lines are relevant to
        :return: The service types for a given stoppoint
        :rtype: dict
        """
        endpoint = f"/StopPoint/{id}/ServiceTypes?lineId={lineID}&modes={modes}"
        return Helper.parse(Helper.make_raw_api_call(endpoint))

    def get_arrival_predictions(self,stopID:str):
        """
        Gets the list of arrival predictions for the given stop point id

        :param stopID: A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
        :type stopID: str
        :return: The list of arrival predictions for the given stop point id
        :rtype: dict
        """
        endpoint = f"/StopPoint/{stopID}/Arrivals"

        # must also get it seperatly from another endpoint for the elizabeth, thameslink and overground lines as they are not included in the above endpoint
        # https://api.tfl.gov.uk/swagger/ui/index.html?url=/swagger/docs/v1#!/StopPoint/StopPoint_ArrivalDepartures

        elizabeth = f"/StopPoint/{stopID}/ArrivalDepartures"
        eliz = Helper.parse(Helper.make_raw_api_call(elizabeth))
        everythingElse = Helper.parse(Helper.make_raw_api_call(endpoint))
        
        return everythingElse["arrivals"].extend(eliz["arrivals"])

    # https://api.tfl.gov.uk/swagger/ui/index.html?url=/swagger/docs/v1#!/StopPoint/StopPoint_ReachableFrom

    ### I got to here before I had to go, so if someone would like to finish off the rest of this file that would be great :)
    