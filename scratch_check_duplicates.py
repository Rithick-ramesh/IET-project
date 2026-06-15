import os
import sys
import re

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from myapp.real_destinations_metadata import STATE_DETAILS, CITY_DETAILS
from myapp.real_attractions_data import REAL_ATTRACTIONS

# Check for duplicate image URLs in STATE_DETAILS and CITY_DETAILS
images = []
descriptions = []

print("=== STATE DETAILS ===")
for key, data in STATE_DETAILS.items():
    img = data.get('image')
    ab_img = data.get('about_image')
    desc = data.get('description')
    
    if img:
        images.append((img, f"state:{key}:image"))
    if ab_img:
        images.append((ab_img, f"state:{key}:about_image"))
    if desc:
        descriptions.append((desc, f"state:{key}"))

print("=== CITY DETAILS ===")
for key, data in CITY_DETAILS.items():
    img = data.get('image')
    ab_img = data.get('about_image')
    desc = data.get('description')
    
    if img:
        images.append((img, f"city:{key}:image"))
    if ab_img:
        images.append((ab_img, f"city:{key}:about_image"))
    if desc:
        descriptions.append((desc, f"city:{key}"))

print("=== REAL ATTRACTIONS ===")
for key, att_list in REAL_ATTRACTIONS.items():
    for idx, att in enumerate(att_list):
        img = att.get('image')
        desc = att.get('desc')
        if img:
            images.append((img, f"attraction:{key}:{idx}:image"))
        if desc:
            descriptions.append((desc, f"attraction:{key}:{idx}"))

# Find duplicate images (base photo IDs)
photo_id_to_sources = {}
for url, src in images:
    match = re.search(r'photo-[a-zA-Z0-9\-]+', url)
    if match:
        photo_id = match.group(0)
    else:
        photo_id = url
    if photo_id not in photo_id_to_sources:
        photo_id_to_sources[photo_id] = []
    photo_id_to_sources[photo_id].append((url, src))

duplicates = {k: v for k, v in photo_id_to_sources.items() if len(v) > 1}

print(f"\nTotal unique base photo IDs: {len(photo_id_to_sources)}")
print(f"Total base photo IDs with duplicates: {len(duplicates)}")
print("\nSome duplicate groups:")
count = 0
for pid, sources in sorted(duplicates.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"\nPhoto ID: {pid} (used {len(sources)} times)")
    for url, src in sources[:5]:
        print(f"  - {src}: {url}")
    count += 1
    if count >= 10:
        break

# Find duplicate descriptions
desc_to_sources = {}
for desc, src in descriptions:
    clean_desc = desc.strip().lower()
    if clean_desc not in desc_to_sources:
        desc_to_sources[clean_desc] = []
    desc_to_sources[clean_desc].append((desc, src))

duplicate_descs = {k: v for k, v in desc_to_sources.items() if len(v) > 1}
print(f"\nTotal unique descriptions: {len(desc_to_sources)}")
print(f"Total descriptions with duplicates: {len(duplicate_descs)}")
for d, sources in list(duplicate_descs.items())[:5]:
    print(f"\nDuplicate Description (used {len(sources)} times): '{d[:60]}...'")
    for orig_d, src in sources:
        print(f"  - {src}")
