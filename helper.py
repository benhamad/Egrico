import requests

def get_location_name(longt, lat):
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={lat}, {longt}".format(lat, longt))
    return r.json()['results'][0]['address_components'][1]['short_name']