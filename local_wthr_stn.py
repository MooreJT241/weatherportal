from requests import get
import json
from pprint import pprint
from haversine import haversine

##DB URLs housing data
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

##lat and long can be changed to fit desired coordinates
my_lat = 29.74
my_lon = -95.35

all_stations = get(stations).json()['items']

def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

closest_stn = find_closest()
##creates variable for find_closest() then makes a string to add to end of weather URL
weather = weather + str(closest_stn)

## Fetch closest station data
my_weather = get(weather).json()['items']
pprint(my_weather)
