import urllib.parse
import requests


user_input = ''
while user_input != 'exit':
    try:
        google_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
        user_input = input('Please enter in your location: ')
        url = google_url + urllib.parse.urlencode({'address': user_input})
        google_json_data = requests.get(url).json()  # creates json data from the requests

        addr_compo_city_long_name = google_json_data['results'][0]['address_components'][0]['long_name']  # i.e. San Francisco
        addr_compo_county_long_name = google_json_data['results'][0]['address_components'][1]['long_name']  # i.e. Santa Clara
        addr_compo_state_long_name = google_json_data['results'][0]['address_components'][2]['long_name']  # i.e. California
        addr_compo_state_short_name = google_json_data['results'][0]['address_components'][2]['short_name']  # i.e. CA
        full_address = google_json_data['results'][0]['formatted_address']  # i.e. (Morgan Hill, CA, USA)
        geo_lng = google_json_data['results'][0]['geometry']['location']['lng']  # returns longitude
        geo_lat = google_json_data['results'][0]['geometry']['location']['lat']  # returns latitude
        return_status = google_json_data['status']  # returns the status message
    except Exception as e:
        print('\n** An unexpected error occured. Please try again! **\n')
    