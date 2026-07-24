import base64
import os

def get_base64_image(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Required image {filename} not found.")
    with open(filename, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode('utf-8')

def main():
    print("Initializing directories...")
    # Create all target folders
    os.makedirs("halloween", exist_ok=True)
    os.makedirs("halloween/dividers", exist_ok=True)
    os.makedirs("halloween/buttons", exist_ok=True)
    os.makedirs("halloween/icons", exist_ok=True)
    os.makedirs("halloween/animations", exist_ok=True)

    print("Loading image assets...")
    try:
        char_b64 = get_base64_image("character_600.png")
        avatar_b64 = get_base64_image("avatar.png")
        print("Images loaded and encoded successfully.")
    except Exception as e:
        print(f"Error loading images: {e}")
        return

    # Details
    name = "Charan BS"
    username = "CharanBS18"
    email = "charan201204@gmail.com"
    role = "Full-Stack Developer"
    tagline = "Stay Sharp. Keep Building."
    quote = "Architecting digital worlds with cybernetic precision."
    skills_list = ["React", "Next.js", "TypeScript", "Node.js", "Python", "Docker", "TailwindCSS"]
    skills_html = " ".join([f"<code>{s}</code>" for s in skills_list])

    # ==================== 1. halloween/banner.svg ====================
    print("Generating halloween/banner.svg...")
    banner_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="1280" height="740">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="sky-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f0726" />
      <stop offset="60%" stop-color="#1c0a35" />
      <stop offset="100%" stop-color="#240046" />
    </linearGradient>
    
    <!-- Moon Glow Filter -->
    <filter id="moon-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="15" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Warm Pumpkin Glow -->
    <radialGradient id="lamp-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff7518" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#e85d04" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>

    <!-- Keyboard Backlight Gradient -->
    <linearGradient id="rgb-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ea580c" />
      <stop offset="50%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#ea580c" />
    </linearGradient>

    <clipPath id="hologram-clip">
      <rect x="780" y="100" width="450" height="0">
        <animate attributeName="height" from="0" to="620" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      </rect>
    </clipPath>

    <clipPath id="terminal-type">
      <rect x="0" y="100" width="0" height="40">
        <animate attributeName="width" from="0" to="400" dur="1.2s" begin="0.8s" fill="freeze"/>
      </rect>
    </clipPath>
  </defs>

  <style>
    <![CDATA[
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&amp;family=Outfit:wght@400;600&amp;display=swap');
    
    .name-text {{
      font-family: 'Syne', sans-serif;
      font-weight: 800;
      font-size: 46px;
      letter-spacing: 2px;
      fill: #ff7518;
    }}

    .sub-text {{
      font-family: 'Outfit', sans-serif;
      font-size: 16px;
      fill: #f8f9fa;
      opacity: 0.8;
    }}

    @keyframes blink {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}
    .cursor {{
      animation: blink 0.8s infinite;
      fill: #ff7518;
    }}

    @keyframes float {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-10px); }}
    }}
    .ghost-floater {{
      animation: float 4s ease-in-out infinite;
    }}

    @keyframes flicker {{
      0%, 100% {{ opacity: 0.95; }}
      50% {{ opacity: 0.8; }}
    }}
    .light-flicker {{
      animation: flicker 0.2s infinite;
    }}
    ]]>
  </style>

  <!-- Sky background inside window -->
  <rect width="1280" height="740" rx="20" fill="url(#sky-grad)"/>

  <!-- Stars -->
  <g fill="#f8f9fa" opacity="0.5">
    <circle cx="150" cy="80" r="1.5"/>
    <circle cx="280" cy="120" r="1"/>
    <circle cx="450" cy="70" r="2"/>
    <circle cx="600" cy="100" r="1"/>
    <circle cx="720" cy="60" r="1.5"/>
    <circle cx="1100" cy="90" r="1"/>
  </g>

  <!-- Large Full Moon -->
  <circle cx="150" cy="150" r="90" fill="#ffd166" filter="url(#moon-glow)" opacity="0.85"/>
  <!-- Moon details -->
  <circle cx="120" cy="120" r="15" fill="#fbc43d" opacity="0.3"/>
  <circle cx="180" cy="170" r="20" fill="#fbc43d" opacity="0.3"/>
  <circle cx="130" cy="180" r="10" fill="#fbc43d" opacity="0.3"/>

  <!-- Spooky twisted branches in front of moon -->
  <path d="M 0 300 C 50 250, 100 240, 120 180 C 122 170, 100 160, 95 150 M 120 180 C 150 170, 180 130, 200 150 C 220 170, 250 160, 260 140" fill="none" stroke="#0d1117" stroke-width="6" stroke-linecap="round"/>
  <path d="M 0 300 C 30 290, 80 320, 110 300 C 130 280, 150 290, 160 270" fill="none" stroke="#0d1117" stroke-width="4" stroke-linecap="round"/>

  <!-- Clouds -->
  <path d="M -50 220 C 50 180, 150 200, 250 220 C 350 240, 450 210, 550 230 L 1280 230 L 1280 740 L -50 740 Z" fill="#1c1c1c" opacity="0.4"/>
  <path d="M 700 120 C 800 100, 900 130, 1000 110 C 1100 90, 1200 110, 1300 100 L 1300 740 L 700 740 Z" fill="#0d1117" opacity="0.35"/>

  <!-- Flying bats silhouettes -->
  <path d="M 280 180 Q 290 170, 295 178 Q 300 170, 310 180 Q 295 185, 280 180 Z" fill="#0d1117" class="ghost-floater"/>
  <path d="M 330 150 Q 338 142, 342 148 Q 346 142, 354 150 Q 342 154, 330 150 Z" fill="#0d1117" class="ghost-floater" style="animation-delay: 1.5s;"/>

  <!-- Ambient lamp glow behind desk elements -->
  <circle cx="1080" cy="380" r="320" fill="url(#lamp-glow)" class="light-flicker"/>

  <!-- LEFT PANEL: Spooky Terminal Window (x=50, y=80, width=700, height=580) -->
  <g transform="translate(50, 80)">
    <rect width="700" height="580" rx="16" fill="#0d1117" stroke="#5a189a" stroke-width="2" style="filter: drop-shadow(0 10px 30px rgba(0, 0, 0, 0.65));"/>
    
    <!-- Window Header -->
    <path d="M 0 45 H 700" stroke="#1c1c1c" stroke-width="1.5"/>
    <circle cx="20" cy="22" r="7" fill="#ff5f56"/>
    <circle cx="42" cy="22" r="7" fill="#ffbd2e"/>
    <circle cx="64" cy="22" r="7" fill="#27c93f"/>
    <text x="350" y="28" fill="#ff7518" font-family="monospace" font-size="14" font-weight="bold" letter-spacing="1" text-anchor="middle">SPOOKY_TERMINAL // Bio.sh</text>

    <!-- Terminal Text -->
    <g transform="translate(40, 80)">
      <!-- Line 1 -->
      <g clip-path="url(#terminal-type)">
        <text x="0" y="25" fill="#f8f9fa" font-family="monospace" font-size="18" font-weight="bold">
          <tspan fill="#5a189a">user@hallow-box</tspan>:<tspan fill="#ff7518">~$</tspan> cat dev_profile.txt
        </text>
      </g>
      <!-- Blinking Cursor -->
      <rect x="0" y="8" width="10" height="20" class="cursor">
        <animate attributeName="x" from="0" to="370" dur="1.2s" begin="0.8s" fill="freeze"/>
        <animate attributeName="visibility" values="visible;hidden" keyTimes="0;0.99" dur="2s" fill="freeze"/>
      </rect>

      <!-- Profile Header -->
      <text class="name-text" x="0" y="90" opacity="0">
        CHARAN BS
        <animate attributeName="opacity" from="0" to="1" dur="0.8s" begin="1.8s" fill="freeze" />
      </text>

      <!-- Roles -->
      <g transform="translate(0, 130)">
        <text x="0" y="0" fill="#f8f9fa" font-family="monospace" font-size="20">> ROLE: </text>
        <g>
          <text x="90" y="0" fill="#ff7518" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
            Full-Stack Developer
            <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.05;0.22;0.25;1" dur="12s" repeatCount="indefinite" />
          </text>
          <text x="90" y="0" fill="#7fff00" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
            Spooky Script Wizard
            <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.25;0.30;0.47;0.50;1" dur="12s" repeatCount="indefinite" />
          </text>
          <text x="90" y="0" fill="#5a189a" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
            UI/UX Alchemist
            <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.50;0.55;0.72;0.75;1" dur="12s" repeatCount="indefinite" />
          </text>
        </g>
      </g>

      <!-- Quote Box with Twisting Vine Frame -->
      <g transform="translate(0, 170)">
        <rect width="620" height="90" rx="8" fill="#1c1c1c" stroke="#5a189a" stroke-width="1.5"/>
        <path d="M 0 15 V 0 H 15 M 605 0 H 620 V 15 M 620 75 V 90 H 605 M 15 90 H 0 V 75" stroke="#ff7518" stroke-width="3" fill="none"/>
        <text x="30" y="50" fill="#ffd166" font-family="monospace" font-size="14" font-style="italic">
          "{quote}"
        </text>
      </g>

      <!-- Skills Details -->
      <g transform="translate(0, 290)">
        <text x="0" y="20" fill="#f8f9fa" font-family="monospace" font-size="16" font-weight="bold">> CORE_OBJECTIVES:</text>
        <text x="20" y="50" fill="#f8f9fa" font-family="monospace" font-size="15" opacity="0">
          - Crafting responsive frontend architectures
          <animate attributeName="opacity" from="0" to="0.9" dur="0.5s" begin="4.2s" fill="freeze"/>
        </text>
        <text x="20" y="80" fill="#f8f9fa" font-family="monospace" font-size="15" opacity="0">
          - Secure backends &amp; microservice frameworks
          <animate attributeName="opacity" from="0" to="0.9" dur="0.5s" begin="4.8s" fill="freeze"/>
        </text>
        <text x="20" y="110" fill="#f8f9fa" font-family="monospace" font-size="15" opacity="0">
          - Handcrafted premium designs &amp; user experiences
          <animate attributeName="opacity" from="0" to="0.9" dur="0.5s" begin="5.4s" fill="freeze"/>
        </text>
      </g>
      
      <!-- Tech Pills (Halloween Colors) -->
      <g transform="translate(0, 430)">
        <text x="0" y="15" fill="#ea580c" font-family="monospace" font-size="15" font-weight="bold">> WEAPONS_OF_CHOICE:</text>
        
        <g transform="translate(20, 30)">
          <!-- React -->
          <rect width="70" height="26" rx="13" fill="#240046" stroke="#8b5cf6" stroke-width="1.5"/>
          <text x="35" y="17" fill="#f8f9fa" font-family="monospace" font-size="11" text-anchor="middle">React</text>
          
          <!-- Node -->
          <g transform="translate(80, 0)">
            <rect width="75" height="26" rx="13" fill="#240046" stroke="#7fff00" stroke-width="1.5"/>
            <text x="37.5" y="17" fill="#7fff00" font-family="monospace" font-size="11" text-anchor="middle">Node.js</text>
          </g>

          <!-- Python -->
          <g transform="translate(165, 0)">
            <rect width="80" height="26" rx="13" fill="#240046" stroke="#ff7518" stroke-width="1.5"/>
            <text x="40" y="17" fill="#ff7518" font-family="monospace" font-size="11" text-anchor="middle">Python</text>
          </g>

          <!-- Tailwind -->
          <g transform="translate(255, 0)">
            <rect width="90" height="26" rx="13" fill="#240046" stroke="#8b5cf6" stroke-width="1.5"/>
            <text x="45" y="17" fill="#f8f9fa" font-family="monospace" font-size="11" text-anchor="middle">Tailwind</text>
          </g>
        </g>
      </g>
    </g>
  </g>

  <!-- RIGHT PANEL: Character & Spooky desk setup -->
  <g transform="translate(780, 80)">
    <!-- Desktop monitors backing -->
    <rect x="0" y="0" width="450" height="250" rx="12" fill="#1c1c1c" stroke="#5a189a" stroke-width="1.5"/>
    <path d="M 0 35 H 450" stroke="#0d1117" stroke-width="1.5"/>
    
    <!-- Spooky Code Card -->
    <g transform="translate(20, 50)" font-family="monospace" font-size="12" font-weight="bold">
      <text x="0" y="20" fill="#7fff00">const <tspan fill="#ff7518">hallowCode</tspan> = () => {{</text>
      <text x="20" y="45" fill="#f8f9fa">deployPotion(<tspan fill="#5a189a">"cauldron"</tspan>);</text>
      <text x="20" y="70" fill="#f8f9fa">ignite(<tspan fill="#ea580c">"jack-o-lantern"</tspan>);</text>
      <text x="20" y="95" fill="#7fff00">return <tspan fill="#ffd166">"magic_sparks"</tspan>;</text>
      <text x="0" y="120" fill="#f8f9fa">}};</text>
    </g>

    <!-- Pumpkin Lamp on Desk -->
    <g transform="translate(320, 75)">
      <!-- Lamp base -->
      <path d="M 50 80 L 35 150 H 65 Z" fill="#0d1117" stroke="#ea580c" stroke-width="1"/>
      <!-- Pumpkin carving lamp -->
      <circle cx="50" cy="70" r="30" fill="#ff7518" style="filter: drop-shadow(0 0 8px #ff7518);"/>
      <path d="M 40 65 L 45 70 L 38 72 Z" fill="#240046"/>
      <path d="M 60 65 L 55 70 L 62 72 Z" fill="#240046"/>
      <path d="M 42 80 Q 50 88, 58 80 Q 50 83, 42 80 Z" fill="#240046"/>
      <path d="M 48 40 L 52 40 L 50 32 Z" fill="#0d1117"/>
    </g>

    <!-- Programmer Desk Surface -->
    <rect x="-20" y="580" width="490" height="20" rx="4" fill="#0d1117"/>

    <!-- Keyboard with Backlight -->
    <g transform="translate(100, 560)">
      <rect width="250" height="20" rx="3" fill="#1c1c1c" stroke="url(#rgb-grad)" stroke-width="2" style="filter: drop-shadow(0 0 10px #ff7518);"/>
      <path d="M 20 5 H 230" stroke="#f8f9fa" stroke-dasharray="8 4" stroke-width="2" opacity="0.8"/>
      <path d="M 15 15 H 235" stroke="#f8f9fa" stroke-dasharray="12 6" stroke-width="2" opacity="0.8"/>
    </g>

    <!-- Coffee Mug with Ghost Steam -->
    <g transform="translate(30, 520)" class="ghost-floater">
      <rect x="10" y="30" width="30" height="30" rx="6" fill="#5a189a" stroke="#f8f9fa" stroke-width="1.5"/>
      <path d="M 40 38 C 45 38, 48 42, 48 45 C 48 48, 45 52, 40 52" fill="none" stroke="#f8f9fa" stroke-width="2"/>
      <!-- Ghost Steam -->
      <path d="M 20 20 Q 25 10, 20 2 Q 30 10, 25 25 Z" fill="#f8f9fa" opacity="0.6"/>
    </g>

    <!-- Vector Character Hologram Reveal -->
    <g clip-path="url(#hologram-clip)">
      <image href="data:image/png;base64,{{char_b64}}" x="13" y="100" width="424" height="600" />
      <rect x="0" y="100" width="450" height="480" fill="url(#grid)" opacity="0.2" pointer-events="none" />
    </g>

    <!-- Green Scanline reveal -->
    <line x1="10" y1="100" x2="440" y2="100" stroke="#7fff00" stroke-width="3" opacity="0" style="filter: drop-shadow(0 0 5px #7fff00);">
      <animate attributeName="y1" from="100" to="580" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      <animate attributeName="y2" from="100" to="580" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.9;1" dur="2s" begin="0.5s" fill="freeze" />
    </line>
  </g>
</svg>"""

    with open("halloween/banner.svg", "w") as f:
      f.write(banner_content.replace("{{char_b64}}", char_b64))
    print("halloween/banner.svg generated.")

    # ==================== 2. halloween/dividers/ ====================
    print("Generating dividers...")
    # A. Twisting Pumpkin Vines Divider
    vines_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" width="100%" height="60">
  <path d="M 0 30 C 150 10, 250 50, 400 30 C 550 10, 650 50, 800 30 C 950 10, 1050 50, 1200 30" fill="none" stroke="#e85d04" stroke-width="4" stroke-linecap="round"/>
  <!-- Twigs and Tendrils -->
  <path d="M 100 24 Q 120 10, 110 5" fill="none" stroke="#5a189a" stroke-width="1.5"/>
  <path d="M 500 35 Q 510 50, 530 45" fill="none" stroke="#5a189a" stroke-width="1.5"/>
  <!-- Pumpkin Leaves -->
  <path d="M 280 23 Q 295 10, 310 25 Z" fill="#240046" stroke="#ff7518" stroke-width="1"/>
  <path d="M 680 37 Q 695 50, 710 35 Z" fill="#240046" stroke="#ff7518" stroke-width="1"/>
  <!-- Mini Pumpkins -->
  <g transform="translate(400, 20)">
    <ellipse cx="0" cy="5" rx="12" ry="9" fill="#ff7518"/>
    <ellipse cx="0" cy="5" rx="6" ry="9" fill="#e85d04"/>
    <path d="M 0 -4 L 2 -9" stroke="#7fff00" stroke-width="2" fill="none"/>
  </g>
  <g transform="translate(800, 20)">
    <ellipse cx="0" cy="5" rx="12" ry="9" fill="#ff7518"/>
    <ellipse cx="0" cy="5" rx="6" ry="9" fill="#e85d04"/>
    <path d="M 0 -4 L 2 -9" stroke="#7fff00" stroke-width="2" fill="none"/>
  </g>
</svg>"""
    with open("halloween/dividers/vines.svg", "w") as f:
      f.write(vines_content)

    # B. Spooky bats wave divider
    bats_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" width="100%" height="60" fill="#0d1117">
  <!-- Small line behind bats -->
  <line x1="0" y1="30" x2="1200" y2="30" stroke="#240046" stroke-width="2" stroke-dasharray="10 15"/>
  
  <!-- Bat silhouettes -->
  <!-- Bat 1 -->
  <path d="M 150 25 Q 165 10, 175 22 Q 185 10, 200 25 Q 175 35, 150 25" fill="#ff7518"/>
  <!-- Bat 2 -->
  <path d="M 580 20 Q 595 5, 605 17 Q 615 5, 630 20 Q 605 30, 580 20" fill="#0d1117" stroke="#5a189a" stroke-width="1.5"/>
  <!-- Bat 3 -->
  <path d="M 980 28 Q 995 13, 1005 25 Q 1015 13, 1030 28 Q 1005 38, 980 28" fill="#e85d04"/>
</svg>"""
    with open("halloween/dividers/bats.svg", "w") as f:
      f.write(bats_content)

    # C. Floating Ghost Divider
    ghosts_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" width="100%" height="60" fill="none">
  <path d="M 0 35 Q 150 15, 300 35 Q 450 55, 600 35 Q 750 15, 900 35 Q 1050 55, 1200 35" stroke="#5a189a" stroke-width="2" stroke-dasharray="8 8"/>
  <!-- Tiny Ghosts floating along the line -->
  <g transform="translate(200, 20)">
    <path d="M -10 10 C -10 -5, 10 -5, 10 10 C 10 15, 5 13, 0 15 C -5 13, -10 15, -10 10 Z" fill="#f8f9fa" stroke="#ff7518" stroke-width="1"/>
    <circle cx="-3" cy="5" r="1.2" fill="#000"/>
    <circle cx="3" cy="5" r="1.2" fill="#000"/>
  </g>
  <g transform="translate(600, 20)">
    <path d="M -10 10 C -10 -5, 10 -5, 10 10 C 10 15, 5 13, 0 15 C -5 13, -10 15, -10 10 Z" fill="#f8f9fa" stroke="#5a189a" stroke-width="1"/>
    <circle cx="-3" cy="5" r="1.2" fill="#000"/>
    <circle cx="3" cy="5" r="1.2" fill="#000"/>
  </g>
  <g transform="translate(1000, 20)">
    <path d="M -10 10 C -10 -5, 10 -5, 10 10 C 10 15, 5 13, 0 15 C -5 13, -10 15, -10 10 Z" fill="#f8f9fa" stroke="#ff7518" stroke-width="1"/>
    <circle cx="-3" cy="5" r="1.2" fill="#000"/>
    <circle cx="3" cy="5" r="1.2" fill="#000"/>
  </g>
</svg>"""
    with open("halloween/dividers/ghosts.svg", "w") as f:
      f.write(ghosts_content)
    print("Dividers generated.")

    # ==================== 3. halloween/buttons/ ====================
    print("Generating buttons...")
    button_titles = ["ABOUT_ME", "CORE_SKILLS", "MY_PROJECTS", "CONNECT_PORTAL"]
    button_filenames = ["about.svg", "skills.svg", "projects.svg", "contact.svg"]
    button_colors = ["#ff7518", "#7fff00", "#8b5cf6", "#ffd166"]
    
    for title, filename, col in zip(button_titles, button_filenames, button_colors):
      btn_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 50" width="200" height="50">
  <defs>
    <filter id="btn-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <!-- Wooden Signpost / Tombstone Look -->
  <rect x="5" y="5" width="190" height="40" rx="6" fill="#1c1c1c" stroke="{col}" stroke-width="2" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4));"/>
  <!-- Spooky Bracket Border Accents -->
  <path d="M 12 12 V 8 H 25 M 188 12 V 8 H 175 M 188 38 V 42 H 175 M 12 38 V 42 H 25" stroke="{col}" stroke-width="2" fill="none"/>
  
  <text x="100" y="29" fill="{col}" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1.5" text-anchor="middle" filter="url(#btn-glow)">{title}</text>
  
  <!-- Tiny bat decoration -->
  <path d="M 25 15 Q 30 10, 33 13 Q 36 10, 41 15 Q 33 18, 25 15 Z" fill="{col}" opacity="0.8"/>
</svg>"""
      with open(f"halloween/buttons/{filename}", "w") as f:
        f.write(btn_svg)
    print("Buttons generated.")

    # ==================== 4. halloween/icons/ ====================
    print("Generating Halloween-styled Coding Icons...")
    # HTML: Tombstone Style
    html_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <path d="M 15 70 C 15 25, 65 25, 65 70 Z" fill="#1c1c1c" stroke="#e85d04" stroke-width="3"/>
  <path d="M 25 40 L 35 48 L 25 56 M 55 40 L 45 48 L 55 56" stroke="#ff7518" stroke-width="3" fill="none" stroke-linecap="round"/>
  <text x="40" y="65" fill="#f8f9fa" font-family="monospace" font-size="10" text-anchor="middle">HTML</text>
  <!-- Cobweb in corner -->
  <path d="M 18 55 Q 28 58, 30 70 M 18 62 Q 24 64, 25 70" stroke="#ea580c" stroke-width="1" fill="none"/>
</svg>"""
    with open("halloween/icons/html.svg", "w") as f:
      f.write(html_icon)

    # CSS: Tombstone Style
    css_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <path d="M 15 70 C 15 25, 65 25, 65 70 Z" fill="#1c1c1c" stroke="#8b5cf6" stroke-width="3"/>
  <text x="40" y="48" fill="#8b5cf6" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">{ }</text>
  <text x="40" y="65" fill="#f8f9fa" font-family="monospace" font-size="10" text-anchor="middle">CSS</text>
</svg>"""
    with open("halloween/icons/css.svg", "w") as f:
      f.write(css_icon)

    # JS: Wizard Spell-book
    js_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <!-- Book Cover -->
  <rect x="20" y="15" width="44" height="52" rx="4" fill="#5a189a" stroke="#ffd166" stroke-width="2"/>
  <rect x="15" y="15" width="6" height="52" fill="#240046"/>
  <!-- Gold JS Symbol on book -->
  <rect x="35" y="32" width="20" height="20" fill="#ffd166"/>
  <text x="45" y="47" fill="#240046" font-family="sans-serif" font-weight="bold" font-size="14" text-anchor="middle">JS</text>
  <line x1="18" y1="25" x2="18" y2="55" stroke="#ffd166" stroke-width="2"/>
</svg>"""
    with open("halloween/icons/js.svg", "w") as f:
      f.write(js_icon)

    # Python: Skull with Slithered Snake
    python_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <!-- Cartoon Skull -->
  <rect x="25" y="25" width="30" height="26" rx="10" fill="#f8f9fa" stroke="#1c1c1c" stroke-width="2"/>
  <rect x="30" y="48" width="20" height="12" fill="#f8f9fa" stroke="#1c1c1c" stroke-width="2"/>
  <circle cx="33" cy="38" r="4.5" fill="#000"/>
  <circle cx="47" cy="38" r="4.5" fill="#000"/>
  <line x1="37" y1="54" x2="37" y2="60" stroke="#1c1c1c" stroke-width="2"/>
  <line x1="43" y1="54" x2="43" y2="60" stroke="#1c1c1c" stroke-width="2"/>
  <!-- Green Python coiled around it -->
  <path d="M 15 50 Q 25 35, 40 40 Q 55 45, 60 30 Q 62 20, 52 15" fill="none" stroke="#7fff00" stroke-width="5" stroke-linecap="round"/>
  <!-- Snake Eye -->
  <circle cx="54" cy="17" r="1" fill="#fff"/>
</svg>"""
    with open("halloween/icons/python.svg", "w") as f:
      f.write(python_icon)

    # React: Spider-Web Atomic structure
    react_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <!-- React orbits transformed into spider web lines -->
  <ellipse cx="40" cy="40" rx="35" ry="12" fill="none" stroke="#8b5cf6" stroke-width="1.5" transform="rotate(30 40 40)"/>
  <ellipse cx="40" cy="40" rx="35" ry="12" fill="none" stroke="#8b5cf6" stroke-width="1.5" transform="rotate(90 40 40)"/>
  <ellipse cx="40" cy="40" rx="35" ry="12" fill="none" stroke="#8b5cf6" stroke-width="1.5" transform="rotate(150 40 40)"/>
  
  <!-- Spiders web lines connecting orbits -->
  <path d="M 40 28 Q 48 35, 40 52 M 40 28 Q 32 35, 40 52" stroke="#8b5cf6" stroke-width="1" stroke-dasharray="2 2" fill="none"/>
  
  <!-- Spider at center -->
  <circle cx="40" cy="40" r="4.5" fill="#e85d04"/>
  <path d="M 40 40 L 46 36 M 40 40 L 46 44 M 40 40 L 34 36 M 40 40 L 34 44" stroke="#e85d04" stroke-width="1.5"/>
</svg>"""
    with open("halloween/icons/react.svg", "w") as f:
      f.write(react_icon)

    # Node: Cauldron bubbling with green potion
    node_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <!-- Cauldron Body -->
  <path d="M 20 40 C 20 62, 60 62, 60 40 C 60 30, 20 30, 20 40 Z" fill="#1c1c1c" stroke="#5a189a" stroke-width="2"/>
  <ellipse cx="40" cy="32" rx="18" ry="4" fill="#240046" stroke="#5a189a" stroke-width="2"/>
  
  <!-- Bubbling green steam -->
  <circle cx="32" cy="22" r="4" fill="#7fff00"/>
  <circle cx="48" cy="20" r="6" fill="#7fff00"/>
  <circle cx="40" cy="25" r="5" fill="#7fff00"/>
  
  <text x="40" y="52" fill="#7fff00" font-family="monospace" font-weight="bold" font-size="9" text-anchor="middle">NODE</text>
</svg>"""
    with open("halloween/icons/node.svg", "w") as f:
      f.write(node_icon)

    # Docker: Ghost Cargo
    docker_icon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <!-- Ghost Whale Body -->
  <path d="M 10 45 C 10 25, 45 25, 55 35 C 65 35, 75 40, 70 50 C 65 52, 45 50, 10 45 Z" fill="#f8f9fa" stroke="#5a189a" stroke-width="2"/>
  <path d="M 68 46 L 75 42 L 72 50 Z" fill="#f8f9fa" stroke="#5a189a" stroke-width="1.5"/>
  <circle cx="22" cy="38" r="2.5" fill="#000"/>
  
  <!-- Glowing shipping crates (represented as pumpkins!) -->
  <g transform="translate(32, 18)">
    <rect width="10" height="10" fill="#ff7518" stroke="#000" stroke-width="1"/>
    <rect x="12" y="0" width="10" height="10" fill="#e85d04" stroke="#000" stroke-width="1"/>
  </g>
</svg>"""
    with open("halloween/icons/docker.svg", "w") as f:
      f.write(docker_icon)
    print("Icons generated.")

    # ==================== 5. halloween/animations/ ====================
    print("Generating animations...")
    
    # A. Typing Ghost with laptop
    typing_ghost = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 220" width="220" height="220">
  <defs>
    <filter id="ghost-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <style>
    @keyframes floatGhost {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-8px); }
    }
    @keyframes typeHands {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-4px); }
    }
    @keyframes keyboardGlow {
      0%, 100% { fill: #ff7518; }
      50% { fill: #a855f7; }
    }
    .ghost-body { animation: floatGhost 3.5s ease-in-out infinite; }
    .ghost-hands { animation: typeHands 0.15s ease-in-out infinite; }
    .key-glow { animation: keyboardGlow 0.4s infinite; }
  </style>

  <!-- Animated Ghost -->
  <g class="ghost-body" filter="url(#ghost-glow)">
    <!-- Main Body -->
    <path d="M 60 120 C 60 50, 140 50, 140 120 C 140 160, 125 150, 100 165 C 75 150, 60 160, 60 120 Z" fill="#f8f9fa" stroke="#5a189a" stroke-width="2"/>
    
    <!-- Glasses -->
    <circle cx="88" cy="100" r="10" fill="none" stroke="#ff7518" stroke-width="2"/>
    <circle cx="112" cy="100" r="10" fill="none" stroke="#ff7518" stroke-width="2"/>
    <line x1="98" y1="100" x2="102" y2="100" stroke="#ff7518" stroke-width="2"/>
    <!-- Eyes inside glasses -->
    <circle cx="88" cy="100" r="2.5" fill="#000"/>
    <circle cx="112" cy="100" r="2.5" fill="#000"/>

    <!-- Cheeks -->
    <circle cx="76" cy="110" r="3" fill="#ff7518" opacity="0.5"/>
    <circle cx="124" cy="110" r="3" fill="#ff7518" opacity="0.5"/>

    <!-- Typing Hands -->
    <g class="ghost-hands">
      <ellipse cx="80" cy="132" rx="6" ry="4" fill="#f8f9fa" stroke="#5a189a" stroke-width="1.5"/>
      <ellipse cx="120" cy="132" rx="6" ry="4" fill="#f8f9fa" stroke="#5a189a" stroke-width="1.5"/>
    </g>
  </g>

  <!-- Laptop (Stationary) -->
  <g transform="translate(50, 135)">
    <!-- Base -->
    <path d="M 10 40 L 110 40 L 120 50 L 0 50 Z" fill="#1c1c1c" stroke="#ff7518" stroke-width="2"/>
    <!-- Keys with flashing light -->
    <rect class="key-glow" x="20" y="42" width="80" height="4" rx="1"/>
    
    <!-- Lid/Screen -->
    <path d="M 20 40 L 15 5 L 105 5 L 100 40 Z" fill="#0d1117" stroke="#ff7518" stroke-width="2"/>
    <rect x="22" y="8" width="76" height="28" fill="#240046"/>
    <!-- Code lines on screen -->
    <line x1="30" y1="15" x2="70" y2="15" stroke="#7fff00" stroke-width="2"/>
    <line x1="30" y1="23" x2="80" y2="23" stroke="#ff7518" stroke-width="2"/>
    <line x1="30" y1="31" x2="55" y2="31" stroke="#f8f9fa" stroke-width="2"/>
  </g>
</svg>"""
    with open("halloween/animations/typing_ghost.svg", "w") as f:
      f.write(typing_ghost)

    # B. Blinking scary Jack-o'-lantern
    blinking_jack = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <style>
    @keyframes eyeBlink {
      0%, 90%, 100% { fill: #ffd166; }
      95% { fill: #1c1c1c; }
    }
    @keyframes glowPulse {
      0%, 100% { filter: drop-shadow(0 0 4px #ff7518); }
      50% { filter: drop-shadow(0 0 12px #ff7518); }
    }
    .glowing-eyes { animation: eyeBlink 3.8s infinite; }
    .pumpkin-glow { animation: glowPulse 2s ease-in-out infinite; }
  </style>

  <!-- Stem -->
  <path d="M 80 40 C 78 30, 72 25, 70 25 C 68 25, 72 32, 75 40 Z" fill="#240046" stroke="#ea580c" stroke-width="2"/>

  <!-- Pumpkin Body -->
  <g class="pumpkin-glow">
    <!-- Asymmetric organic round ribs -->
    <ellipse cx="80" cy="95" rx="55" fill="#ff7518" stroke="#1c1c1c" stroke-width="3"/>
    <ellipse cx="80" cy="95" rx="35" fill="#e85d04" stroke="#1c1c1c" stroke-width="2"/>
    <ellipse cx="80" cy="95" rx="16" fill="#d04e00" stroke="#1c1c1c" stroke-width="1.5"/>

    <!-- Carved Eyes (flashing/blinking) -->
    <!-- Left Eye -->
    <path class="glowing-eyes" d="M 52 80 L 68 76 L 62 90 Z" stroke="#1c1c1c" stroke-width="1.5"/>
    <!-- Right Eye -->
    <path class="glowing-eyes" d="M 108 80 L 92 76 L 98 90 Z" stroke="#1c1c1c" stroke-width="1.5"/>

    <!-- Carved Mouth -->
    <path class="glowing-eyes" d="M 45 105 Q 80 135, 115 105 Q 98 115, 80 110 Q 62 115, 45 105 Z" stroke="#1c1c1c" stroke-width="1.5"/>
  </g>
</svg>"""
    with open("halloween/animations/blinking_jack.svg", "w") as f:
      f.write(blinking_jack)

    # C. Melting candle with flickering flame
    candle = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 160" width="100%" height="160">
  <defs>
    <filter id="candle-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <style>
    @keyframes sway {
      0%, 100% { transform: rotate(-2deg) scale(1); }
      50% { transform: rotate(3deg) scale(0.95); }
    }
    .flame-anim {
      transform-origin: 50px 48px;
      animation: sway 0.25s infinite ease-in-out;
    }
  </style>

  <!-- Skull Candle Holder -->
  <g transform="translate(15, 95)">
    <rect width="70" height="40" rx="14" fill="#f8f9fa" stroke="#1c1c1c" stroke-width="2.5"/>
    <circle cx="28" cy="18" r="6" fill="#1c1c1c"/>
    <circle cx="42" cy="18" r="6" fill="#1c1c1c"/>
    <path d="M 28 30 Q 35 36, 42 30" fill="none" stroke="#1c1c1c" stroke-width="2"/>
  </g>

  <!-- Candle Wax Pillar -->
  <rect x="38" y="55" width="24" height="50" rx="3" fill="#ffd166" stroke="#1c1c1c" stroke-width="2"/>
  
  <!-- Melted dripping wax details -->
  <path d="M 38 60 Q 42 75, 45 60" fill="#ffd166" stroke="#1c1c1c" stroke-width="2"/>
  <path d="M 52 58 Q 55 78, 57 58" fill="#ffd166" stroke="#1c1c1c" stroke-width="2"/>

  <!-- Wick -->
  <line x1="50" y1="55" x2="50" y2="46" stroke="#000" stroke-width="2.5"/>

  <!-- Glowing Flame -->
  <g class="flame-anim" filter="url(#candle-glow)">
    <path d="M 50 46 C 45 42, 42 30, 50 18 C 58 30, 55 42, 50 46 Z" fill="#ff7518"/>
    <path d="M 50 44 C 47 40, 45 32, 50 24 C 55 32, 53 40, 50 44 Z" fill="#ffd166"/>
  </g>
</svg>"""
    with open("halloween/animations/candle.svg", "w") as f:
      f.write(candle)
    print("Animations generated.")

    # ==================== 6. Custom Stats Cards ====================
    # A. Stats Card: Tombstone style
    print("Generating custom stats.svg...")
    stats_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 200" width="450" height="200">
  <defs>
    <linearGradient id="tomb-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1c1c1c" />
      <stop offset="100%" stop-color="#0d1117" />
    </linearGradient>
  </defs>
  <!-- Tombstone Silhouette Backing Frame -->
  <rect width="450" height="200" rx="14" fill="url(#tomb-grad)" stroke="#5a189a" stroke-width="2"/>
  
  <!-- Cobwebs in corners -->
  <path d="M 5 35 Q 25 25, 35 5 M 5 20 Q 18 18, 20 5 M 5 10 Q 10 10, 10 5" stroke="#ff7518" stroke-width="1.2" stroke-opacity="0.6" fill="none"/>
  <path d="M 445 35 Q 425 25, 415 5 M 445 20 Q 432 18, 430 5 M 445 10 Q 440 10, 440 5" stroke="#ff7518" stroke-width="1.2" stroke-opacity="0.6" fill="none"/>

  <!-- Tombstone top arch decor -->
  <path d="M 120 30 C 180 15, 270 15, 330 30" fill="none" stroke="#e85d04" stroke-width="2" stroke-linecap="round"/>

  <text x="225" y="32" fill="#ffd166" font-family="monospace" font-weight="bold" font-size="14" text-anchor="middle">// GHOSTLY STATS.bin</text>

  <!-- Left: Glowing Tombstone RIP ring -->
  <g transform="translate(10, 0)">
    <path d="M 40 145 C 40 90, 100 90, 100 145 Z" fill="#1c1c1c" stroke="#ff7518" stroke-width="2"/>
    <text x="70" y="125" fill="#f8f9fa" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">RIP</text>
    <text x="70" y="165" fill="#ff7518" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">DEV LEVEL</text>
  </g>

  <!-- Stats List -->
  <g transform="translate(160, 50)" fill="#f8f9fa" font-family="monospace" font-size="13">
    <!-- Commits -->
    <g transform="translate(0, 15)">
      <text x="0" y="0">Spooky Commits</text>
      <text x="260" y="0" fill="#ffd166" font-weight="bold" text-anchor="end">1,420</text>
      <line x1="0" y1="8" x2="260" y2="8" stroke="#5a189a" stroke-width="1" stroke-opacity="0.4"/>
    </g>
    <!-- Pull Requests -->
    <g transform="translate(0, 45)">
      <text x="0" y="0">Magic PRs</text>
      <text x="260" y="0" fill="#7fff00" font-weight="bold" text-anchor="end">184</text>
      <line x1="0" y1="8" x2="260" y2="8" stroke="#5a189a" stroke-width="1" stroke-opacity="0.4"/>
    </g>
    <!-- Stars -->
    <g transform="translate(0, 75)">
      <text x="0" y="0">Haunted Stars</text>
      <text x="260" y="0" fill="#ff7518" font-weight="bold" text-anchor="end">92</text>
      <line x1="0" y1="8" x2="260" y2="8" stroke="#5a189a" stroke-width="1" stroke-opacity="0.4"/>
    </g>
    <!-- Issues -->
    <g transform="translate(0, 105)">
      <text x="0" y="0">Banish Issues</text>
      <text x="260" y="0" fill="#f8f9fa" font-weight="bold" text-anchor="end">56</text>
      <line x1="0" y1="8" x2="260" y2="8" stroke="#5a189a" stroke-width="1" stroke-opacity="0.4"/>
    </g>
  </g>
</svg>"""
    with open("halloween/stats.svg", "w") as f:
      f.write(stats_svg)

    # B. Languages Card: Potion shelves theme
    print("Generating custom langs.svg...")
    langs_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 200" width="450" height="200">
  <rect width="450" height="200" rx="14" fill="#0d1117" stroke="#7fff00" stroke-width="2"/>
  
  <text x="25" y="32" fill="#7fff00" font-family="monospace" font-weight="bold" font-size="14">// SPOOKY INGREDIENTS</text>
  <line x1="20" y1="40" x2="430" y2="40" stroke="#1c1c1c" stroke-width="2"/>

  <!-- Potion Shelf design for languages -->
  <g transform="translate(25, 55)" font-family="monospace" font-size="12" fill="#f8f9fa">
    <!-- TS: Purple Potion -->
    <g transform="translate(0, 10)">
      <path d="M 12 18 L 6 32 C 4 37, 10 40, 15 40 L 20 40 C 25 40, 31 37, 29 32 L 23 18 Z" fill="#5a189a" stroke="#8b5cf6" stroke-width="1.5"/>
      <rect x="15" y="14" width="5" height="4" fill="#facc15"/>
      <text x="45" y="28">TypeScript Potion</text>
      <text x="380" y="28" fill="#8b5cf6" font-weight="bold" text-anchor="end">85%</text>
    </g>

    <!-- JS: Orange Liquid -->
    <g transform="translate(0, 50)">
      <path d="M 12 18 L 6 32 C 4 37, 10 40, 15 40 L 20 40 C 25 40, 31 37, 29 32 L 23 18 Z" fill="#e85d04" stroke="#ff7518" stroke-width="1.5"/>
      <rect x="15" y="14" width="5" height="4" fill="#facc15"/>
      <text x="45" y="28">JavaScript Brew</text>
      <text x="380" y="28" fill="#ff7518" font-weight="bold" text-anchor="end">78%</text>
    </g>

    <!-- Python: Glowing Slime -->
    <g transform="translate(0, 90)">
      <path d="M 12 18 L 6 32 C 4 37, 10 40, 15 40 L 20 40 C 25 40, 31 37, 29 32 L 23 18 Z" fill="#240046" stroke="#7fff00" stroke-width="1.5"/>
      <rect x="15" y="14" width="5" height="4" fill="#facc15"/>
      <!-- Glowing green liquid bubble -->
      <circle cx="17" cy="32" r="4" fill="#7fff00"/>
      <text x="45" y="28">Python Slime</text>
      <text x="380" y="28" fill="#7fff00" font-weight="bold" text-anchor="end">70%</text>
    </g>
  </g>
</svg>"""
    with open("halloween/langs.svg", "w") as f:
      f.write(langs_svg)

    # C. Trophies Card: Coffin Display
    print("Generating custom trophies.svg...")
    trophies_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 200" width="450" height="200">
  <rect width="450" height="200" rx="14" fill="#1c1c1c" stroke="#ff7518" stroke-width="2"/>
  <text x="25" y="32" fill="#ff7518" font-family="monospace" font-weight="bold" font-size="14">// SPOOKY COFFIN HALL</text>
  <line x1="20" y1="40" x2="430" y2="40" stroke="#0d1117" stroke-width="2"/>

  <!-- Coffin 1: Code Warrior -->
  <g transform="translate(30, 60)">
    <!-- Coffin frame shape -->
    <polygon points="15,0 45,0 55,20 45,100 15,100 5,20" fill="#0d1117" stroke="#8b5cf6" stroke-width="2"/>
    <text x="30" y="45" fill="#8b5cf6" font-family="monospace" font-size="9" text-anchor="middle" font-weight="bold">CODE</text>
    <text x="30" y="60" fill="#f8f9fa" font-family="monospace" font-size="8" text-anchor="middle">RIP</text>
  </g>

  <!-- Coffin 2: PR Champion -->
  <g transform="translate(195, 60)">
    <polygon points="15,0 45,0 55,20 45,100 15,100 5,20" fill="#0d1117" stroke="#ff7518" stroke-width="2"/>
    <text x="30" y="45" fill="#ff7518" font-family="monospace" font-size="9" text-anchor="middle" font-weight="bold">PRs</text>
    <text x="30" y="60" fill="#f8f9fa" font-family="monospace" font-size="8" text-anchor="middle">RIP</text>
  </g>

  <!-- Coffin 3: Bug Hunter -->
  <g transform="translate(360, 60)">
    <polygon points="15,0 45,0 55,20 45,100 15,100 5,20" fill="#0d1117" stroke="#7fff00" stroke-width="2"/>
    <text x="30" y="45" fill="#7fff00" font-family="monospace" font-size="9" text-anchor="middle" font-weight="bold">BUGS</text>
    <text x="30" y="60" fill="#f8f9fa" font-family="monospace" font-size="8" text-anchor="middle">RIP</text>
  </g>
</svg>"""
    with open("halloween/trophies.svg", "w") as f:
      f.write(trophies_svg)
    print("Cards generated.")

    # ==================== 7. Output files for GitHub Actions Workflow ====================
    print("Generating github-snake.yml...")
    snake_workflow_content = """name: Generate Contribution Snake

on:
  # Run automatically every 24 hours
  schedule:
    - cron: "0 0 * * *"
  
  # Allows to manually run the job at any time
  workflow_dispatch:
  
  # Run on every push on the main branch
  push:
    branches:
    - main
    - master

permissions:
  contents: write

jobs:
  generate:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    
    steps:
      # Generates a game-of-life game from a github user contribution graph, output a svg animation
      - name: Generate github-contribution-grid-snake
        uses: Platane/snk/svg-only@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg?color_snake=purple&color_dots=#161b22,#ffee4a,#ffc501,#fe9600,#03001c
            dist/github-contribution-grid-snake-light.svg?color_snake=purple&color_dots=#f8fafc,#ffee4a,#ffc501,#fe9600,#03001c
        
      # Push the content of <build_dir> to a branch
      - name: Push github-contribution-grid-snake.svg to the output branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
"""
    with open(".github/workflows/github-snake.yml", "w") as f:
      f.write(snake_workflow_content)

    # ==================== 8. README.md ====================
    print("Generating README.md...")
    readme_template = """<h1 align="center">ACCESS SYSTEM // {name_upper}</h1>

<p align="center">
  <img alt="Halloween Room Developer Banner" src="halloween/banner.svg" width="100%">
</p>

<!-- Navigation Buttons -->
<p align="center">
  <a href="#bio">
    <img src="halloween/buttons/about.svg" width="180">
  </a>
  <a href="#skills">
    <img src="halloween/buttons/skills.svg" width="180">
  </a>
  <a href="#projects">
    <img src="halloween/buttons/projects.svg" width="180">
  </a>
  <a href="#contact">
    <img src="halloween/buttons/contact.svg" width="180">
  </a>
</p>

<p align="center">
  <img src="halloween/dividers/vines.svg" width="100%">
</p>

<a id="bio"></a>
<h2 align="center">🔮 SYSTEM_BIOMETRICS // ACCESS</h2>

<table align="center" border="0" cellpadding="15" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto;">
  <tr style="border: 0px;">
    <!-- Animated typing ghost flanking the bio -->
    <td align="center" valign="top" style="border: 0px; padding: 10px; width: 40%;">
      <img src="halloween/animations/typing_ghost.svg" alt="Animated Coding Ghost" width="100%" style="max-width: 250px;">
    </td>
    <!-- Bio text details -->
    <td valign="top" style="border: 0px; padding: 20px; width: 60%; font-family: monospace; color: #cbd5e1;">
      <h3>HALLOWEEN_NODE.bin</h3>
      <p><b>&gt; IDENTITY:</b> {name} / @{username}</p>
      <p><b>&gt; ACCESS_PORT:</b> <a href="mailto:{email}" style="color: #ff7518;">{email}</a></p>
      <p><b>&gt; POWER_LEVEL:</b> <code>Stay Spooky. Keep Building.</code></p>
      <hr style="border-color: #5a189a; opacity: 0.4;">
      <p>
        Welcome, mortal node, to my digital workstation. I construct responsive, highly modular web architectures under the coverage of midnight purples and glowing neon spell-work. Proactive code wizardry is the rule of this domain.
      </p>
    </td>
  </tr>
</table>

<p align="center">
  <img src="halloween/dividers/bats.svg" width="100%">
</p>

<a id="skills"></a>
<h2 align="center">🔥 SPOOKY SKILLS ORBS</h2>

<!-- Modular coding icons grid -->
<p align="center">
  <img src="halloween/icons/html.svg" width="70" alt="HTML">
  <img src="halloween/icons/css.svg" width="70" alt="CSS">
  <img src="halloween/icons/js.svg" width="70" alt="JS">
  <img src="halloween/icons/python.svg" width="70" alt="Python">
  <img src="halloween/icons/react.svg" width="70" alt="React">
  <img src="halloween/icons/node.svg" width="70" alt="Node.js">
  <img src="halloween/icons/docker.svg" width="70" alt="Docker">
</p>

<p align="center">
  <img src="halloween/dividers/ghosts.svg" width="100%">
</p>

<h2 align="center">💀 COFFIN ARCHIVES // PERFORMANCE</h2>

<p align="center">
  <img src="halloween/stats.svg" alt="System Stats" width="48%" style="max-width: 440px; margin-right: 15px;">
  <img src="halloween/langs.svg" alt="Languages" width="48%" style="max-width: 440px;">
</p>
<p align="center">
  <img src="halloween/trophies.svg" alt="Coffin Trophies" width="98%" style="max-width: 900px; margin-top: 15px;">
</p>

<p align="center">
  <img src="halloween/dividers/vines.svg" width="100%">
</p>

<h2 align="center">🎃 CONTRIBUTION SPIDER GRID</h2>

<p align="center">
  <!-- Dynamic snake contribution graph -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg?v=2">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake-light.svg?v=2">
    <img alt="GitHub Snake Game" src="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg?v=2" width="100%">
  </picture>
</p>

<p align="center" style="font-family: monospace; color: #71717a; font-size: 11px;">
  PORTAL SECURED VISITORS: <img src="https://profile-counter.glitch.me/{username}/count.svg" alt="Views Counter" style="vertical-align: middle;"> // SECURE CONNECTIONS COMPLETED
</p>"""

    readme_content = readme_template.replace("{name}", name).replace("{name_upper}", name.upper()).replace("{username}", username).replace("{email}", email).replace("{role}", role).replace("{tagline}", tagline).replace("{skills_html}", skills_html)
    with open("README.md", "w") as f:
      f.write(readme_content)
    print("README.md generated successfully!")
    print("All Halloween modular assets generated successfully!")

if __name__ == "__main__":
    main()
