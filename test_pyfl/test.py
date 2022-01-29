from pyfl import TFL, underground, line

def test_tube():
	"""Tests an API call to get a tube lines status"""

	# tests getting the API key

	tflapi = TFL("ac472ed2f70143b38a98577630042544")
	response = tflapi.api_key

	assert isinstance(response, str)
	assert response == "ac472ed2f70143b38a98577630042544", "The ID should be in the response"

	# tests the victoria line attribute

	Victoria = line.Victoria
	assert isinstance(Victoria, str)
	assert Victoria == "victoria", "This should be an attribute for the underground"

	# tests a call to the api

	tube = underground(api_key="ac472ed2f70143b38a98577630042544")
	print(tube.getLineStatus(route=line.Victoria))