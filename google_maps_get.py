import urllib.parse
import requests


google_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = 'morgan hill'
url = google_url + urllib.parse.urlencode({'address': address})
google_json_data = requests.get(url).json()  # creates json data from the requests

return_status = google_json_data['status']  # returns the status message
full_address = google_json_data['results'][0]['formatted_address']
addr_compo_city_long_name = google_json_data['results'][0]['address_components'][0]['long_name']
addr_compo_county_long_name = google_json_data['results'][0]['address_components'][1]['long_name']
addr_compo_state_long_name = google_json_data['results'][0]['address_components'][2]['long_name']
addr_compo_state_short_name = google_json_data['results'][0]['address_components'][2]['short_name']
print(address_components_state_long_name)
print(address_components_state_short_name)