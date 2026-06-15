import urllib.request
import re
import json

urls = [
    "https://raw.githubusercontent.com/souravsb66/WanderWorld/main/db.json",
    "https://raw.githubusercontent.com/aditya-kri/travel-website/master/src/data/db.json",
    "https://raw.githubusercontent.com/Shubham-Sardar/Travel-Planner/main/src/db/destinations.json"
]

unsplash_pattern = re.compile(r'photo-[a-zA-Z0-9\-]+')
all_ids = set()

headers = {'User-Agent': 'Mozilla/5.0'}

for url in urls:
    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            matches = unsplash_pattern.findall(content)
            print(f"  Found {len(matches)} matches.")
            for m in matches:
                if len(m) > 12:
                    all_ids.add(m)
    except Exception as e:
        print(f"  Error: {e}")

print(f"\nTotal unique Unsplash photo IDs found: {len(all_ids)}")
if all_ids:
    print("First 10 IDs:")
    for i in list(all_ids)[:10]:
        print(f"  '{i}',")
