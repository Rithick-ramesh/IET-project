with open('static/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

for term in ['.hotel-card', '.hotel-container', '.hotel-category', '.hotels-section', 'hotel']:
    print(f"'{term}' in style.css: {term in content}")
