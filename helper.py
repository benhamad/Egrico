import requests
import urllib2, urllib, json

def get_location_name(longt, lat):
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={}, {}".format(lat, longt))
    return r.json()['results'][0]['address_components'][1]['short_name']


def get_weather(location):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"

    yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="'+location+'") and u=\'c\''
    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
    result = urllib2.urlopen(yql_url).read()
    data = json.loads(result)
    return data['query']['results']['channel']['item']['forecast'][1]


def sms(phone, text):
    r = requests.get("http://sms.tritux.com/v1/send?username=tunihack4&password=core2456&origin=VIPER&destination={}&text={}".format(phone, text))
