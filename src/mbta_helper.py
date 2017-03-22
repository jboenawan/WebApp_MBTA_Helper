# Useful URLs (you need to add the appropriate parameters for your requests)
import urllib.request
import json
from pprint import pprint

MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key="
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?address="


# A little bit of scaffolding if you want to use it



def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    # url = "https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower"
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    # pprint(response_data)
    return response_data

# get_json("https://maps.googleapis.com/maps/api/geocode/json?address=Prudential%20Tower")


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    place_name2 = place_name.replace(' ','%20')
    # print(place_name2)
    url = GMAPS_BASE_URL + place_name2
    # print(url)
    json_data = get_json(url)
    lat = json_data['results'][0]['geometry']['location']['lat']
    lng = json_data['results'][0]['geometry']['location']['lng']
    return lat, lng

# print(get_lat_long('PrudentialTower'))


def get_nearest_station(lat,lng):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = MBTA_BASE_URL + MBTA_DEMO_API_KEY + '&lat=' + str(lat) + '&lon=' + str(lng) + "&format=json"
    # print(url)
    stop_data = get_json(url)
    stop = stop_data['stop'][0]['stop_name']
    distance = stop_data['stop'][0]['distance']
    distance = '{:.2f}'.format(float(distance))
    return (stop, distance)

# print(get_nearest_station(42.3471477, -71.0825077))


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat, lon = get_lat_long(place_name)
    stop,distance = get_nearest_station(lat,lon)

    return (stop,distance)

# print(find_stop_near('Prudential Tower'))

# print(find_stop_near('Prudential Tower'))

