import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from myapp.real_destinations_metadata import STATE_DETAILS, CITY_DETAILS
from myapp.destinations_data import states_metadata, DESTINATIONS

print("--- Checking Bengaluru Flow ---")
city_key = 'bengaluru'
state_key = 'karnataka'
state_data = states_metadata[state_key]

print(f"city_key: {city_key}")
print(f"city_key in CITY_DETAILS: {city_key in CITY_DETAILS}")
print(f"city_key in DESTINATIONS: {city_key in DESTINATIONS}")

# Let's print details of bengaluru in DESTINATIONS
bengaluru_dest = DESTINATIONS.get(city_key)
if bengaluru_dest:
    print(f"Compiled name: {bengaluru_dest.get('name')}")
    print(f"Compiled tag: {bengaluru_dest.get('tag')}")
    print(f"Compiled description: {bengaluru_dest.get('description')}")
else:
    print("Bengaluru not in DESTINATIONS!")
