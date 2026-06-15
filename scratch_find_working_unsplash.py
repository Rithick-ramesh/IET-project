import os
import re
import urllib.request
import urllib.error

# Regex to match photo-XXXXXXXXXXXXX-XXXXXXXXXXXX
pattern = re.compile(r'photo-\d+-[a-f0-9]+')
all_ids = set()

# Scan all python, html, and json files in the project
for root, dirs, files in os.walk('.'):
    # Exclude directories we don't want to scan
    if any(p in root for p in ['myenv', '.git', '.gemini', 'scratch', 'logs', '.system_generated']):
        continue
    for f in files:
        if f.endswith(('.py', '.html', '.json', '.bak')):
            try:
                with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
                    content = file.read()
                    matches = pattern.findall(content)
                    for m in matches:
                        all_ids.add(m)
            except Exception:
                pass

print(f"Total unique Unsplash photo IDs found in project codebase: {len(all_ids)}")

# Test each one
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
working_ids = []
broken_ids = []

for idx, pid in enumerate(sorted(all_ids)):
    url = f"https://images.unsplash.com/photo-{pid.split('photo-')[-1]}?q=80&w=800&auto=format&fit=crop"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                working_ids.append(pid)
            else:
                broken_ids.append((pid, response.status))
    except urllib.error.HTTPError as e:
        broken_ids.append((pid, e.code))
    except Exception as e:
        broken_ids.append((pid, str(e)))

print(f"\nTested {len(all_ids)} IDs:")
print(f"Working: {len(working_ids)}")
print(f"Broken/Failed: {len(broken_ids)}")

print("\n--- WORKING IDS (ready to copy) ---")
for pid in working_ids:
    print(f"    '{pid}',")

print("\n--- BROKEN/FAILED IDS ---")
for pid, err in broken_ids:
    print(f"    '{pid}': {err},")
