import os
import re

templates_dir = r'templates'

unified_nav = """<!-- =========================
     NAVBAR
========================= -->
<nav class="navbar navbar-expand-lg navbar-dark fixed-top"
     style="background: rgba(0, 0, 0, 0.85) !important; backdrop-filter: blur(12px); border-bottom: 1px solid rgba(255, 255, 255, 0.15); padding: 15px 0; z-index: 2000; width: 100%;">

    <div class="container">

        <a class="navbar-brand fw-bold text-warning fs-2"
           href="{% url 'home' %}"
           style="letter-spacing: 1px; color: #ffcc00 !important; font-size: 28px !important; text-decoration: none;">
            Amazing India
        </a>

        <button class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse justify-content-end"
             id="navbarNav">

            <ul class="navbar-nav align-items-center gap-3">

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'home' %}" style="color: rgba(255, 255, 255, 0.75) !important; font-size: 16px; font-weight: 500; text-decoration: none; transition: 0.3s;" onmouseover="this.style.color='#ffcc00'" onmouseout="this.style.color='rgba(255, 255, 255, 0.75)'">
                        Home
                    </a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'about' %}" style="color: rgba(255, 255, 255, 0.75) !important; font-size: 16px; font-weight: 500; text-decoration: none; transition: 0.3s;" onmouseover="this.style.color='#ffcc00'" onmouseout="this.style.color='rgba(255, 255, 255, 0.75)'">
                        About
                    </a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'destination' %}" style="color: rgba(255, 255, 255, 0.75) !important; font-size: 16px; font-weight: 500; text-decoration: none; transition: 0.3s;" onmouseover="this.style.color='#ffcc00'" onmouseout="this.style.color='rgba(255, 255, 255, 0.75)'">
                        Destination
                    </a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'ai_planner' %}" style="color: rgba(255, 255, 255, 0.75) !important; font-size: 16px; font-weight: 500; text-decoration: none; transition: 0.3s;" onmouseover="this.style.color='#ffcc00'" onmouseout="this.style.color='rgba(255, 255, 255, 0.75)'">
                        AI Planner
                    </a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'contact' %}" style="color: rgba(255, 255, 255, 0.75) !important; font-size: 16px; font-weight: 500; text-decoration: none; transition: 0.3s;" onmouseover="this.style.color='#ffcc00'" onmouseout="this.style.color='rgba(255, 255, 255, 0.75)'">
                        Contact
                    </a>
                </li>

                {% if user.is_authenticated %}

                <li class="nav-item">
                    <span class="text-white small" style="color: white !important; font-weight: 500;">
                        Hi, {{ user.username }}
                    </span>
                </li>

                <li class="nav-item">
                    <a href="{% url 'logout' %}"
                       class="btn btn-warning rounded-pill px-3"
                       style="color: black !important; background-color: #ffcc00 !important; border: none; font-weight: bold; font-size: 14px; text-decoration: none;">
                        Logout
                    </a>
                </li>

                {% else %}

                <li class="nav-item">
                    <a href="{% url 'login' %}"
                       class="btn btn-warning rounded-pill px-3"
                       style="color: black !important; background-color: #ffcc00 !important; border: none; font-weight: bold; font-size: 14px; text-decoration: none;">
                        Login
                    </a>
                </li>

                <li class="nav-item">
                    <a href="{% url 'signup' %}"
                       class="btn btn-outline-light rounded-pill px-3"
                       style="color: white !important; border: 1px solid white !important; font-weight: bold; font-size: 14px; text-decoration: none;">
                        Sign Up
                    </a>
                </li>

                {% endif %}

            </ul>

        </div>

    </div>

</nav>"""

for file in os.listdir(templates_dir):
    if file.endswith('.html') and file not in ['login.html', 'signup.html']:
        path = os.path.join(templates_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Replace Navbar
        new_content = re.sub(r'<nav.*?>.*?</nav>', unified_nav, content, flags=re.DOTALL)
        
        # 2. Add padding style to body if not homepage
        if file != 'homepage.html':
            padding_style = "\n        body {\n            padding-top: 85px !important;\n        }\n"
            # Find style block
            if '<style>' in new_content:
                # Insert padding style right after <style>
                new_content = new_content.replace('<style>', '<style>' + padding_style, 1)
            else:
                # Create style block right before </head>
                style_block = f"    <style>{padding_style}    </style>\n</head>"
                new_content = new_content.replace('</head>', style_block, 1)
                
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Standardized navbar for {file}")
