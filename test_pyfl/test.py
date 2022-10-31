from pyfl import client
import os

def test_tube():
	"""Tests an API call to get a tube lines status"""
	
	token = os.getenv("TFL_API_TOKEN")
	token = ""

	# tests getting the API key

	TFL = client(token)
	response = TFL.api_key

	assert isinstance(response, str)
	assert response ==token, "The ID should be in the response"

	# tests the victoria line attribute

	Victoria = TFL.helper.victoria
	assert isinstance(Victoria, str)
	assert Victoria == "victoria", "This should be an attribute for the underground"

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

	response = TFL.bike.get_bike_point("BikePoints_85")
	assert isinstance(response,dict)

	response = TFL.bike.get_bike_point_by_name("Baker Street")
	assert isinstance(response,dict)

	# tests cabWise.py

	response = TFL.cab.get_taxi_information(51.5074,0.1278)
	assert isinstance(response,dict)

	# tests journeys.py

	response = TFL.journey.get_available_modes()
	assert isinstance(response,dict)

	response = TFL.journey.perform_journey("51.5074","0.1278")
	assert isinstance(response,dict)

	# tests mode.py

	response = TFL.mode.get_mode()
	assert isinstance(response,dict)

	response = TFL.mode.get_arrival_predictions("tube")
	assert isinstance(response,dict)

	# tests occupancy.py

	response = TFL.occupancy.get_bike_point_occupancy(["BikePoints_85"])
	assert isinstance(response,dict)

	response = TFL.occupancy.get_car_park_occupancy()
	assert isinstance(response,dict)

	response = TFL.occupancy.get_charge_point_occupancy()
	assert isinstance(response,dict)

	# tests place.py

	# tests road.py

	# tests search.py

	response = TFL.search.search("test")
	assert isinstance(response,dict)

	response = TFL.search.search_bus_schedule("test")
	assert isinstance(response,dict)

	# response = TFL.search.get_all_avaiable_sort_options()
	# assert isinstance(response,dict)

	# response = TFL.search.get_available_search_catagories()
	# assert isinstance(response,dict)

	# tests stop.py

	# tests travel.py

	# tests tube.py

	response = TFL.tube.get_line_status("victoria")
	assert isinstance(response, dict)

	# test vehicle.py

	# response = TFL.vehicle.get_vehicle_arrival(["LX58CFV"])
	# assert isinstance(response,dict)