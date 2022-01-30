from pyfl import TFL, underground, line
import os

def test_tube():
	"""Tests an API call to get a tube lines status"""
	
	token = os.getenv("TFL_API_TOKEN")

	# tests getting the API key

	tflapi = TFL(token)
	response = tflapi.api_key

	assert isinstance(response, str)
	assert response ==token, "The ID should be in the response"

	# tests the victoria line attribute

	Victoria = line.Victoria
	assert isinstance(Victoria, str)
	assert Victoria == "victoria", "This should be an attribute for the underground"

	# tests a call to the api

	tube = underground(api_key=token)
	print(tube.getLineStatus(route=line.Victoria))
