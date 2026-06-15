with open('static/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
for i, line in enumerate(lines, 1):
    if 'hotel' in line.lower():
        print(f"Line {i}: {line.strip()}")
