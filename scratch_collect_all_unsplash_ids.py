import os
import re

unsplash_pattern = re.compile(r'photo-[a-zA-Z0-9\-]+')
all_ids = set()

for root, dirs, files in os.walk('.'):
    if 'myenv' in root or '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.py', '.html', '.json')):
            try:
                with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
                    content = file.read()
                    matches = unsplash_pattern.findall(content)
                    for m in matches:
                        all_ids.add(m)
            except Exception:
                pass

print(f"Total unique Unsplash photo IDs found in codebase: {len(all_ids)}")
print("List of some photo IDs:")
for i in list(all_ids)[:30]:
    print(f"'{i}',")
