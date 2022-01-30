from pyfl import TFL, underground, line
import os

def test_tube():
	"""Tests an API call to get a tube lines status"""

	# tests getting the API key

	tflapi = TFL(os.getenv("TFL_API_TOKEN"))
	response = tflapi.api_key

	assert isinstance(response, str)
	assert response == os.getenv("TFL_API_TOKEN"), "The ID should be in the response"

	# tests the victoria line attribute

	Victoria = line.Victoria
	assert isinstance(Victoria, str)
	assert Victoria == "victoria", "This should be an attribute for the underground"

	# tests a call to the api

	tube = underground(api_key=os.getenv("TFL_API_TOKEN"))
	print(tube.getLineStatus(route=line.Victoria))
