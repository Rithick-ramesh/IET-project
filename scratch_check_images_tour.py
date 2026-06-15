import os
import re

templates_dir = r'templates'
for file in sorted(os.listdir(templates_dir)):
    if file.endswith('.html'):
        path = os.path.join(templates_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Search for images tour/ or similar strings
        matches = re.findall(r'images tour/[^\'\"]+', content)
        if matches:
            print(f"=== {file} ===")
            for m in matches:
                print(f"  Found: {m}")
