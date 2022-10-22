from .errors import *
from .helper import Helper

class Vehicle():
    """ Vehicle class"""
    def __init__(self):
        """ Initiliases the vehicle class"""
        pass

        def get_vehicle_arrival(registration:list):
            """
            Returns the predicted arrival of a vehicle with the given registration

            :param kind: The registration of the vehicle to gt
            :type kind: list of strings
            :return: The predicted arrival time of the vehicle with that registration
            :rtype: dict
            """
            if len(registration) > 25 or len(registration) < 1:
                raise invalid_parameter("The parameter for registration must be between 1 and 25 items")
            else:
                endpoint = f"/Vehicle/{registration}/Arrivals"
                return Helper.parse(Helper.make_raw_api_call(endpoint))
