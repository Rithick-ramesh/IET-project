import re

filepath = 'myapp/destinations_data.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add import statement at the top of the file
import_target = "from .custom_destinations_data import CUSTOM_DESTINATIONS"
import_replacement = "from .custom_destinations_data import CUSTOM_DESTINATIONS\nfrom .real_attractions_data import REAL_ATTRACTIONS"

if import_target in content and import_replacement not in content:
    content = content.replace(import_target, import_replacement, 1)
    print("Added import statement.")

# 2. Update state fallback attractions to include both 'desc' and 'description' keys
state_attractions_target = """    else:
        attractions = [
            {
                'name': f"Famous Landmark of {data['name']}",
                'image': get_dynamic_photo(f"{data['name']},landmark", img_sig + 1),
                'desc': f"Experience the majestic views and heritage of {data['name']} at this iconic site."
            },
            {
                'name': f"Scenic Nature Trail in {data['name']}",
                'image': get_dynamic_photo(f"{data['name']},nature", img_sig + 2),
                'desc': f"Take a relaxing walk through the beautiful forests and nature parks of {data['name']}."
            },
            {
                'name': f"Ancient Spiritual Center in {data['name']}",
                'image': get_dynamic_photo(f"{data['name']},temple", img_sig + 3),
                'desc': f"Immerse yourself in local traditions at this historic spiritual destination."
            }
        ]"""

state_attractions_replacement = """    else:
        attractions = [
            {
                'name': f"Famous Landmark of {data['name']}",
                'image': get_dynamic_photo(f"{data['name']},landmark", img_sig + 1),
                'desc': f"Experience the majestic views and heritage of {data['name']} at this iconic site.",
                'description': f"Experience the majestic views and heritage of {data['name']} at this iconic site."
            },
            {
                'name': f"Scenic Nature Trail in {data['name']}",
                'image': get_dynamic_photo(f"{data['name']},nature", img_sig + 2),
                'desc': f"Take a relaxing walk through the beautiful forests and nature parks of {data['name']}.",
                'description': f"Take a relaxing walk through the beautiful forests and nature parks of {data['name']}."
            },
            {
                'name': f"Ancient Spiritual Center in {data['name']}",
                'image': get_dynamic_photo(f"{data['name']},temple", img_sig + 3),
                'desc': f"Immerse yourself in local traditions at this historic spiritual destination.",
                'description': f"Immerse yourself in local traditions at this historic spiritual destination."
            }
        ]"""

if state_attractions_target in content:
    content = content.replace(state_attractions_target, state_attractions_replacement, 1)
    print("Updated state fallback attractions keys.")
else:
    print("Warning: Could not exact-match state fallback attractions target.")

# 3. Replace the entire city attractions generator logic (lines 637 to 709 approx)
# Let's target from `if city_key == 'gaya':` up to `attractions = [` and the fallback.
# We will use regex or string replace to clean this up.

city_attractions_block_pattern = r'        if city_key == \'gaya\':.*?        img_sig \+= 4'

city_attractions_replacement = """        if city_key in REAL_ATTRACTIONS:
            attractions = REAL_ATTRACTIONS[city_key]
        elif city_key == 'diu':
            attractions = [
                {
                    'name': "Naida Caves",
                    'image': "/static/images/section image3.jpg",
                    'desc': "A breathtaking network of interlinked stone caves located near the Diu Fort, famous for natural sunlight openings.",
                    'description': "A breathtaking network of interlinked stone caves located near the Diu Fort, famous for natural sunlight openings."
                },
                {
                    'name': "Diu Scenic Point",
                    'image': get_dynamic_photo("diu,nature", img_sig + 2),
                    'desc': "A serene scenic park and lake, perfect for boat rides and peaceful walks in Diu.",
                    'description': "A serene scenic park and lake, perfect for boat rides and peaceful walks in Diu."
                },
                {
                    'name': "Diu Spiritual Center",
                    'image': get_dynamic_photo("diu,temple", img_sig + 3),
                    'desc': "An ancient spiritual sanctuary in Diu filled with peace and local devotion.",
                    'description': "An ancient spiritual sanctuary in Diu filled with peace and local devotion."
                }
            ]
        else:
            attractions = [
                {
                    'name': f"{city_name} Heritage Site",
                    'image': get_dynamic_photo(f"{city_name},landmark", img_sig + 1),
                    'desc': f"A beautiful heritage landmark in {city_name} showing rich local design and history.",
                    'description': f"A beautiful heritage landmark in {city_name} showing rich local design and history."
                },
                {
                    'name': f"{city_name} Scenic Point",
                    'image': get_dynamic_photo(f"{city_name},nature", img_sig + 2),
                    'desc': f"A serene scenic park and lake, perfect for boat rides and peaceful walks in {city_name}.",
                    'description': f"A serene scenic park and lake, perfect for boat rides and peaceful walks in {city_name}."
                },
                {
                    'name': f"{city_name} Spiritual Center",
                    'image': get_dynamic_photo(f"{city_name},temple", img_sig + 3),
                    'desc': f"An ancient spiritual sanctuary in {city_name} filled with peace and local devotion.",
                    'description': f"An ancient spiritual sanctuary in {city_name} filled with peace and local devotion."
                }
            ]
        img_sig += 4"""

new_content, count = re.subn(city_attractions_block_pattern, city_attractions_replacement, content, flags=re.DOTALL)
if count > 0:
    content = new_content
    print(f"Successfully replaced city attractions generator block (replaced {count} match).")
else:
    print("Warning: Could not match city attractions generator block pattern.")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved patched file.")
