import urllib.parse
import requests


google_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = 'morgan hill'
url = google_url + urllib.parse.urlencode({'address': address})
google_json_data = requests.get(url).json()  # creates json data from the requests

return_status = google_json_data['status']  # returns the status message
formatted_address = google_json_data['results'][0]['formatted_address']
address_components_long_name = google_json_data['results'][0]['address_components'][0]['long_name']
address_components_short_name = google_json_data['results'][0]['address_components'][0]['long_short']

print(address_components)