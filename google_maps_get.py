import urllib.parse
import requests


google_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = 'lhr'
url = google_url + urllib.parse.urlencode({'address': address})
json_data = requests.get(url).json() . # creates json dats from the requests 

return_status = json_data['status']  # returns the status message