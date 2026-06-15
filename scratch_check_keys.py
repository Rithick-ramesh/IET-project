import os
import sys

# Add myapp to path if needed
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from myapp.real_destinations_metadata import CITY_DETAILS
from myapp.destinations_data import DESTINATIONS

print("CITY_DETAILS keys count:", len(CITY_DETAILS))
print("bengaluru in CITY_DETAILS:", 'bengaluru' in CITY_DETAILS)
if 'bengaluru' in CITY_DETAILS:
    print("CITY_DETAILS['bengaluru']:", CITY_DETAILS['bengaluru'])

print("\nDESTINATIONS['bengaluru']:", DESTINATIONS.get('bengaluru'))
