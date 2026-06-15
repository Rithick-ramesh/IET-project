import urllib.request
import json
import re

url = "https://picsum.photos/v2/list?page=1&limit=100"
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        print(f"Successfully fetched {len(data)} images.")
        print("First few items:")
        for item in data[:5]:
            # Get download url: e.g. "https://unsplash.com/photos/yC-Yzbqy7PY" or similar
            # let's extract the ID part at the end
            download_url = item.get('download_url')
            # Look for ID in download_url: e.g. https://picsum.photos/id/0/5000/3333 or similar
            # Wait, download_url is e.g. https://images.unsplash.com/... or picsum...
            print(f"  ID: {item.get('id')}, Author: {item.get('author')}, URL: {download_url}")
except Exception as e:
    print(f"Error: {e}")
