import requests
import asyncio
import json

class tube:
    def __init__(self, api_key):
        self.apiKey = api_key
        self.dlr = "No Service Data"

    async def getLineStatus(self,line_ID=None):
        valid_lines = ["dlr", "london-overground", "tfl-rail", "tram", "tube", "bakerloo", "central", "circle", "district", "hammersmith-city", "jubilee", "metropolitan","northern","piccadilly","victoria","waterloo-city"]
        if line_ID not in valid_lines:
            try:
                status = requests.get("https://api.tfl.gov.uk/Line/Mode/tube,dlr,overground,tflrail/Status")
            except Exception as e:
                return e
        else:
            try:
                status = requests.get(f"https://api.tfl.gov.uk/Line/Mode/{line_ID}/Status")
            except Exception as e:
                return e
        #jsonEncoding = status.json()
        #jsonEncoding["lineStatuses"]
        return status.json()
