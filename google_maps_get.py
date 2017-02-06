import urllib.parse
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def index():
    user_input = ''
    while user_input != 'exit':
        try:
            google_url = 'http://maps.googleapis.com/maps/api/geocode/json?'
            user_input = input('\nPlease enter in your location: ')
            print('-' * 50)
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

            # print('\nInformation pertaining to your search:\n')
            # print('\tFull address: ' + full_address)
            # print('\tCity: ' + addr_compo_city_long_name)
            # print('\tCounty: ' + addr_compo_county_long_name)
            # print('\tFull state name: ' + addr_compo_state_long_name)
            # print('\tState abreviation: ' + addr_compo_state_short_name)
            # print('\tLongitude: ' + str(geo_lng))
            # print('\tLatitude: ' + str(geo_lat))
            # print('\tStatus: ' + return_status)
            # print('-' * 50)

        except Exception as e:
            print('\n** An unexpected error occured. Please try again! **\n')
        
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)