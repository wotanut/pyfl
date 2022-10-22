from .errors import *
from .helper import Helper

class Search():
    """ Search class"""
    def __init__(self):
        """ Initilaises the search class"""
        pass

    def search(self,query:str):
        """
        Searches the TFL website for any references of the query, returns 100 results

        :param query:  The query which to search
        :type: str
        :return: Any references of the query
        :rtype: dict 
        """
        endpoint = f"/Search/query={query}"
        return Helper.make_raw_api_call(endpoint)
    
    def search_bus_schedule(self,query:str):
        """
        Searches the TFL website for a bus number

        :param query:  The query which to search
        :type: str
        :return: The schedule of the busses
        :rtype: dict 
        """
        endpoint = f"/Search/BusSchedules/query={query}"
        return Helper.make_raw_api_call(endpoint)

    # TODO: Find out what this endpoint does
    def search_provider_names(self):
        """
        
        """
        endpoint = f"/Search/Meta/SearchProviders"
        return Helper.make_raw_api_call(endpoint)

    def get_available_search_catagories(self):
        """
        Get's all the available search cataogries

        :return: All of the available search catagries
        :rtype: dict
        """
        endpoint = f"/Search/Meta/Categories"
        return Helper.parse(Helper.make_raw_api_call(endpoint))
    
    def get_all_avaiable_sort_options(self):
        """
        Get's all the avaiable sorting options

        :return: A list of all the avaialble sorting options
        :rtype: dict
        """
        endpoint = f"/Search/Meta/Sorts"
        return Helper.parse(Helper.make_raw_api_call(endpoint))