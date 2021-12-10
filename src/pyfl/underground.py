import requests
import asyncio
import json

class tube:
    def __init__(self, api_key):
        self.apiKey = api_key

    async def getLineStatus(self,line_ID=None):
        """
        Returns the status of a line (I.E Good Service, Minor Delays)
        """
        valid_lines = ["dlr", "london-overground", "tfl-rail", "tram", "tube", "bakerloo", "central", "circle", "district", "hammersmith-city", "jubilee", "metropolitan","northern","piccadilly","victoria","waterloo-city"]
        if line_ID.lower() not in valid_lines:
            return f"Line ID '{line_ID}' is not valid, please see https://link.to.documentation/valid_line_ids to find a list of all valid line IDs"
        else:
            try:
                status = requests.get(f"https://api.tfl.gov.uk/Line/{line_ID}/Status/")
            except Exception as e:
                return e
        decoding = status.json()
        getDescription = decoding[0]["lineStatuses"][0]["statusSeverityDescription"]
        return getDescription