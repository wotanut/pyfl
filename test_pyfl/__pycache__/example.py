import pyfl
from pyfl import TFL, underground

tflapi = TFL("ac472ed2f70143b38a98577630042544")

print(underground.Victoria)
print(underground.getLineStatus(underground.Victoria))