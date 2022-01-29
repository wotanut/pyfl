from pyfl import TFL, underground
import pyfl

tflapi = TFL(api_key="ac472ed2f70143b38a98577630042544")

test = tflapi.send_request("/Line/Mode/dlr/Status")
print(test)