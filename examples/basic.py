import os
import pyfl
from pyfl.client import client

key = os.getenv("api_key")

TFL = pyfl.client(key)

print(TFL.tube.get_line_status(TFL.helper.victoria))