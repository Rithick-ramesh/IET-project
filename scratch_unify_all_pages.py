import os
import re

templates_dir = r'templates'
static_css_dir = r'static/css'

templates = [
    'About.html', 'Goa.html', 'agra.html', 'ai_planner.html', 
    'contact us.html', 'destination.html', 'destination_detail.html', 
    'homepage.html', 'jaipur.html', 'kashmir.html', 'kerala.html', 'varanasi.html'
]

# Bootstrap 5.3.3 CSS & JS, Font Awesome, and Poppins Google Font CDNs
bootstrap_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">'
font_awesome = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'
google_font = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>'

poppins_body_style = """
    body {
        font-family: 'Poppins', sans-serif !important;
    }
"""

def backup_file(path):
    if os.path.exists(path):
        backup_path = path + '.bak'
        if not os.path.exists(backup_path):
            with open(path, 'r', encoding='utf-8') as src:
                with open(backup_path, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
            print(f"Created backup for {path}")

# ========================================================
# 1. STANDARDIZE CDNs AND SCRIPTS ON ALL TEMPLATES
# ========================================================
print("\n--- Standardizing CDNs on Templates ---")
for t_file in templates:
    path = os.path.join(templates_dir, t_file)
    if not os.path.exists(path):
        print(f"Warning: {path} not found.")
        continue
        
    backup_file(path)
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check/insert Bootstrap CSS
    if 'bootstrap@5.3.3/dist/css/bootstrap' not in content and 'bootstrap.min.css' not in content:
        # Insert inside head
        content = content.replace('<head>', f'<head>\n  {bootstrap_css}', 1)
        print(f"Added Bootstrap CSS to {t_file}")
        
    # Check/insert Font Awesome
    if 'font-awesome' not in content and 'cdnjs.cloudflare.com/ajax/libs/font-awesome' not in content:
        content = content.replace('<head>', f'<head>\n  {font_awesome}', 1)
        print(f"Added Font Awesome to {t_file}")
        
    # Check/insert Poppins Google Font
    if 'Poppins' not in content:
        content = content.replace('<head>', f'<head>\n  {google_font}', 1)
        print(f"Added Poppins Font to {t_file}")
        
    # Check/insert Poppins Body Style
    if 'Poppins' in content and 'font-family' not in content:
        # Create style block if doesn't exist
        if '<style>' in content:
            content = content.replace('<style>', f'<style>\n{poppins_body_style}', 1)
        else:
            style_block = f"<style>{poppins_body_style}</style>\n</head>"
            content = content.replace('</head>', style_block, 1)
        print(f"Added Poppins Font Style to {t_file}")
        
    # Check/insert Bootstrap JS
    if 'bootstrap.bundle.min.js' not in content:
        content = content.replace('</body>', f'  {bootstrap_js}\n</body>', 1)
        print(f"Added Bootstrap JS to {t_file}")
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ========================================================
# 2. UPDATE HOMEPAGE CARDS MARKUP
# ========================================================
print("\n--- Updating Homepage Cards to Anchors ---")
homepage_path = os.path.join(templates_dir, 'homepage.html')
if os.path.exists(homepage_path):
    with open(homepage_path, 'r', encoding='utf-8') as f:
        hp_content = f.read()

    # 2.1 Wrap Crafts Slider Cards in Anchors
    crafts_section_target = """                <!-- CARD 1 -->
                <div class="craft-card-slide">
                    <div class="card craft-card h-100 shadow-sm" onclick="window.location.href='{% url 'destination' %}?q=punjab';">
                        <img src="{% static 'images/traditional section 1.avif' %}" alt="Punjab Phulkari">
                        <div class="card-body" style="background: #fff9f2; padding: 20px;">
                            <div class="state">Punjab</div>
                            <h5 class="craft-name fw-bold mb-0">Phulkari Embroidery</h5>
                        </div>
                    </div>
                </div>

                <!-- CARD 2 -->
                <div class="craft-card-slide">
                    <div class="card craft-card h-100 shadow-sm" onclick="window.location.href='{% url 'destination' %}?q=chhattisgarh';">
                        <img src="{% static 'images/traditional section 2.avif' %}" alt="Chhattisgarh Bastar Dhokra">
                        <div class="card-body" style="background: #fff9f2; padding: 20px;">
                            <div class="state">Chhattisgarh</div>
                            <h5 class="craft-name fw-bold mb-0">Bastar Dhokra Art</h5>
                        </div>
                    </div>
                </div>

                <!-- CARD 3 -->
                <div class="craft-card-slide">
                    <div class="card craft-card h-100 shadow-sm" onclick="window.location.href='{% url 'destination' %}?q=gujarat';">
                        <img src="{% static 'images/traditional section 3.avif' %}" alt="Gujarat Patan Patola">
                        <div class="card-body" style="background: #fff9f2; padding: 20px;">
                            <div class="state">Gujarat</div>
                            <h5 class="craft-name fw-bold mb-0">Patan Patola Silk</h5>
                        </div>
                    </div>
                </div>

                <!-- CARD 4 -->
                <div class="craft-card-slide">
                    <div class="card craft-card h-100 shadow-sm" onclick="window.location.href='{% url 'kashmir' %}';">
                        <img src="{% static 'images/traditional section 4.avif' %}" alt="Kashmir Pashmina">
                        <div class="card-body" style="background: #fff9f2; padding: 20px;">
                            <div class="state">Kashmir</div>
                            <h5 class="craft-name fw-bold mb-0">Pashmina Shawls</h5>
                        </div>
                    </div>
                </div>

                <!-- CARD 5 -->
                <div class="craft-card-slide">
                    <div class="card craft-card h-100 shadow-sm" onclick="window.location.href='{% url 'jaipur' %}';">
                        <img src="{% static 'images/jaipur image2.jpg' %}" alt="Rajasthan Blue Pottery">
                        <div class="card-body" style="background: #fff9f2; padding: 20px;">
                            <div class="state">Rajasthan</div>
                            <h5 class="craft-name fw-bold mb-0">Blue Pottery</h5>
                        </div>
                    </div>
                </div>

                <!-- CARD 6 -->
                <div class="craft-card-slide">
                    <div class="card craft-card h-100 shadow-sm" onclick="window.location.href='{% url 'varanasi' %}';">
                        <img src="{% static 'images/varanasi image1.jpg' %}" alt="Uttar Pradesh Banarasi Silk">
                        <div class="card-body" style="background: #fff9f2; padding: 20px;">
                            <div class="state">Uttar Pradesh</div>
                            <h5 class="craft-name fw-bold mb-0">Banarasi Silk</h5>
                        </div>
                    </div>
                </div>"""

    crafts_section_replacement = """                <!-- CARD 1 -->
                <div class="craft-card-slide">
                    <a href="{% url 'destination' %}?q=punjab" class="text-decoration-none text-dark d-block h-100">
                        <div class="card craft-card h-100 shadow-sm">
                            <img src="{% static 'images/traditional section 1.avif' %}" alt="Punjab Phulkari">
                            <div class="card-body" style="background: #fff9f2; padding: 20px;">
                                <div class="state">Punjab</div>
                                <h5 class="craft-name fw-bold mb-0">Phulkari Embroidery</h5>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- CARD 2 -->
                <div class="craft-card-slide">
                    <a href="{% url 'destination' %}?q=chhattisgarh" class="text-decoration-none text-dark d-block h-100">
                        <div class="card craft-card h-100 shadow-sm">
                            <img src="{% static 'images/traditional section 2.avif' %}" alt="Chhattisgarh Bastar Dhokra">
                            <div class="card-body" style="background: #fff9f2; padding: 20px;">
                                <div class="state">Chhattisgarh</div>
                                <h5 class="craft-name fw-bold mb-0">Bastar Dhokra Art</h5>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- CARD 3 -->
                <div class="craft-card-slide">
                    <a href="{% url 'destination' %}?q=gujarat" class="text-decoration-none text-dark d-block h-100">
                        <div class="card craft-card h-100 shadow-sm">
                            <img src="{% static 'images/traditional section 3.avif' %}" alt="Gujarat Patan Patola">
                            <div class="card-body" style="background: #fff9f2; padding: 20px;">
                                <div class="state">Gujarat</div>
                                <h5 class="craft-name fw-bold mb-0">Patan Patola Silk</h5>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- CARD 4 -->
                <div class="craft-card-slide">
                    <a href="{% url 'kashmir' %}" class="text-decoration-none text-dark d-block h-100">
                        <div class="card craft-card h-100 shadow-sm">
                            <img src="{% static 'images/traditional section 4.avif' %}" alt="Kashmir Pashmina">
                            <div class="card-body" style="background: #fff9f2; padding: 20px;">
                                <div class="state">Kashmir</div>
                                <h5 class="craft-name fw-bold mb-0">Pashmina Shawls</h5>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- CARD 5 -->
                <div class="craft-card-slide">
                    <a href="{% url 'jaipur' %}" class="text-decoration-none text-dark d-block h-100">
                        <div class="card craft-card h-100 shadow-sm">
                            <img src="{% static 'images/jaipur image2.jpg' %}" alt="Rajasthan Blue Pottery">
                            <div class="card-body" style="background: #fff9f2; padding: 20px;">
                                <div class="state">Rajasthan</div>
                                <h5 class="craft-name fw-bold mb-0">Blue Pottery</h5>
                            </div>
                        </div>
                    </a>
                </div>

                <!-- CARD 6 -->
                <div class="craft-card-slide">
                    <a href="{% url 'varanasi' %}" class="text-decoration-none text-dark d-block h-100">
                        <div class="card craft-card h-100 shadow-sm">
                            <img src="{% static 'images/varanasi image1.jpg' %}" alt="Uttar Pradesh Banarasi Silk">
                            <div class="card-body" style="background: #fff9f2; padding: 20px;">
                                <div class="state">Uttar Pradesh</div>
                                <h5 class="craft-name fw-bold mb-0">Banarasi Silk</h5>
                            </div>
                        </div>
                    </a>
                </div>"""

    if crafts_section_target in hp_content:
        hp_content = hp_content.replace(crafts_section_target, crafts_section_replacement)
        print("Updated Crafts slider cards to native links.")
    else:
        # Fallback regex substitution
        hp_content = re.sub(
            r'<div class="card craft-card h-100 shadow-sm" onclick="window\.location\.href=\'\{% url \'([^\']+)\' %\}\?q=([^\'\"]+)\';">',
            r'<a href="{% url \'\1\' %}?q=\2" class="text-decoration-none text-dark d-block h-100"><div class="card craft-card h-100 shadow-sm">',
            hp_content
        )
        hp_content = re.sub(
            r'<div class="card craft-card h-100 shadow-sm" onclick="window\.location\.href=\'\{% url \'([^\']+)\' %\}\';">',
            r'<a href="{% url \'\1\' %}" class="text-decoration-none text-dark d-block h-100"><div class="card craft-card h-100 shadow-sm">',
            hp_content
        )
        # We need to add closing tags inside .craft-card-slide divs
        # Let's target the card image & body contents to close anchor tags nicely.
        hp_content = re.sub(
            r'(<div class="card-body" style="background: #fff9f2; padding: 20px;">.*?</h5>\s*</div>\s*</div>)\s*(</div>\s*<!-- CARD)',
            r'\1</a>\2',
            hp_content,
            flags=re.DOTALL
        )
        hp_content = re.sub(
            r'(<div class="card-body" style="background: #fff9f2; padding: 20px;">.*?</h5>\s*</div>\s*</div>)\s*(</div>\s*</div>\s*<button class="slider-arrow next-arrow")',
            r'\1</a>\2',
            hp_content,
            flags=re.DOTALL
        )
        print("Regex replaced Crafts slider cards.")

    # 2.2 Wrap Recommended Destination Cards in Anchors
    destination_section_target = """        <div class="row g-4">

            <div class="col-md-3 col-sm-6">
                <div class="destination-card shadow-sm" onclick="window.location.href='{% url 'jaipur' %}';" style="cursor: pointer; border-radius: 18px; overflow: hidden; background: white; transition: 0.3s; height: 100%;">
                    <img src="{% static 'images/jaipur image1.webp' %}" alt="Jaipur" style="width: 100%; height: 220px; object-fit: cover; transition: 0.5s;">
                    <div class="card-body" style="padding: 20px; text-align: center;">
                        <h5 class="fw-bold mb-1" style="font-size: 18px; color: #222;">Jaipur</h5>
                        <p class="text-muted mb-0" style="font-size: 14px;">Royal Heritage Experience</p>
                    </div>
                </div>
            </div>

            <div class="col-md-3 col-sm-6">
                <div class="destination-card shadow-sm" onclick="window.location.href='{% url 'kashmir' %}';" style="cursor: pointer; border-radius: 18px; overflow: hidden; background: white; transition: 0.3s; height: 100%;">
                    <img src="{% static 'images/kashmir image1.jpg' %}" alt="Kashmir" style="width: 100%; height: 220px; object-fit: cover; transition: 0.5s;">
                    <div class="card-body" style="padding: 20px; text-align: center;">
                        <h5 class="fw-bold mb-1" style="font-size: 18px; color: #222;">Kashmir</h5>
                        <p class="text-muted mb-0" style="font-size: 14px;">Heaven On Earth</p>
                    </div>
                </div>
            </div>

            <div class="col-md-3 col-sm-6">
                <div class="destination-card shadow-sm" onclick="window.location.href='{% url 'varanasi' %}';" style="cursor: pointer; border-radius: 18px; overflow: hidden; background: white; transition: 0.3s; height: 100%;">
                    <img src="{% static 'images/varanasi image1.jpg' %}" alt="Varanasi" style="width: 100%; height: 220px; object-fit: cover; transition: 0.5s;">
                    <div class="card-body" style="padding: 20px; text-align: center;">
                        <h5 class="fw-bold mb-1" style="font-size: 18px; color: #222;">Varanasi</h5>
                        <p class="text-muted mb-0" style="font-size: 14px;">Spiritual Tourism</p>
                    </div>
                </div>
            </div>

            <div class="col-md-3 col-sm-6">
                <div class="destination-card shadow-sm" onclick="window.location.href='{% url 'goa' %}';" style="cursor: pointer; border-radius: 18px; overflow: hidden; background: white; transition: 0.3s; height: 100%;">
                    <img src="{% static 'images/goa image1.webp' %}" alt="Goa" style="width: 100%; height: 220px; object-fit: cover; transition: 0.5s;">
                    <div class="card-body" style="padding: 20px; text-align: center;">
                        <h5 class="fw-bold mb-1" style="font-size: 18px; color: #222;">Goa</h5>
                        <p class="text-muted mb-0" style="font-size: 14px;">Beach Nightlife</p>
                    </div>
                </div>
            </div>

        </div>"""

    destination_section_replacement = """        <div class="row g-4">

            <div class="col-md-3 col-sm-6">
                <a href="{% url 'jaipur' %}" class="text-decoration-none text-dark d-block h-100">
                    <div class="destination-card shadow-sm" style="border-radius: 18px; overflow: hidden; background: white; transition: 0.3s; height: 100%;">
                        <img src="{% static 'images/jaipur image1.webp' %}" alt="Jaipur" style="width: 100%; height: 220px; object-fit: cover; transition: 0.5s;">
                        <div class="card-body" style="padding: 20px; text-align: center;">
                            <h5 class="fw-bold mb-1" style="font-size: 18px; color: #222;">Jaipur</h5>
                            <p class="text-muted mb-0" style="font-size: 14px;">Royal Heritage Experience</p>
                        </div>
                    </div>
                </a>
            </div>

            <div class="col-md-3 col-sm-6">
                <a href="{% url 'kashmir' %}" class="text-decoration-none text-dark d-block h-100">
                    <div class="destination-card shadow-sm" style="border-radius: 18px; overflow: hidden; background: white; transition: 0.3s; height: 100%;">
                        <img src="{% static 'images/kashmir image1.jpg' %}" alt="Kashmir" style="width: 100%; height: 220px; object-fit: cover; transition: 0.5s;">
                        <div class="card-body" style="padding: 20px; text-align: center;">
                            <h5 class="fw-bold mb-1" style="font-size: 18px; color: #222;">Kashmir</h5>
                            <p class="text-muted mb-0" style="font-size: 14px;">Heaven On Earth</p>
                        </div>
                    </div>
                </a>
            </div>

            <div class="col-md-3 col-sm-6">
                <a href="{% url 'varanasi' %}" class="text-decoration-none text-dark d-block h-100">
                    <div class="destination-card shadow-sm" style="border-radius: 18px; overflow: hidden; background: white; transition: 0.3s; height: 100%;">
                        <img src="{% static 'images/varanasi image1.jpg' %}" alt="Varanasi" style="width: 100%; height: 220px; object-fit: cover; transition: 0.5s;">
                        <div class="card-body" style="padding: 20px; text-align: center;">
                            <h5 class="fw-bold mb-1" style="font-size: 18px; color: #222;">Varanasi</h5>
                            <p class="text-muted mb-0" style="font-size: 14px;">Spiritual Tourism</p>
                        </div>
                    </div>
                </a>
            </div>

            <div class="col-md-3 col-sm-6">
                <a href="{% url 'goa' %}" class="text-decoration-none text-dark d-block h-100">
                    <div class="destination-card shadow-sm" style="border-radius: 18px; overflow: hidden; background: white; transition: 0.3s; height: 100%;">
                        <img src="{% static 'images/goa image1.webp' %}" alt="Goa" style="width: 100%; height: 220px; object-fit: cover; transition: 0.5s;">
                        <div class="card-body" style="padding: 20px; text-align: center;">
                            <h5 class="fw-bold mb-1" style="font-size: 18px; color: #222;">Goa</h5>
                            <p class="text-muted mb-0" style="font-size: 14px;">Beach Nightlife</p>
                        </div>
                    </div>
                </a>
            </div>

        </div>"""

    if destination_section_target in hp_content:
        hp_content = hp_content.replace(destination_section_target, destination_section_replacement)
        print("Updated Recommended Destination cards.")
    else:
        print("Error: Could not exact-match Recommended Destination section in homepage.html.")

    # 2.3 Wrap Live Festival Cards in Anchors
    festival_section_target = """        <div class="row g-4">

            <div class="col-md-4">
                <div class="festival-box shadow-sm" onclick="window.location.href='{% url 'jaipur' %}';" style="position: relative; overflow: hidden; border-radius: 18px; height: 350px; cursor: pointer; transition: 0.4s;">
                    <img src="{% static 'images/festival image 1.jpg' %}" alt="Diwali in Jaipur" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div class="festival-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)); display: flex; flex-direction: column; justify-content: flex-end; padding: 25px; color: white;">
                        <span style="font-size: 11px; color: #ffcc00; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px;">Jaipur, Rajasthan</span>
                        <h3 class="fw-bold mb-1" style="font-size: 22px;">Diwali Festival</h3>
                        <p class="mb-0 text-white-50" style="font-size: 13px;">The grand festival of lights, featuring stunning street decorations and traditional bazaars.</p>
                    </div>
                </div>
            </div>

            <div class="col-md-4">
                <div class="festival-box shadow-sm" onclick="window.location.href='{% url 'destination' %}?q=kohima';" style="position: relative; overflow: hidden; border-radius: 18px; height: 350px; cursor: pointer; transition: 0.4s;">
                    <img src="{% static 'images/festival image 2.webp' %}" alt="Hornbill Festival" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div class="festival-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)); display: flex; flex-direction: column; justify-content: flex-end; padding: 25px; color: white;">
                        <span style="font-size: 11px; color: #ffcc00; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px;">Kohima, Nagaland</span>
                        <h3 class="fw-bold mb-1" style="font-size: 22px;">Hornbill Festival</h3>
                        <p class="mb-0 text-white-50" style="font-size: 13px;">A magnificent celebration of Naga tribal heritage, dance, music, and traditional crafts.</p>
                    </div>
                </div>
            </div>

            <div class="col-md-4">
                <div class="festival-box shadow-sm" onclick="window.location.href='{% url 'destination' %}?q=kolkata';" style="position: relative; overflow: hidden; border-radius: 18px; height: 350px; cursor: pointer; transition: 0.4s;">
                    <img src="{% static 'images/festival image 3.webp' %}" alt="Durga Puja" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                    <div class="festival-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)); display: flex; flex-direction: column; justify-content: flex-end; padding: 25px; color: white;">
                        <span style="font-size: 11px; color: #ffcc00; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px;">Kolkata, West Bengal</span>
                        <h3 class="fw-bold mb-1" style="font-size: 22px;">Durga Puja</h3>
                        <p class="mb-0 text-white-50" style="font-size: 13px;">Witness spectacular street art installations (pandals) and drum beats of traditional Dhak.</p>
                    </div>
                </div>
            </div>

        </div>"""

    festival_section_replacement = """        <div class="row g-4">

            <div class="col-md-4">
                <a href="{% url 'jaipur' %}" class="text-decoration-none text-white d-block">
                    <div class="festival-box shadow-sm" style="position: relative; overflow: hidden; border-radius: 18px; height: 350px; transition: 0.4s;">
                        <img src="{% static 'images/festival image 1.jpg' %}" alt="Diwali in Jaipur" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                        <div class="festival-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)); display: flex; flex-direction: column; justify-content: flex-end; padding: 25px; color: white;">
                            <span style="font-size: 11px; color: #ffcc00; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px;">Jaipur, Rajasthan</span>
                            <h3 class="fw-bold mb-1" style="font-size: 22px;">Diwali Festival</h3>
                            <p class="mb-0 text-white-50" style="font-size: 13px;">The grand festival of lights, featuring stunning street decorations and traditional bazaars.</p>
                        </div>
                    </div>
                </a>
            </div>

            <div class="col-md-4">
                <a href="{% url 'destination' %}?q=kohima" class="text-decoration-none text-white d-block">
                    <div class="festival-box shadow-sm" style="position: relative; overflow: hidden; border-radius: 18px; height: 350px; transition: 0.4s;">
                        <img src="{% static 'images/festival image 2.webp' %}" alt="Hornbill Festival" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                        <div class="festival-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)); display: flex; flex-direction: column; justify-content: flex-end; padding: 25px; color: white;">
                            <span style="font-size: 11px; color: #ffcc00; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px;">Kohima, Nagaland</span>
                            <h3 class="fw-bold mb-1" style="font-size: 22px;">Hornbill Festival</h3>
                            <p class="mb-0 text-white-50" style="font-size: 13px;">A magnificent celebration of Naga tribal heritage, dance, music, and traditional crafts.</p>
                        </div>
                    </div>
                </a>
            </div>

            <div class="col-md-4">
                <a href="{% url 'destination' %}?q=kolkata" class="text-decoration-none text-white d-block">
                    <div class="festival-box shadow-sm" style="position: relative; overflow: hidden; border-radius: 18px; height: 350px; transition: 0.4s;">
                        <img src="{% static 'images/festival image 3.webp' %}" alt="Durga Puja" style="width: 100%; height: 100%; object-fit: cover; transition: 0.5s;">
                        <div class="festival-overlay" style="position: absolute; inset: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)); display: flex; flex-direction: column; justify-content: flex-end; padding: 25px; color: white;">
                            <span style="font-size: 11px; color: #ffcc00; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 5px;">Kolkata, West Bengal</span>
                            <h3 class="fw-bold mb-1" style="font-size: 22px;">Durga Puja</h3>
                            <p class="mb-0 text-white-50" style="font-size: 13px;">Witness spectacular street art installations (pandals) and drum beats of traditional Dhak.</p>
                        </div>
                    </div>
                </a>
            </div>

        </div>"""

    if festival_section_target in hp_content:
        hp_content = hp_content.replace(festival_section_target, festival_section_replacement)
        print("Updated Live Festival cards.")
    else:
        print("Error: Could not exact-match Live Festival section in homepage.html.")

    with open(homepage_path, 'w', encoding='utf-8') as f:
        f.write(hp_content)

# ========================================================
# 3. CONFLICTING NAVBAR STYLE CLEANUP & PREMIUM STYLE INJECTION IN style.css
# ========================================================
print("\n--- Updating style.css ---")
style_css_path = os.path.join(static_css_dir, 'style.css')
if os.path.exists(style_css_path):
    backup_file(style_css_path)
    with open(style_css_path, 'r', encoding='utf-8') as f:
        style_content = f.read()

    # Disable old .navbar, .logo, .nav-links rules by renaming them to prevent conflicts
    style_content = style_content.replace('.navbar{', '/* Disabled old navbar style to prevent layout breaks */\n.navbar-old-disabled{')
    style_content = style_content.replace('.logo{', '.logo-old-disabled{')
    style_content = style_content.replace('.nav-links{', '.nav-links-old-disabled{')
    style_content = style_content.replace('.nav-links a{', '.nav-links-a-old-disabled{')
    style_content = style_content.replace('.nav-links a:hover{', '.nav-links-a-hover-old-disabled{')

    # Comment out old navbar rules in mobile responsive overrides
    style_content = style_content.replace('  .navbar{\n    padding:18px 25px;\n    flex-direction:column;\n    gap:15px;\n  }', '  /* Disabled responsive navbar styles */\n  .navbar-old-responsive-disabled{\n  }')

    # Let's add Poppins font globally in style.css
    if "font-family: 'Poppins'" not in style_content:
        # replace the font-family under *{ }
        style_content = re.sub(r'\*\s*\{([^}]+)font-family:[^;]+;', r'* {\1font-family: \'Poppins\', sans-serif;', style_content)
        style_content = re.sub(r'body\s*\{([^}]+)font-family:[^;]+;', r'body {\1font-family: \'Poppins\', sans-serif !important;', style_content)

    # Let's append premium style definitions for .about, .places, .hotels-section, .hotel-card, .place-card, .info-card, and mobile toggler override
    premium_css_append = """
/* =========================================================
   PREMIUM CUSTOM STYLING OVERRIDES (UNIFIED ACCROSS CITIES)
   ========================================================= */

body {
    font-family: 'Poppins', sans-serif !important;
    background: #f8f9fa;
}

/* Mobile responsive menu hamburger background override */
@media (max-width: 991.98px) {
    .navbar-collapse {
        background: rgba(0, 0, 0, 0.95) !important;
        padding: 20px;
        border-radius: 15px;
        margin-top: 15px;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
}

/* Premium card hover scales and overlays */
.place-card {
    border: none !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    background: white;
}
.place-card:hover {
    transform: translateY(-8px) !important;
    box-shadow: 0 15px 35px rgba(255, 152, 0, 0.12) !important;
}
.place-card img {
    border-top-left-radius: 20px !important;
    border-top-right-radius: 20px !important;
    transition: transform 0.5s ease !important;
}
.place-card:hover img {
    transform: scale(1.06) !important;
}

.hotel-card {
    border: none !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    background: #fdfdfd;
}
.hotel-card:hover {
    transform: translateY(-8px) !important;
    box-shadow: 0 15px 35px rgba(255, 152, 0, 0.15) !important;
}
.hotel-card img {
    border-top-left-radius: 20px !important;
    border-top-right-radius: 20px !important;
    transition: transform 0.5s ease !important;
}
.hotel-card:hover img {
    transform: scale(1.06) !important;
}

.hotel-content button {
    width: 100% !important;
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 16px !important;
    border: none !important;
    font-weight: 700 !important;
    background: linear-gradient(135deg, #ffcc00, #ff9800) !important;
    transition: all 0.3s ease !important;
    color: black !important;
}
.hotel-content button a {
    text-decoration: none !important;
    color: black !important;
    display: block !important;
}
.hotel-content button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 5px 15px rgba(255, 152, 0, 0.4) !important;
}

.info-card {
    background: #f8f9fa !important;
    border: 1px solid rgba(0,0,0,0.04) !important;
    border-radius: 16px !important;
    padding: 20px !important;
    transition: all 0.3s ease !important;
}
.info-card:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.05) !important;
    border-color: rgba(255, 204, 0, 0.3) !important;
}
.info-card i {
    color: #ff9800 !important;
    font-size: 32px !important;
    margin-bottom: 12px !important;
}

/* Alert icons positioning and design theme */
.alert-status-card {
    border-radius: 16px !important;
    background: white;
    transition: all 0.3s ease;
}
.alert-status-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.06) !important;
}
.alert-icon-box {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
}
"""
    style_content += premium_css_append
    
    with open(style_css_path, 'w', encoding='utf-8') as f:
        f.write(style_content)
    print("Injected premium selectors into style.css")

# ========================================================
# 4. REMOVE NAVBAR CONFLICTS IN about.css, contact us.css, homepage.css
# ========================================================
for c_file in ['about.css', 'contact us.css', 'homepage.css']:
    path = os.path.join(static_css_dir, c_file)
    if os.path.exists(path):
        backup_file(path)
        with open(path, 'r', encoding='utf-8') as f:
            css_content = f.read()
            
        # Rename navbar selectors
        css_content = css_content.replace('.navbar{', '/* Disabled conflict */\n.navbar-old-disabled{')
        css_content = css_content.replace('.navbar-brand{', '.navbar-brand-old-disabled{')
        css_content = css_content.replace('.nav-link{', '.nav-link-old-disabled{')
        css_content = css_content.replace('.nav-link:hover{', '.nav-link-hover-old-disabled{')
        css_content = css_content.replace('nav a,', '/* Disabled conflict */\nnav-a-disabled,')
        
        # In homepage.css set craft-card border radius to 18px
        if c_file == 'homepage.css':
            css_content = css_content.replace('border-radius:0;', 'border-radius:18px;')
            css_content = css_content.replace('background:pink;', 'background:#fff9f2;')
            # Let's verify we also add hover transition
            if '.craft-card:hover' not in css_content:
                css_content += "\n.craft-card:hover { transform: translateY(-8px); box-shadow: 0 15px 30px rgba(255,152,0,0.15) !important; }\n"
                
        with open(path, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"Disabled old navbar styles in {c_file}")

print("\nTask Complete!")
