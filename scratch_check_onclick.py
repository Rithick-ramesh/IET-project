import os
import re

templates_dir = r'templates'
for file in sorted(os.listdir(templates_dir)):
    if file.endswith('.html'):
        path = os.path.join(templates_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if 'onclick' in line and ('location' in line or 'href' in line):
                print(f'{file}:{i}: {line.strip()}')
