from geopy.geocoders import Nominatim
from geopy.geocoders import Photon
from pprint import pprint
from geopy import distance
import geopy
import configparser
import time
from diskcache import Cache 

from dataset import testing_dataset

class CachedGeocoder():
    def __init__(self, geocoder_from_geopy, identifier):
        self.geocoder_from_geopy = geocoder_from_geopy
        self.identifier = identifier
        self.cache = Cache('tmp/' + identifier)

    def get_geocoder_reply(self, query):
        returned = self.cache.get(query)
        if returned != None:
            return returned['reply']
        else:
            uncached = self.get_uncached_geocoder_reply(query)
            self.cache.set(query, {'reply': uncached})
            return uncached

    def get_uncached_geocoder_reply(self, query):
        print(query, "for", self.identifier, "was not cached")
        while True:
            time.sleep(1)
            try:
                return self.geocoder_from_geopy.geocode(query)
            except geopy.exc.GeocoderUnavailable:
                sleep_time_in_s = 10
                print("will retry after", sleep_time_in_s, "seconds")
                time.sleep(sleep_time_in_s)
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
    email = config['DEFAULT']['email']
    apis = create_geocoders(email)
    run_compare(apis)

def create_geocoders(email):
    user_agent = email + " using geocode benchmark https://github.com/matkoniecz/benchmark-geocoders"
    return [
        CachedGeocoder(Nominatim(user_agent=user_agent), "nominatim"),
        CachedGeocoder(Photon(user_agent=user_agent), "photon"),
    ]

def run_compare(apis):
    for entry in testing_dataset():
        for geocoder in apis:
            print(entry, geocoder.identifier)
            location = geocoder.get_geocoder_reply(entry['query'])
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