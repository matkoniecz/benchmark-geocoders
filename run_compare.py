from geopy.geocoders import Nominatim
from geopy.geocoders import Photon
from pprint import pprint
from geopy import distance
import geopy
import configparser
import time

from dataset import testing_dataset

def get_geocoder_reply(geocoder, query):
    while True:
        time.sleep(1)
        try:
            return geocoder.geocode(query)
        except geopy.exc.GeocoderUnavailable:
            print("retrying")
            time.sleep(10)
            continue

def osm_url_pin(lat, lon):
    return "https://www.openstreetmap.org/?mlat=" + str(lat) + "&mlon=" + str(lon) + "#map=18/" + str(lat) + "/" + str(lon)

def main():
    config = configparser.ConfigParser()
    config.read('config_file.secret')

    if "email" not in config['DEFAULT']:
        print("insufficient data in config file!")
        print("please run `python3 create_config_file.py`")
        return

    user_agent = config['DEFAULT']['email'] + " using geocode benchmark https://github.com/matkoniecz/benchmark-geocoders"
    apis = [
        Nominatim(user_agent=user_agent),
        Photon(user_agent=user_agent),
    ]

    for entry in testing_dataset():
        for geocoder in apis:
            location = get_geocoder_reply(geocoder, entry['query'])
            if location == None:
                if entry['lat'] == None and entry['lon'] == None:
                    print("nothing was found as expected")
                    continue
                else:
                    print("nothing was found, mismatching expectations")
                    continue
            returned_location = (location.latitude, location.longitude)
            expected_location = (entry['lat'], entry['lon'])
            distance_in_m = distance.distance(returned_location, expected_location).m
            if distance_in_m < entry['allowed_mismatch_in_meters']:
                continue
            print(entry['allowed_mismatch_in_meters'])
            print(distance_in_m)
            print("expected: " + osm_url_pin(entry["lat"], entry["lon"]))
            print("returned: " + osm_url_pin(location.latitude, location.longitude))
            print()

main()