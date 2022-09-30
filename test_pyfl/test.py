from pyfl import client
import os

def test_tube():
	"""Tests an API call to get a tube lines status"""
	
	token = os.getenv("TFL_API_TOKEN")

	# tests getting the API key

	TFL = client(token)
	response = TFL.api_key

	assert isinstance(response, str)
	assert response ==token, "The ID should be in the response"

	# tests the victoria line attribute

	Victoria = TFL.helper.victoria
	assert isinstance(Victoria, str)
	assert Victoria == "victoria", "This should be an attribute for the underground"

	# tests tube.py

	response = TFL.tube.get_line_status("victoria")
	assert isinstance(response, dict)

	# tests accident.py

	response = TFL.accident.get_accident_stats(2019)
	assert isinstance(response, dict)

	# tests helper.py

	response = TFL.helper.parse(TFL.helper.make_raw_api_call("/line/victoria/status"))
	assert isinstance(response, dict)

	# tests airquality.py

	response = TFL.AirQuality.get_air_quality()
	assert isinstance(response,dict)

	# tests bikePoint.py

	response = TFL.bike.get_all_bike_points()
	assert isinstance(response,dict)

	response = TFL.bike.get_bike_point(1122)
	assert isinstance(response,dict)

	response = TFL.bike.get_bike_point_by_name("Baker Street")
	assert isinstance(response,dict)