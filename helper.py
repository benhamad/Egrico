import requests

def get_location_name(longt, lat):
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=36.835084,%2010.144354")
    print r.text
    print r.json()['results'][0]['address_components'][1]['short_name']