This is a tool to easily benchmark and compare quality of different geocoders.

It test quality of geolocating - to be more specific, text to location transformation.

For example text such as "Długa 12, Kraków" should be located somewhere close to [50.06715; 19.93860](https://www.openstreetmap.org/?mlat=50.06715&mlon=19.93860#map=19/50.06715/19.93860).

This repository contains simple to setup Python code running tests and base dataset.

Repository with cached test results will be also setup and linked here once created.

## Limitations

Note that test is heavily biased toward OSM as it was created by an [active OSM contributor](https://www.openstreetmap.org/user/Mateusz%20Konieczny/history) who fixes or at least [reports](https://wiki.openstreetmap.org/wiki/Notes) any noticed problems with OSM data.

In addition, tests were mostly created based on OSM data.

At least initial data sample is extremely biased toward Poland (only Poland?), but pull requests extending coverage are welcomed.

For obvious reasons test is exluding geocoders without free tier/trial. And services with time-limited trial may be listed with outdated results.

To keep running it manageable (also under limitations of trial plans) it is preferable to avoid complete duplicates to avoid inflating number of tests without benefit.

# Installation

Requires Python 3 and dependencies specified in `requirements.txt`.

To install dependencies: `pip install -r requirements.txt` (`pip3 install -r requirements.txt` if `pip` is still for Python2)

Run `create_config_file.py` file using python3 (likely with command such as `python3 create_config_file.py`).

It will ask about some info and will store it in a config file used by other software. Answers, including database password, will be saved in plaintext. It is advisable to delete created config file only no longer needed and/or change database password.

## Contributing

Adding support for more geocoders or adding more test is welcomed.

## License

Code:

GNU Affero General Public License v3.0

Test data:

ODBL, data collected by OpenStreetMap mappers

## Similar things
* [https://getlon.lat/](https://getlon.lat/) - compares pricing plans of various geocoders. This tool compares geocoding quality, on specific examples.
* [geocoders/geocoder-tester](https://github.com/geocoders/geocoder-tester) - seems to be about something related to a dead proposal.
* [pelias/fuzzy-tester](https://github.com/pelias/fuzzy-tester) - tool optimized for large scale testing of a specific geocoder, for use as a part of a test suite. Intended to produce single score from thousands of tests, but richer than a binary pass/fail.
* * My tool is intended to list specific differences between different geocoders not just a single opaque number.
* * My tool is not intended to be tightly coupled with a specific geocoder but rather test multiple
* * My tool is intended to generate a website with comparison/report, not a single number
* * My tool is intended to be easy to setup and run as a Python script

## Maintemance tools

`autopep8 --in-place --recursive . --jobs 0 --max-line-length 900` is a nice reformatting command.

# Where is Google?

Overall, Google ToS is insane and is in unique position of being a company that may cause big losses for me by banning me from their service and bricking my devices.

Therefore at this point I will not touch any additional Google services, especially ones where I would be calling some APIs.

To be more specific Google automated banning system has no way to appeal. And I am scared that Google may remotely brick my smartphone or lock me out of my primary email account. Therefore I am not going to use any additional Google services.

## Terms of service set by Google

 - Their [ToS](https://enterprise.google.com/maps/terms/us/maps_purchase_agreement_emea.html) forbids "attempt to reverse engineer the Service or any component or attempt to create a substitute or similar service through use of or access to the Service" and this tool is created to improve a specialized geocoding tool that I am developing (and potentially create new one [if someone else will hire me](mailto:matkoniecz@gmail.com))
 - Their ToS also forbids "use or display the Content on or in conjunction with a non-Google map (by way of example, geocodes obtained through the Service may not be used or displayed except with a Google Map)"
 - Separately stored [additional ToS](https://cloud.google.com/maps-platform/terms) is further restricting people "Customer will not: (i) pre-fetch, index, store, reshare, or rehost Google Maps Content outside the services"
 - As I am unable to restrict who visits this page I am also unable to follow "No Use in Prohibited Territories. Customer will not distribute or market in a Prohibited Territory any Customer Application(s) that use the Google Maps Core Services."
  - And, yes I would have to ensure this: "Customer will: (a) ensure that Customer’s and its End Users’ use of the Services complies with the Agreement"
   - I am really curious how I am supposed to ensure that noone is using it to "reverse engineer the Service or any component"

## But I want to compare with Google

Feel free to do this. If you decide to publish results - please open an issue here or contact me in other way. I am curious about results.

Geopy has support for [Google API](https://geopy.readthedocs.io/en/latest/#googlev3) so code should be trivial.

I would gladly link to it.