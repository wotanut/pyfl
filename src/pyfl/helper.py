import requests

class Helper():
    victoria = "victoria"
    def __init__(self):
        pass

    @staticmethod
    def make_raw_api_call(endpoint):
        """ Make a raw API call to the TFL API """
        r = requests.get("https://api.tfl.gov.uk/" + endpoint)
        return r.json()

    @staticmethod
    def remove_crap(json_data):
        """A lot of the TFL API returns a lot of crap, this function removes it..."""
        return json_data[0]

    #@staticmethod
    #def victoria():
    #    return "victoria"