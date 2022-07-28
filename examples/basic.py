from pyfl import client
import os

key = os.getenv("api_key")

TFL = client.pyfl(key)

print(TFL.tube.get_line_status(TFL.helper.victoria()))