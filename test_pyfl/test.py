from pyfl import client
import os

def test_tube():
	"""Tests an API call to get a tube lines status"""
	
	token = os.getenv("TFL_API_TOKEN")

	# tests getting the API key

	TFL = client.pyfl(token)
	response = TFL.api_key

	assert isinstance(response, str)
	assert response ==token, "The ID should be in the response"

	# tests the victoria line attribute

	Victoria = TFL.helper.victoria()
	assert isinstance(Victoria, str)
	assert Victoria == "victoria", "This should be an attribute for the underground"