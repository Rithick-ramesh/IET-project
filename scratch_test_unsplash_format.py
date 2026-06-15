import urllib.request

test_ids = ["yC-Yzbqy7PY", "LNRyGwIJr5c", "N7XodRrbzS0", "Dl6jeyfihLk", "y83Je1OC6Wc"]
headers = {'User-Agent': 'Mozilla/5.0'}

for tid in test_ids:
    url = f"https://images.unsplash.com/photo-{tid}?q=80&w=800&auto=format&fit=crop"
    req = urllib.request.Request(url, headers=headers, method='HEAD')
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            print(f"ID {tid}: Status {response.status}")
    except Exception as e:
        print(f"ID {tid}: Failed with {e}")
