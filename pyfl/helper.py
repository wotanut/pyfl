import requests

class Helper():
    def __init__(self):
        pass

    @staticmethod
    def make_raw_api_call(endpoint):
        r = requests.get("https://api.tfl.gov.uk/" + endpoint)
        return r.json()

    @staticmethod
    def victoria():
        return "victoria"