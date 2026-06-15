import urllib.request
import re

test_ids = [0, 1, 2, 3, 4]
headers = {'User-Agent': 'Mozilla/5.0'}

for tid in test_ids:
    url = f"https://picsum.photos/id/{tid}/800/600"
    req = urllib.request.Request(url, headers=headers)
    try:
        # We open the URL and get the final URL after redirects
        with urllib.request.urlopen(req, timeout=5) as response:
            final_url = response.geturl()
            # Find photo-xxxxxxxxxxxxx
            match = re.search(r'photo-[a-zA-Z0-9\-]+', final_url)
            if match:
                photo_id = match.group(0)
                print(f"Picsum {tid} -> Unsplash CDN URL: {final_url}")
                print(f"  Extracted ID: {photo_id}")
            else:
                print(f"Picsum {tid} -> Unsplash CDN URL: {final_url} (No ID match)")
    except Exception as e:
        print(f"Picsum {tid} -> Failed with {e}")
