with open(r"c:\Users\Rithick prabhu\OneDrive\Desktop\tourism backgroung\myproject\myapp\custom_destinations_data.py", "r", encoding="utf-8") as f:
    content = f.read()

for term in ["gaya", "mahabodhi", "anjuna", "gateway", "naida", "diu"]:
    if term in content.lower():
        print(f"Term '{term}' is found in custom_destinations_data.py")
    else:
        print(f"Term '{term}' is NOT found in custom_destinations_data.py")
