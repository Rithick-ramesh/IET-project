import urllib.request
import json
import re
import time

unsplash_ids = []
seen = set()

headers = {'User-Agent': 'Mozilla/5.0'}

# Picsum has IDs ranging from 0 to 1000+
# Let's check IDs sequentially and extract their original Unsplash URL
print("Fetching Unsplash photo IDs from Picsum Info API...")
count = 0
for i in range(300):
    url = f"https://picsum.photos/id/{i}/info"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            unsplash_url = data.get('url')
            # url is e.g. "https://unsplash.com/photos/yC-Yzbqy7PY"
            # let's extract the last part
            photo_id = unsplash_url.split('/')[-1]
            if photo_id and photo_id not in seen:
                seen.add(photo_id)
                unsplash_ids.append(photo_id)
                count += 1
                if count % 10 == 0:
                    print(f"  Retrieved {count} unique IDs...")
    except Exception:
        # Some IDs might not exist in Picsum, skip them
        pass
    time.sleep(0.02)  # Quick pause to avoid spamming

print(f"\nSuccessfully collected {len(unsplash_ids)} unique Unsplash photo IDs.")
with open('picsum_unsplash_ids.json', 'w', encoding='utf-8') as f:
    json.dump(list(unsplash_ids), f, indent=4)
print("Saved to picsum_unsplash_ids.json")
