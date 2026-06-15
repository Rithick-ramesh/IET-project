import os
import sys
import json

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from myapp.destinations_data import DESTINATIONS

bengaluru_data = DESTINATIONS.get('bengaluru')

with open('bengaluru_compiled.json', 'w', encoding='utf-8') as f:
    json.dump(bengaluru_data, f, indent=4, ensure_ascii=False)

print("Saved to bengaluru_compiled.json")
