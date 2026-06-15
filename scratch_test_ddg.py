import urllib.request
import re

url = "https://html.duckduckgo.com/html/?q=site:images.unsplash.com/photo-+temple+india"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        # Look for photo IDs
        matches = re.findall(r'photo-[a-zA-Z0-9\-]+', html)
        seen = set()
        unique = []
        for m in matches:
            if len(m) > 12 and m not in seen:
                seen.add(m)
                unique.append(m)
        print(f"DuckDuckGo found {len(unique)} unique photo IDs.")
        print("First few:")
        for u in unique[:10]:
            print(f"  {u}")
except Exception as e:
    print(f"Error: {e}")
