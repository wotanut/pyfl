import pyfl
from pyfl import TFL, underground, line
import os

key = os.getenv(api_key)

tflapi = TFL(api_key=key)
tube = underground(api_key=key)

print(tube.getLineStatus(line.Victoria))
print(tube.getLineStatus(line.DLR))