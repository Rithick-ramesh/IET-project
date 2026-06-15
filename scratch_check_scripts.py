import os
import re

templates_dir = r'templates'
for file in sorted(os.listdir(templates_dir)):
    if file.endswith('.html'):
        path = os.path.join(templates_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        scripts = re.findall(r'<script [^>]*src=[^>]*>', content)
        print(f'{file}:')
        for script in scripts:
            print(f'  {script}')
