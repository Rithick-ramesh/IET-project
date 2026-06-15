import os

search_word = 'historic spiritual town'
results = []

for root, dirs, files in os.walk('.'):
    # Skip environment and git folders
    if 'myenv' in root or '.git' in root or '.gemini' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.js', '.py', '.json', '.css')):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if search_word in content.lower():
                        results.append(path)
            except Exception:
                pass

print("Files containing 'historic spiritual town':")
for r in results:
    print(r)
