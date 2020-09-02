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

class FallbackGeocoder(CachedGeocoder):
    def __init__(self, cached_geocoder_list, identifier):
        self.cached_geocoder_list = cached_geocoder_list
        self.identifier = identifier
    
    def get_geocoder_reply(self, query):
        for g in self.cached_geocoder_list:
            returned = g.get_geocoder_reply(query)
            if returned != None:
                return returned
        return None

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
    cached_nominatim = CachedGeocoder(Nominatim(user_agent=user_agent), "nominatim")
    cached_photon = CachedGeocoder(Photon(user_agent=user_agent), "photon")
    return [
        cached_nominatim,
        cached_photon,
        FallbackGeocoder([cached_nominatim, cached_photon], "nominatim_fallback_to_photon"),
        FallbackGeocoder([cached_photon, cached_nominatim], "photon_fallback_to_nominatim"),
    ]

def format_distance(distance_in_m):
    if distance_in_m < 1:
        return str(round(distance_in_m, 2)) + " m"
    if distance_in_m < 10:
        return str(round(distance_in_m, 1)) + " m"
    if distance_in_m < 5000:
        return str(int(distance_in_m)) + " m"
    return str(round(distance_in_m/1000))+" km"

def entry_to_human_text(entry, geocoder_identifier):
    text = entry['query']
    if 'comment' in entry:
        text += " (" + entry['comment'] + ")"
    if 'info_about_known_failures' in entry:
        if geocoder_identifier in entry['info_about_known_failures']:
            text += ' [' + entry['info_about_known_failures'][geocoder_identifier] + ']'
    return text

def run_compare(apis):
    output = ""
    output += "<html>"    
    for geocoder in apis:
        about_geocoder = ""
        success = 0
        fail = 0
        for entry in testing_dataset():
            text = entry_to_human_text(entry, geocoder.identifier)
            location = geocoder.get_geocoder_reply(entry['query'])
            if entry['lat'] == None and entry['lon'] == None:
                text += " expected nothing to match"
            else:
                expected_url = osm_url_pin(entry["lat"], entry["lon"])
                text += ' <a href="' + expected_url + '">expected</a>'
            if location == None:
                text += " nothing returned"
            else:
                returned_url = osm_url_pin(location.latitude, location.longitude)
                text += ' <a href="' + returned_url + '">returned</a>'

            if run_compare_in_specific_case(entry, geocoder):
                about_geocoder += '<div style="background-color: #aaFFaa;font-size: 7px;color:  black;">' + text + "</div>"
                success += 1
            else:
                about_geocoder += '<div style="background-color: #FFFF00;font-size: 16px;color:  red;">' + text + "</div>"
                fail += 1
        output += "<h1>" + geocoder.identifier + " (" + str(success) + "/" + str(success+fail) + ")</h1>"
        output += about_geocoder
    output += "</html>"
    with open('tmp/output.html', 'w') as f:
        f.write(output)

def run_compare_in_specific_case(entry, geocoder):
    header = geocoder.identifier + "\n" + entry['query']
    if 'comment' in entry:
        header += "\n" + entry['comment']
    location = geocoder.get_geocoder_reply(entry['query'])
    if location == None:
        if entry['lat'] == None and entry['lon'] == None:
            print("nothing was found as expected")
            return True
        else:
            print("nothing was found, mismatching expectations")
            print(header)
            print()
            return False
    returned_location = (location.latitude, location.longitude)
    expected_location = (entry['lat'], entry['lon'])
    distance_in_m = distance.distance(returned_location, expected_location).m
    if distance_in_m < entry['allowed_mismatch_in_meters']:
        if 'info_about_known_failures' in entry:
            if geocoder.identifier in entry['info_about_known_failures']:
                print(entry['info_about_known_failures'][geocoder.identifier], " - failure was expected!")
        return True
    print('allowed mismatch:', format_distance(entry['allowed_mismatch_in_meters']))
    print('mismatch:', format_distance(distance_in_m))
    print("expected: " + osm_url_pin(entry["lat"], entry["lon"]))
    print("returned: " + osm_url_pin(location.latitude, location.longitude))
    if 'info_about_known_failures' in entry:
        if geocoder.identifier in entry['info_about_known_failures']:
            print('failure reason:', entry['info_about_known_failures'][geocoder.identifier])
    print(header)
    print()
    return False

main()