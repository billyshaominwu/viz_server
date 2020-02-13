from django.shortcuts import render
from django.core import serializers

from django.http import HttpResponse
from mysite.crimesapp.models import Crime

import math
import json

earth_radius = 3960.0
degrees_to_radians = math.pi / 180.0
radians_to_degrees = 180.0 / math.pi

def deg_to_rad(deg):
  return deg * (math.pi / 180)

def change_in_latitude(miles):
    '''
    Given a distance north, return the change in latitude.
    '''
    return (miles / earth_radius) * radians_to_degrees

def change_in_longitude(latitude, miles):
    '''
    Given a latitude and a distance west, return the change in longitude.
    '''
    # Find the radius of a circle around the earth at given latitude.
    r = earth_radius * math.cos(latitude * degrees_to_radians)
    return (miles / r) * radians_to_degrees

def distance(lat1, lon1, lat2, lon2):
    '''
    Calculates the distance between two points given
    their latitudes and longitude
    '''
    dLat = deg_to_rad(lat2-lat1)
    dLon = deg_to_rad(lon2-lon1) 
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg_to_rad(lat1)) * math.cos(deg_to_rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)); 
    return earth_radius * c


def get_crimes_in_circle(longitude, latitude, radius):
    '''
    Returns all crimes within a certain mile radius from the point
    defined by the given longitude and latitude
    '''

    longitude_rad = change_in_longitude(latitude, radius)
    latitude_rad = change_in_latitude(radius)

    longitude_min = longitude - longitude_rad
    longitude_max = longitude + longitude_rad
    latitude_min = latitude - latitude_rad
    latitude_max = latitude + latitude_rad
    
    crimes_in_box = Crime.objects.filter(longitude__gte=longitude_min, longitude__lte=longitude_max, latitude__gte=latitude_min, latitude__lte=latitude_max)

    # crime_frequency = {}
    crimes_in_circle = []
    for crime in crimes_in_box:
        distFromCenter = distance(latitude, longitude, crime.latitude, crime.longitude)
        if (distFromCenter <= radius):
            crimes_in_circle.append(crime)
            # if crime.offense_type not in crime_frequency:
                # crime_frequency[crime.offense_type] = 0
            # crime_frequency[crime.offense_type] += 1

    return crimes_in_circle
    
    crime_freq_json = json.dumps(crime_frequency)
    return HttpResponse(crime_freq_json, content_type='application/json')

    # result_json = serializers.serialize('json', crimesWithinBox)
    # result_json = serializers.serialize('json', crime_frequency)
    # return HttpResponse(result_json, content_type='application/json')

def get_crime_frequency_in_circle(request, longitude, latitude, radius):
    longitude = float(longitude)
    latitude = float(latitude)
    radius = float(radius)
    crimes_in_circle = get_crimes_in_circle(longitude, latitude, radius)

    crime_frequency = {}
    
    for crime in crimes_in_circle:
      if crime.offense_type not in crime_frequency:
        crime_frequency[crime.offense_type] = 0
      crime_frequency[crime.offense_type] += 1

    crime_freq_json = json.dumps(crime_frequency)
    return HttpResponse(crime_freq_json, content_type='application/json')

def get_crime_frequency_by_year(request, longitude, latitude, radius):
    longitude = float(longitude)
    latitude = float(latitude)
    radius = float(radius)
    crimes_in_circle = get_crimes_in_circle(longitude, latitude, radius)

    crime_by_year = {}

    for crime in crimes_in_circle:
      year = crime.report_date.year
      if year not in crime_by_year:
        crime_by_year[year] = 0
      crime_by_year[year] += 1

    crime_year_json = json.dumps(crime_by_year)
    return HttpResponse(crime_year_json, content_type='application/json')
    
