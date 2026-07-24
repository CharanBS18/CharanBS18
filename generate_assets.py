import base64
import os

def get_base64_image(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Required image {filename} not found.")
    with open(filename, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode('utf-8')

def main():
    print("Loading image assets...")
    try:
        char_b64 = get_base64_image("character_600.png")
        avatar_b64 = get_base64_image("avatar.png")
        print("Images loaded and encoded successfully.")
    except Exception as e:
        print(f"Error loading images: {e}")
        return

    # User details
    name = "Charan BS"
    username = "CharanBS18"
    email = "charan201204@gmail.com"
    role = "Full-Stack Developer"
    tagline = "Stay Sharp. Keep Building."
    quote = "Architecting digital worlds with cybernetic precision."
    skills_list = ["React", "Next.js", "TypeScript", "Node.js", "Python", "Docker", "TailwindCSS"]
    skills_html = " ".join([f"<code>{s}</code>" for s in skills_list])

    # 1. banner.svg (Dark Mode - Matte Black & Halloween Purple/Orange Theme)
    print("Generating banner.svg (dark theme)...")
    banner_dark_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="1280" height="740">
  <defs>
    <!-- Background Grid (Modern Purple/Slate) -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#8b5cf6" stroke-width="1.2" stroke-opacity="0.08"/>
    </pattern>
    
    <!-- Cybernetic Hexagon Pattern -->
    <pattern id="hex-pattern" width="120" height="104" patternUnits="userSpaceOnUse" patternTransform="scale(0.5)">
      <path d="M 60 0 L 120 34.6 L 120 104 L 60 138.6 L 0 104 L 0 34.6 Z" fill="none" stroke="#ea580c" stroke-width="1" stroke-opacity="0.04"/>
    </pattern>

    <!-- Radial Glow Gradients (Purple / Orange) -->
    <radialGradient id="green-glow-1" cx="20%" cy="20%" r="50%">
      <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#0a0a0a" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="green-glow-2" cx="80%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#ea580c" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#0a0a0a" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="neon-glow" cx="50%" cy="80%" r="40%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#0a0a0a" stop-opacity="0"/>
    </radialGradient>
    
    <!-- Linear Gradients for UI Elements -->
    <linearGradient id="signature-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="50%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#facc15"/>
    </linearGradient>

    <!-- Glowing Filters -->
    <filter id="neon-glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="subtle-glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Clip Paths -->
    <clipPath id="banner-clip">
      <rect width="1280" height="740" rx="20"/>
    </clipPath>
    <clipPath id="hologram-clip">
      <rect x="780" y="100" width="450" height="0">
        <animate attributeName="height" from="0" to="620" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      </rect>
    </clipPath>
    
    <!-- Typing Clipping Paths -->
    <clipPath id="clip-terminal-line1">
      <rect x="0" y="100" width="0" height="40">
        <animate attributeName="width" from="0" to="400" dur="1.2s" begin="0.8s" fill="freeze"/>
      </rect>
    </clipPath>
    <clipPath id="clip-quote-line">
      <rect x="0" y="10" width="0" height="80">
        <animate attributeName="width" from="0" to="640" dur="2s" begin="3.2s" fill="freeze"/>
      </rect>
    </clipPath>
  </defs>

  <style>
    <![CDATA[
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&amp;display=swap');
    
    .name-text {
      font-family: 'Syne', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-weight: 800;
      font-size: 44px;
      letter-spacing: 2px;
    }

    @keyframes blink-cursor {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
    .cursor-pipe {
      animation: blink-cursor 0.8s infinite;
      font-family: monospace;
      font-weight: bold;
    }
    
    @keyframes pulse-orb {
      0%, 100% { transform: scale(1); opacity: 0.3; }
      50% { transform: scale(1.08); opacity: 0.45; }
    }
    .ambient-orb-1 {
      transform-origin: 200px 150px;
      animation: pulse-orb 10s ease-in-out infinite;
    }
    .ambient-orb-2 {
      transform-origin: 1000px 500px;
      animation: pulse-orb 12s ease-in-out infinite;
    }

    /* Tech Stack Pills Hover Effect */
    .tech-pill {
      transition: all 0.3s ease;
      cursor: pointer;
    }
    .tech-pill:hover {
      fill: #111827;
      stroke: #f97316;
      filter: drop-shadow(0 0 8px rgba(249, 115, 22, 0.5));
    }
    
    /* Code typing animation line-by-line using opacity and keyframes */
    @keyframes type-code-1 { 0%, 10% { opacity: 0; } 11%, 100% { opacity: 1; } }
    @keyframes type-code-2 { 0%, 20% { opacity: 0; } 21%, 100% { opacity: 1; } }
    @keyframes type-code-3 { 0%, 30% { opacity: 0; } 31%, 100% { opacity: 1; } }
    @keyframes type-code-4 { 0%, 40% { opacity: 0; } 41%, 100% { opacity: 1; } }
    @keyframes type-code-5 { 0%, 50% { opacity: 0; } 51%, 100% { opacity: 1; } }
    @keyframes type-code-6 { 0%, 60% { opacity: 0; } 61%, 100% { opacity: 1; } }
    @keyframes type-code-7 { 0%, 70% { opacity: 0; } 71%, 100% { opacity: 1; } }
    
    .code-l1 { animation: type-code-1 6s forwards; }
    .code-l2 { animation: type-code-2 6s forwards; }
    .code-l3 { animation: type-code-3 6s forwards; }
    .code-l4 { animation: type-code-4 6s forwards; }
    .code-l5 { animation: type-code-5 6s forwards; }
    .code-l6 { animation: type-code-6 6s forwards; }
    .code-l7 { animation: type-code-7 6s forwards; }
    ]]>
  </style>

  <!-- Main Banner Wrapper (Clipped to Rounded Corners) -->
  <g clip-path="url(#banner-clip)">
    <!-- Deep Matte Background (neutral-950 / #0a0a0a) -->
    <rect width="1280" height="740" fill="#0a0a0a"/>
    <rect width="1280" height="740" fill="url(#grid)"/>
    <rect width="1280" height="740" fill="url(#hex-pattern)"/>

    <!-- Ambient Glowing Orbs -->
    <circle cx="200" cy="150" r="220" fill="url(#green-glow-1)" class="ambient-orb-1" />
    <circle cx="1000" cy="500" r="300" fill="url(#green-glow-2)" class="ambient-orb-2" />
    <circle cx="640" cy="700" r="250" fill="url(#neon-glow)" opacity="0.3" />

    <!-- Circuit Lines & Geometric Tech Accents -->
    <path d="M 0 100 H 300 L 350 150 H 500" fill="none" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.2" stroke-dasharray="8 8"/>
    <path d="M 1280 600 H 1000 L 950 550 H 700" fill="none" stroke="#f97316" stroke-width="1.5" stroke-opacity="0.15" stroke-dasharray="10 6"/>
    <circle cx="500" cy="150" r="4" fill="#7c3aed" opacity="0.5"/>
    <circle cx="700" cy="550" r="4" fill="#f97316" opacity="0.4"/>

    <!-- Floating Hexagons and Binary Particles -->
    <g opacity="0.3">
      <text x="80" y="80" fill="#7c3aed" font-family="monospace" font-size="12" opacity="0.35">
        101010
        <animate attributeName="opacity" values="0.1;0.9;0.1" dur="4s" repeatCount="indefinite" />
      </text>
      <text x="1150" y="120" fill="#f97316" font-family="monospace" font-size="12" opacity="0.4">
        011001
        <animate attributeName="opacity" values="0.9;0.2;0.9" dur="5s" repeatCount="indefinite" />
      </text>
      <text x="720" y="680" fill="#7c3aed" font-family="monospace" font-size="12" opacity="0.25">
        1101
        <animate attributeName="opacity" values="0.2;0.8;0.2" dur="3s" repeatCount="indefinite" />
      </text>
    </g>

    <!-- LEFT COLUMN: Terminal & Dashboard Panel (x=50, y=50, width=700, height=640) -->
    <rect x="50" y="50" width="700" height="640" rx="16" fill="#09090b" stroke="#27272a" stroke-width="1.5" style="filter: drop-shadow(0 4px 20px rgba(0, 0, 0, 0.4));" />
    
    <!-- Terminal Header Bar -->
    <path d="M 50 85 H 750" stroke="#27272a" stroke-width="1" />
    <circle cx="75" cy="68" r="6" fill="#ff5f56"/>
    <circle cx="95" cy="68" r="6" fill="#ffbd2e"/>
    <circle cx="115" cy="68" r="6" fill="#27c93f"/>
    <text x="365" y="73" fill="#ea580c" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1" text-anchor="middle" opacity="0.8">HACKER_WORKSTATION // README.md</text>

    <!-- Terminal Content Area -->
    <!-- Line 1: user@dev:~$ cat README.md -->
    <g clip-path="url(#clip-terminal-line1)">
      <text x="80" y="125" fill="#8b5cf6" font-family="monospace" font-size="18" font-weight="bold" letter-spacing="0.5">
        <tspan fill="#737373">user@dev</tspan>:<tspan fill="#e2e8f0">~$</tspan> cat README.md
      </text>
    </g>
    <!-- Blinking Terminal Cursor for Line 1 -->
    <text x="80" y="125" fill="#8b5cf6" font-family="monospace" font-size="18" font-weight="bold" class="cursor-pipe">
      |
      <animate attributeName="x" from="80" to="350" dur="1.2s" begin="0.8s" fill="freeze" />
      <animate attributeName="visibility" values="visible;hidden" keyTimes="0;0.99" dur="2.0s" fill="freeze" />
    </text>

    <!-- Bold Extended Name: CHARAN BS (Syne Bold Style) -->
    <g transform="translate(80, 192)" filter="url(#subtle-glow)">
      <text class="name-text" fill="url(#signature-grad)" opacity="0">
        CHARAN BS
        <animate attributeName="opacity" from="0" to="1" dur="0.8s" begin="1.8s" fill="freeze" />
      </text>
    </g>

    <!-- Cycling Role Titles -->
    <g transform="translate(80, 220)">
      <text x="0" y="20" fill="#8b5cf6" font-family="monospace" font-size="20" font-weight="bold" letter-spacing="1">
        > ROLE: <tspan fill="#8b5cf6" class="cursor-pipe">|</tspan>
      </text>
      
      <!-- Role 1: Full-Stack Developer -->
      <g>
        <text x="90" y="20" fill="#f97316" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
          Full-Stack Developer
          <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.05;0.22;0.25;1" dur="12s" repeatCount="indefinite" />
        </text>
      </g>

      <!-- Role 2: Cyberpunk Coder -->
      <g>
        <text x="90" y="20" fill="#a855f7" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
          Cyberpunk Coder
          <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.25;0.30;0.47;0.50;1" dur="12s" repeatCount="indefinite" />
        </text>
      </g>

      <!-- Role 3: UI/UX Engineer -->
      <g>
        <text x="90" y="20" fill="#facc15" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
          UI/UX Engineer
          <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.50;0.55;0.72;0.75;1" dur="12s" repeatCount="indefinite" />
        </text>
      </g>

      <!-- Role 4: Systems Architect -->
      <g>
        <text x="90" y="20" fill="#fafafa" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
          Systems Architect
          <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.75;0.80;0.97;1;1" dur="12s" repeatCount="indefinite" />
        </text>
      </g>
    </g>

    <!-- Tagline Quote Box -->
    <g transform="translate(80, 270)">
      <rect x="0" y="0" width="640" height="90" rx="8" fill="#18181b" stroke="#27272a" stroke-width="1.5" />
      <path d="M 0 15 V 0 H 15 M 625 0 H 640 V 15 M 640 75 V 90 H 625 M 15 90 H 0 V 75" fill="none" stroke="#ea580c" stroke-width="2" />
      
      <!-- Quote text typing -->
      <g clip-path="url(#clip-quote-line)">
        <text x="25" y="50" fill="#e4e4e7" font-family="monospace" font-size="14" font-style="italic" font-weight="bold">
          "{quote}"
        </text>
      </g>
      <!-- Blinking cursor for quote -->
      <text x="25" y="50" fill="#ea580c" font-family="monospace" font-size="14" font-weight="bold" class="cursor-pipe">
        |
        <animate attributeName="x" from="25" to="610" dur="2s" begin="3.2s" fill="freeze" />
        <animate attributeName="visibility" values="visible;hidden" keyTimes="0;0.99" dur="5.2s" fill="freeze" />
      </text>
    </g>

    <!-- About Me Section -->
    <g transform="translate(80, 390)">
      <text x="0" y="20" fill="#8b5cf6" font-family="monospace" font-size="16" font-weight="bold">> ABOUT_ME:</text>
      
      <!-- Lines that appear sequentially -->
      <text x="20" y="50" fill="#d4d4d8" font-family="monospace" font-size="15" opacity="0">
        - Professional full-stack engineer and designer.
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="5.5s" fill="freeze"/>
      </text>
      <text x="20" y="80" fill="#d4d4d8" font-family="monospace" font-size="15" opacity="0">
        - Focused on secure, high-performance web products.
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="6.2s" fill="freeze"/>
      </text>
      <text x="20" y="110" fill="#d4d4d8" font-family="monospace" font-size="15" opacity="0">
        - Turning lines of code into responsive cyberpunk UI.
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="6.9s" fill="freeze"/>
      </text>
    </g>

    <!-- Tech Stack Pills -->
    <g transform="translate(80, 530)">
      <!-- Title -->
      <text x="0" y="15" fill="#f97316" font-family="monospace" font-size="16" font-weight="bold">> TECH_STACK:</text>
      
      <!-- Pills -->
      <!-- Pill 1: React -->
      <g transform="translate(20, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="7.5s" fill="freeze" />
        <rect class="tech-pill" x="0" y="0" width="75" height="30" rx="15" fill="#11131c" stroke="#8b5cf6" stroke-width="1.5" />
        <text x="37.5" y="19" fill="#e2e8f0" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">React</text>
      </g>

      <!-- Pill 2: Next.js -->
      <g transform="translate(105, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="7.7s" fill="freeze" />
        <rect class="tech-pill" x="0" y="0" width="85" height="30" rx="15" fill="#11131c" stroke="#8b5cf6" stroke-width="1.5" />
        <text x="42.5" y="19" fill="#e2e8f0" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Next.js</text>
      </g>

      <!-- Pill 3: TypeScript -->
      <g transform="translate(200, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="7.9s" fill="freeze" />
        <rect class="tech-pill" x="0" y="0" width="105" height="30" rx="15" fill="#11131c" stroke="url(#signature-grad)" stroke-width="1.5" />
        <text x="52.5" y="19" fill="#fafafa" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">TypeScript</text>
      </g>

      <!-- Pill 4: Node.js -->
      <g transform="translate(315, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="8.1s" fill="freeze" />
        <rect class="tech-pill" x="0" y="0" width="85" height="30" rx="15" fill="#11131c" stroke="#ea580c" stroke-width="1.5" />
        <text x="42.5" y="19" fill="#ea580c" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Node.js</text>
      </g>

      <!-- Pill 5: Python -->
      <g transform="translate(410, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="8.3s" fill="freeze" />
        <rect class="tech-pill" x="0" y="0" width="80" height="30" rx="15" fill="#11131c" stroke="#ea580c" stroke-width="1.5" />
        <text x="40" y="19" fill="#ea580c" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Python</text>
      </g>

      <!-- Pill 6: Docker -->
      <g transform="translate(500, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="8.5s" fill="freeze" />
        <rect class="tech-pill" x="0" y="0" width="80" height="30" rx="15" fill="#11131c" stroke="#facc15" stroke-width="1.5" />
        <text x="40" y="19" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Docker</text>
      </g>
    </g>

    <!-- Animated System/Stats Bar -->
    <g transform="translate(80, 620)">
      <!-- CPU Overclock Status -->
      <text x="0" y="15" fill="#fafafa" font-family="monospace" font-size="12" font-weight="bold">CORE_OVERCLOCK: 99%</text>
      <rect x="150" y="5" width="200" height="12" rx="3" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <rect x="152" y="7" width="0" height="8" rx="2" fill="url(#signature-grad)">
        <animate attributeName="width" from="0" to="196" dur="2s" begin="5s" fill="freeze" calcMode="spline" keySplines="0.1 0.8 0.2 1"/>
      </rect>

      <!-- Neural Bandwidth Status -->
      <text x="380" y="15" fill="#fafafa" font-family="monospace" font-size="12" font-weight="bold">NEURAL_LINK: 100%</text>
      <rect x="520" y="5" width="120" height="12" rx="3" fill="#18181b" stroke="#27272a" stroke-width="1"/>
      <rect x="522" y="7" width="0" height="8" rx="2" fill="#f97316">
        <animate attributeName="width" from="0" to="116" dur="2s" begin="5.5s" fill="freeze" calcMode="spline" keySplines="0.1 0.8 0.2 1"/>
      </rect>
    </g>

    <!-- RIGHT COLUMN: Code Card, Slogan sign, Character -->
    <!-- Code Editor Card (types buildDreams JSX) -->
    <g transform="translate(780, 50)">
      <rect x="0" y="0" width="450" height="240" rx="12" fill="#09090b" stroke="#27272a" stroke-width="1.5" style="filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.4));"/>
      <path d="M 0 35 H 450" stroke="#27272a" stroke-width="1.2"/>
      <!-- Dots -->
      <circle cx="20" cy="18" r="5" fill="#ff5f56"/>
      <circle cx="35" cy="18" r="5" fill="#ffbd2e"/>
      <circle cx="50" cy="18" r="5" fill="#27c93f"/>
      <text x="225" y="22" fill="#737373" font-family="monospace" font-size="11" font-weight="bold" opacity="0.6" text-anchor="middle">buildDreams.jsx</text>

      <!-- Code Snippet -->
      <g transform="translate(20, 60)" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="0.2">
        <text class="code-l1" x="0" y="15" fill="#8b5cf6">const <tspan fill="#f97316">buildDreams</tspan> = <tspan fill="#e2e8f0">() => {</tspan></text>
        <text class="code-l2" x="20" y="35" fill="#8b5cf6">while <tspan fill="#e2e8f0">(coding) {</tspan></text>
        <text class="code-l3" x="40" y="55" fill="#ea580c">coffee<tspan fill="#e2e8f0">.consume();</tspan></text>
        <text class="code-l4" x="40" y="75" fill="#8b5cf6">ideas<tspan fill="#e2e8f0">.compile();</tspan></text>
        <text class="code-l5" x="40" y="95" fill="#facc15">dreams<tspan fill="#e2e8f0">.deploy();</tspan></text>
        <text class="code-l6" x="20" y="115" fill="#e2e8f0">}</text>
        <text class="code-l7" x="0" y="135" fill="#e2e8f0">};</text>
      </g>
    </g>

    <!-- Slogan Sign: STAY SHARP. KEEP BUILDING. -->
    <g transform="translate(780, 310)">
      <rect x="0" y="0" width="450" height="70" rx="8" fill="#09090b" stroke="#27272a" stroke-width="1.5" />
      <text x="225" y="42" fill="#f97316" font-family="monospace" font-size="18" font-weight="bold" letter-spacing="3" text-anchor="middle">STAY SHARP. KEEP BUILDING.</text>
    </g>

    <!-- Holographic Scan Character Container -->
    <g clip-path="url(#hologram-clip)">
      <image href="data:image/png;base64,{char_b64}" x="793" y="390" width="424" height="600" />
      <rect x="780" y="390" width="450" height="350" fill="url(#grid)" opacity="0.35" pointer-events="none" />
    </g>

    <!-- One-time top-to-bottom scan line for hologram reveal -->
    <line x1="780" y1="100" x2="1230" y2="100" stroke="#8b5cf6" stroke-width="3" opacity="0" filter="url(#neon-glow-filter)">
      <animate attributeName="y1" from="100" to="740" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      <animate attributeName="y2" from="100" to="740" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.9;1" dur="2s" begin="0.5s" fill="freeze" />
    </line>

    <!-- Continuous Full-width Scanner Line Sweeping every 3.5s -->
    <line x1="0" y1="0" x2="1280" y2="0" stroke="#f97316" stroke-width="2" opacity="0" style="filter: drop-shadow(0 0 5px #f97316);">
      <animate attributeName="y1" from="0" to="740" dur="3.5s" begin="2.5s" repeatCount="indefinite" />
      <animate attributeName="y2" from="0" to="740" dur="3.5s" begin="2.5s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;0.8;0.8;0" keyTimes="0;0.1;0.9;1" dur="3.5s" begin="2.5s" repeatCount="indefinite" />
    </line>
  </g>
</svg>"""

    banner_dark_content = banner_dark_template.replace("{char_b64}", char_b64).replace("{quote}", quote)
    with open("banner.svg", "w") as f:
      f.write(banner_dark_content)
    print("banner.svg generated.")

    # 2. banner-light.svg (Light Mode - Premium Purple/Orange Theme)
    print("Generating banner-light.svg (light theme)...")
    banner_light_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 740" width="1280" height="740">
  <defs>
    <!-- Background Grid -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#7c3aed" stroke-width="1" stroke-opacity="0.05"/>
    </pattern>
    
    <!-- Cybernetic Hexagon Pattern -->
    <pattern id="hex-pattern" width="120" height="104" patternUnits="userSpaceOnUse" patternTransform="scale(0.5)">
      <path d="M 60 0 L 120 34.6 L 120 104 L 60 138.6 L 0 104 L 0 34.6 Z" fill="none" stroke="#ea580c" stroke-width="1" stroke-opacity="0.03"/>
    </pattern>

    <!-- Radial Glow Gradients -->
    <radialGradient id="green-glow" cx="20%" cy="20%" r="50%">
      <stop offset="0%" stop-color="#7c3aed" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="mint-glow" cx="80%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#ea580c" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </radialGradient>
    
    <!-- Linear Gradients for UI Elements -->
    <linearGradient id="signature-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8b5cf6"/>
      <stop offset="50%" stop-color="#f97316"/>
      <stop offset="100%" stop-color="#facc15"/>
    </linearGradient>

    <!-- Glowing Filters -->
    <filter id="neon-glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="subtle-glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Clip Paths -->
    <clipPath id="banner-clip">
      <rect width="1280" height="740" rx="20"/>
    </clipPath>
    <clipPath id="hologram-clip">
      <rect x="780" y="100" width="450" height="0">
        <animate attributeName="height" from="0" to="620" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      </rect>
    </clipPath>
    
    <!-- Typing Clipping Paths -->
    <clipPath id="clip-terminal-line1">
      <rect x="0" y="100" width="0" height="40">
        <animate attributeName="width" from="0" to="400" dur="1.2s" begin="0.8s" fill="freeze"/>
      </rect>
    </clipPath>
    <clipPath id="clip-quote-line">
      <rect x="0" y="10" width="0" height="80">
        <animate attributeName="width" from="0" to="640" dur="2s" begin="3.2s" fill="freeze"/>
      </rect>
    </clipPath>
  </defs>

  <style>
    <![CDATA[
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&amp;display=swap');
    
    .name-text {
      font-family: 'Syne', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-weight: 800;
      font-size: 44px;
      letter-spacing: 2px;
    }

    @keyframes blink-cursor {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
    .cursor-pipe {
      animation: blink-cursor 0.8s infinite;
      font-family: monospace;
      font-weight: bold;
    }

    /* Tech Stack Pills Hover Effect */
    .tech-pill {
      transition: all 0.3s ease;
      cursor: pointer;
    }
    .tech-pill:hover {
      fill: #f1f5f9;
      stroke: #f97316;
      filter: drop-shadow(0 0 6px rgba(249, 115, 22, 0.4));
    }
    
    /* Code typing animation line-by-line using opacity and keyframes */
    @keyframes type-code-1 { 0%, 10% { opacity: 0; } 11%, 100% { opacity: 1; } }
    @keyframes type-code-2 { 0%, 20% { opacity: 0; } 21%, 100% { opacity: 1; } }
    @keyframes type-code-3 { 0%, 30% { opacity: 0; } 31%, 100% { opacity: 1; } }
    @keyframes type-code-4 { 0%, 40% { opacity: 0; } 41%, 100% { opacity: 1; } }
    @keyframes type-code-5 { 0%, 50% { opacity: 0; } 51%, 100% { opacity: 1; } }
    @keyframes type-code-6 { 0%, 60% { opacity: 0; } 61%, 100% { opacity: 1; } }
    @keyframes type-code-7 { 0%, 70% { opacity: 0; } 71%, 100% { opacity: 1; } }
    
    .code-l1 { animation: type-code-1 6s forwards; }
    .code-l2 { animation: type-code-2 6s forwards; }
    .code-l3 { animation: type-code-3 6s forwards; }
    .code-l4 { animation: type-code-4 6s forwards; }
    .code-l5 { animation: type-code-5 6s forwards; }
    .code-l6 { animation: type-code-6 6s forwards; }
    .code-l7 { animation: type-code-7 6s forwards; }
    ]]>
  </style>

  <!-- Main Banner Wrapper (Clipped to Rounded Corners) -->
  <g clip-path="url(#banner-clip)">
    <!-- White / Light Theme Background -->
    <rect width="1280" height="740" fill="#f8fafc"/>
    <rect width="1280" height="740" fill="url(#grid)"/>
    <rect width="1280" height="740" fill="url(#hex-pattern)"/>

    <!-- Ambient Glowing Orbs -->
    <circle cx="200" cy="150" r="220" fill="url(#green-glow)" />
    <circle cx="1000" cy="500" r="300" fill="url(#mint-glow)" />

    <!-- Circuit Lines & Geometric Tech Accents -->
    <path d="M 0 100 H 300 L 350 150 H 500" fill="none" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.15" stroke-dasharray="8 8"/>
    <path d="M 1280 600 H 1000 L 950 550 H 700" fill="none" stroke="#ea580c" stroke-width="1.5" stroke-opacity="0.15" stroke-dasharray="10 6"/>
    <circle cx="500" cy="150" r="4" fill="#7c3aed" opacity="0.4"/>
    <circle cx="700" cy="550" r="4" fill="#ea580c" opacity="0.3"/>

    <!-- LEFT COLUMN: Terminal & Dashboard Panel (x=50, y=50, width=700, height=640) -->
    <rect x="50" y="50" width="700" height="640" rx="16" fill="#ffffff" stroke="#e4e4e7" stroke-width="1.5" style="filter: drop-shadow(0 4px 20px rgba(0, 0, 0, 0.05));" />
    
    <!-- Terminal Header Bar -->
    <path d="M 50 85 H 750" stroke="#e4e4e7" stroke-width="1" />
    <circle cx="75" cy="68" r="6" fill="#ff5f56"/>
    <circle cx="95" cy="68" r="6" fill="#ffbd2e"/>
    <circle cx="115" cy="68" r="6" fill="#27c93f"/>
    <text x="365" y="73" fill="#ea580c" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1" text-anchor="middle" opacity="0.8">HACKER_WORKSTATION // README.md</text>

    <!-- Terminal Content Area -->
    <!-- Line 1: user@dev:~$ cat README.md -->
    <g clip-path="url(#clip-terminal-line1)">
      <text x="80" y="125" fill="#7c3aed" font-family="monospace" font-size="18" font-weight="bold" letter-spacing="0.5">
        <tspan fill="#737373">user@dev</tspan>:<tspan fill="#71717a">~$</tspan> cat README.md
      </text>
    </g>
    <!-- Blinking Terminal Cursor for Line 1 -->
    <text x="80" y="125" fill="#7c3aed" font-family="monospace" font-size="18" font-weight="bold" class="cursor-pipe">
      |
      <animate attributeName="x" from="80" to="350" dur="1.2s" begin="0.8s" fill="freeze"/>
      <animate attributeName="visibility" values="visible;hidden" keyTimes="0;0.99" dur="2.0s" fill="freeze"/>
    </text>

    <!-- Bold Extended Name: CHARAN BS -->
    <g transform="translate(80, 192)" filter="url(#subtle-glow)">
      <text class="name-text" fill="url(#signature-grad)" opacity="0">
        CHARAN BS
        <animate attributeName="opacity" from="0" to="1" dur="0.8s" begin="1.8s" fill="freeze"/>
      </text>
    </g>

    <!-- Cycling Role Titles -->
    <g transform="translate(80, 220)">
      <text x="0" y="20" fill="#7c3aed" font-family="monospace" font-size="20" font-weight="bold" letter-spacing="1">
        > ROLE: <tspan fill="#7c3aed" class="cursor-pipe">|</tspan>
      </text>
      
      <text x="90" y="20" fill="#f97316" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
        Full-Stack Developer
        <animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.05;0.22;0.25;1" dur="12s" repeatCount="indefinite"/>
      </text>

      <text x="90" y="20" fill="#8b5cf6" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
        Cyberpunk Coder
        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.25;0.30;0.47;0.50;1" dur="12s" repeatCount="indefinite"/>
      </text>

      <text x="90" y="20" fill="#d97706" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
        UI/UX Engineer
        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.50;0.55;0.72;0.75;1" dur="12s" repeatCount="indefinite"/>
      </text>

      <text x="90" y="20" fill="#7c3aed" font-family="monospace" font-size="20" font-weight="bold" opacity="0">
        Systems Architect
        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.75;0.80;0.97;1;1" dur="12s" repeatCount="indefinite"/>
      </text>
    </g>

    <!-- Tagline Quote Box -->
    <g transform="translate(80, 270)">
      <rect x="0" y="0" width="640" height="90" rx="8" fill="#f8fafc" stroke="#e4e4e7" stroke-width="1.5"/>
      <path d="M 0 15 V 0 H 15 M 625 0 H 640 V 15 M 640 75 V 90 H 625 M 15 90 H 0 V 75" fill="none" stroke="#ea580c" stroke-width="2"/>
      
      <g clip-path="url(#clip-quote-line)">
        <text x="25" y="50" fill="#18181b" font-family="monospace" font-size="14" font-style="italic" font-weight="bold">
          "{quote}"
        </text>
      </g>
      <!-- Blinking cursor for quote -->
      <text x="25" y="50" fill="#7c3aed" font-family="monospace" font-size="14" font-weight="bold" class="cursor-pipe">
        |
        <animate attributeName="x" from="25" to="610" dur="2s" begin="3.2s" fill="freeze"/>
        <animate attributeName="visibility" values="visible;hidden" keyTimes="0;0.99" dur="5.2s" fill="freeze"/>
      </text>
    </g>

    <!-- About Me Section -->
    <g transform="translate(80, 390)">
      <text x="0" y="20" fill="#7c3aed" font-family="monospace" font-size="16" font-weight="bold">> ABOUT_ME:</text>
      <text x="20" y="50" fill="#3f3f46" font-family="monospace" font-size="15" opacity="0">
        - Professional full-stack engineer and designer.
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="5.5s" fill="freeze"/>
      </text>
      <text x="20" y="80" fill="#3f3f46" font-family="monospace" font-size="15" opacity="0">
        - Focused on secure, high-performance web products.
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="6.2s" fill="freeze"/>
      </text>
      <text x="20" y="110" fill="#3f3f46" font-family="monospace" font-size="15" opacity="0">
        - Turning lines of code into responsive cyberpunk UI.
        <animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="6.9s" fill="freeze"/>
      </text>
    </g>

    <!-- Tech Stack Pills -->
    <g transform="translate(80, 530)">
      <text x="0" y="15" fill="#ea580c" font-family="monospace" font-size="16" font-weight="bold">> TECH_STACK:</text>
      
      <!-- Pills -->
      <g transform="translate(20, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="7.5s" fill="freeze"/>
        <rect class="tech-pill" x="0" y="0" width="75" height="30" rx="15" fill="#f8fafc" stroke="#7c3aed" stroke-width="1.5"/>
        <text x="37.5" y="19" fill="#7c3aed" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">React</text>
      </g>

      <g transform="translate(105, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="7.7s" fill="freeze"/>
        <rect class="tech-pill" x="0" y="0" width="85" height="30" rx="15" fill="#f8fafc" stroke="#7c3aed" stroke-width="1.5"/>
        <text x="42.5" y="19" fill="#7c3aed" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Next.js</text>
      </g>

      <g transform="translate(200, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="7.9s" fill="freeze"/>
        <rect class="tech-pill" x="0" y="0" width="105" height="30" rx="15" fill="#f8fafc" stroke="url(#signature-grad)" stroke-width="1.5"/>
        <text x="52.5" y="19" fill="#18181b" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">TypeScript</text>
      </g>

      <g transform="translate(315, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="8.1s" fill="freeze"/>
        <rect class="tech-pill" x="0" y="0" width="85" height="30" rx="15" fill="#f8fafc" stroke="#ea580c" stroke-width="1.5"/>
        <text x="42.5" y="19" fill="#ea580c" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Node.js</text>
      </g>

      <g transform="translate(410, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="8.3s" fill="freeze"/>
        <rect class="tech-pill" x="0" y="0" width="80" height="30" rx="15" fill="#f8fafc" stroke="#ea580c" stroke-width="1.5"/>
        <text x="40" y="19" fill="#ea580c" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Python</text>
      </g>

      <g transform="translate(500, 35)" opacity="0">
        <animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="8.5s" fill="freeze"/>
        <rect class="tech-pill" x="0" y="0" width="80" height="30" rx="15" fill="#f8fafc" stroke="#facc15" stroke-width="1.5"/>
        <text x="40" y="19" fill="#facc15" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">Docker</text>
      </g>
    </g>

    <!-- Animated System/Stats Bar -->
    <g transform="translate(80, 620)">
      <text x="0" y="15" fill="#27272a" font-family="monospace" font-size="12" font-weight="bold">CORE_OVERCLOCK: 99%</text>
      <rect x="150" y="5" width="200" height="12" rx="3" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
      <rect x="152" y="7" width="0" height="8" rx="2" fill="url(#signature-grad)">
        <animate attributeName="width" from="0" to="196" dur="2s" begin="5s" fill="freeze" calcMode="spline" keySplines="0.1 0.8 0.2 1"/>
      </rect>

      <text x="380" y="15" fill="#27272a" font-family="monospace" font-size="12" font-weight="bold">NEURAL_LINK: 100%</text>
      <rect x="520" y="5" width="120" height="12" rx="3" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
      <rect x="522" y="7" width="0" height="8" rx="2" fill="#ea580c">
        <animate attributeName="width" from="0" to="116" dur="2s" begin="5.5s" fill="freeze" calcMode="spline" keySplines="0.1 0.8 0.2 1"/>
      </rect>
    </g>

    <!-- RIGHT COLUMN: Code Card, Slogan sign, Character -->
    <g transform="translate(780, 50)">
      <!-- Editor Frame -->
      <rect x="0" y="0" width="450" height="240" rx="12" fill="#ffffff" stroke="#e4e4e7" stroke-width="1.5" style="filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.05));"/>
      <path d="M 0 35 H 450" stroke="#e4e4e7" stroke-width="1"/>
      <circle cx="20" cy="18" r="5" fill="#ff5f56"/>
      <circle cx="35" cy="18" r="5" fill="#ffbd2e"/>
      <circle cx="50" cy="18" r="5" fill="#27c93f"/>
      <text x="225" y="22" fill="#71717a" font-family="monospace" font-size="11" font-weight="bold" opacity="0.6" text-anchor="middle">buildDreams.jsx</text>

      <!-- Code Snippet -->
      <g transform="translate(20, 60)" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="0.2">
        <text class="code-l1" x="0" y="15" fill="#7c3aed">const <tspan fill="#ea580c">buildDreams</tspan> = <tspan fill="#18181b">() => {</tspan></text>
        <text class="code-l2" x="20" y="35" fill="#7c3aed">while <tspan fill="#18181b">(coding) {</tspan></text>
        <text class="code-l3" x="40" y="55" fill="#ea580c">coffee<tspan fill="#18181b">.consume();</tspan></text>
        <text class="code-l4" x="40" y="75" fill="#7c3aed">ideas<tspan fill="#18181b">.compile();</tspan></text>
        <text class="code-l5" x="40" y="95" fill="#facc15">dreams<tspan fill="#18181b">.deploy();</tspan></text>
        <text class="code-l6" x="20" y="115" fill="#18181b">}</text>
        <text class="code-l7" x="0" y="135" fill="#18181b">};</text>
      </g>
    </g>

    <!-- Slogan Sign: STAY SHARP. KEEP BUILDING. -->
    <g transform="translate(780, 310)">
      <rect x="0" y="0" width="450" height="70" rx="8" fill="#ffffff" stroke="#e4e4e7" stroke-width="1.5" />
      <text x="225" y="42" fill="#ea580c" font-family="monospace" font-size="18" font-weight="bold" letter-spacing="3" text-anchor="middle">STAY SHARP. KEEP BUILDING.</text>
    </g>

    <!-- Character Container -->
    <g clip-path="url(#hologram-clip)">
      <image href="data:image/png;base64,{char_b64}" x="793" y="390" width="424" height="600" />
      <rect x="780" y="390" width="450" height="350" fill="url(#grid)" opacity="0.15" pointer-events="none" />
    </g>

    <!-- Scan Line for hologram reveal -->
    <line x1="780" y1="100" x2="1230" y2="100" stroke="#7c3aed" stroke-width="3" opacity="0" filter="url(#neon-glow-filter)">
      <animate attributeName="y1" from="100" to="740" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      <animate attributeName="y2" from="100" to="740" dur="2s" begin="0.5s" fill="freeze" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.9;1" dur="2s" begin="0.5s" fill="freeze"/>
    </line>

    <!-- Continuous Scanner Line -->
    <line x1="0" y1="0" x2="1280" y2="0" stroke="#ea580c" stroke-width="2" opacity="0" style="filter: drop-shadow(0 0 4px #ea580c);">
      <animate attributeName="y1" from="0" to="740" dur="3.5s" begin="2.5s" repeatCount="indefinite" />
      <animate attributeName="y2" from="0" to="740" dur="3.5s" begin="2.5s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;0.8;0.8;0" keyTimes="0;0.1;0.9;1" dur="3.5s" begin="2.5s" repeatCount="indefinite"/>
    </line>
  </g>
</svg>"""

    banner_light_content = banner_light_template.replace("{char_b64}", char_b64).replace("{quote}", quote)
    with open("banner-light.svg", "w") as f:
      f.write(banner_light_content)
    print("banner-light.svg generated.")

    # 3. lanyard.svg (React-Bits Lanyard style - Purple/Orange Theme)
    print("Generating lanyard.svg...")
    lanyard_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="100%" height="100%" style="max-height: 550px;">
  <defs>
    <!-- Card Glassmorphism Gradient -->
    <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09090b" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#18181b" stop-opacity="0.85" />
    </linearGradient>

    <!-- Metal clasp texture -->
    <linearGradient id="metal-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8" />
      <stop offset="35%" stop-color="#cbd5e1" />
      <stop offset="50%" stop-color="#f1f5f9" />
      <stop offset="65%" stop-color="#cbd5e1" />
      <stop offset="100%" stop-color="#64748b" />
    </linearGradient>

    <!-- Purple/Orange gradient -->
    <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#ea580c" />
    </linearGradient>

    <clipPath id="avatar-clip">
      <circle cx="150" cy="180" r="60" />
    </clipPath>
  </defs>

  <style>
    <![CDATA[
    /* Physics-based Pendulum Drop and Sway Animation */
    @keyframes drop-swing {
      0% { transform: rotate(-40deg) translateY(-300px); }
      10% { transform: rotate(32deg) translateY(0); }
      20% { transform: rotate(-24deg); }
      30% { transform: rotate(18deg); }
      40% { transform: rotate(-12deg); }
      50% { transform: rotate(8deg); }
      60% { transform: rotate(-5deg); }
      70% { transform: rotate(3deg); }
      80% { transform: rotate(-1.5deg); }
      90% { transform: rotate(0.8deg); }
      100% { transform: rotate(0deg); }
    }

    @keyframes sway-loop {
      0%, 100% { transform: rotate(-1.5deg); }
      50% { transform: rotate(1.5deg); }
    }

    .swing-assembly {
      transform-origin: 500px 50px;
      animation: drop-swing 4.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) 1,
                 sway-loop 5s ease-in-out 4.5s infinite;
    }
    ]]>
  </style>

  <!-- Lanyard assembly, swings from top center -->
  <g class="swing-assembly">
    <!-- STRAP LEFT -->
    <path d="M 450 0 L 490 200" stroke="#09090b" stroke-width="26" stroke-linecap="round" />
    <path d="M 450 0 L 490 200" stroke="#7c3aed" stroke-width="12" stroke-linecap="round" stroke-dasharray="8 6" />

    <!-- STRAP RIGHT -->
    <path d="M 550 0 L 510 200" stroke="#09090b" stroke-width="26" stroke-linecap="round" />
    <path d="M 550 0 L 510 200" stroke="#7c3aed" stroke-width="12" stroke-linecap="round" stroke-dasharray="8 6" />
    
    <!-- Strap Texts -->
    <text x="450" y="80" fill="#a1a1aa" font-family="monospace" font-size="10" font-weight="bold" transform="rotate(78 450 80)" letter-spacing="1">{username_upper} // SECURE ACCESS</text>
    <text x="540" y="80" fill="#a1a1aa" font-family="monospace" font-size="10" font-weight="bold" transform="rotate(-78 540 80)" letter-spacing="1">DEVELOPER // CLASS C</text>

    <!-- Metal Ring & Clasp -->
    <polygon points="485,200 515,200 500,225" fill="url(#metal-grad)" stroke="#475569" stroke-width="1" />
    <rect x="492" y="222" width="16" height="24" rx="3" fill="url(#metal-grad)" stroke="#475569" stroke-width="1" />
    <circle cx="500" cy="234" r="3" fill="#334155" />
    <rect x="480" y="246" width="40" height="8" rx="2" fill="#09090b" />

    <!-- THE BADGE CARD (x=350, y=254, width=300, height=480) -->
    <g transform="translate(350, 254)">
      <rect x="0" y="0" width="300" height="480" rx="18" fill="url(#card-grad)" stroke="url(#neon-cyan)" stroke-width="2" style="filter: drop-shadow(0 10px 25px rgba(139, 92, 246, 0.25));" />
      
      <path d="M 0 40 H 300" stroke="#27272a" stroke-width="1" />
      <path d="M 0 440 H 300" stroke="#27272a" stroke-width="1" />
      <rect x="10" y="10" width="280" height="460" rx="12" fill="none" stroke="#ea580c" stroke-width="1" stroke-opacity="0.15" />

      <!-- Top Text -->
      <text x="150" y="28" fill="#ea580c" font-family="monospace" font-size="12" font-weight="bold" letter-spacing="2" text-anchor="middle">WORKSPACE IDENTITY</text>

      <!-- Glow Avatar Rings -->
      <circle cx="150" cy="180" r="66" fill="none" stroke="#7c3aed" stroke-width="1.5" stroke-opacity="0.3" />
      <circle cx="150" cy="180" r="63" fill="none" stroke="#ea580c" stroke-width="2" style="filter: drop-shadow(0 0 6px #ea580c);" />

      <!-- Cropped Avatar Image -->
      <image href="data:image/png;base64,{avatar_b64}" x="90" y="120" width="120" height="120" clip-path="url(#avatar-clip)" />

      <!-- Developer Info -->
      <text x="150" y="280" fill="#ffffff" font-family="monospace" font-size="20" font-weight="bold" letter-spacing="1" text-anchor="middle">{name}</text>
      <text x="150" y="305" fill="#f97316" font-family="monospace" font-size="13" font-weight="bold" letter-spacing="1" text-anchor="middle">{role_upper}</text>
      
      <rect x="50" y="325" width="200" height="24" rx="4" fill="#09090b" stroke="#27272a" stroke-width="1" />
      <text x="150" y="341" fill="#ea580c" font-family="monospace" font-size="12" text-anchor="middle">ID: @{username}</text>

      <!-- Barcode area at bottom -->
      <g transform="translate(40, 370)">
        <!-- Barcode lines -->
        <rect x="0" y="0" width="3" height="40" fill="#e4e4e7" />
        <rect x="5" y="0" width="1" height="40" fill="#e4e4e7" />
        <rect x="8" y="0" width="6" height="40" fill="#e4e4e7" />
        <rect x="16" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="20" y="0" width="4" height="40" fill="#e4e4e7" />
        <rect x="26" y="0" width="1" height="40" fill="#e4e4e7" />
        <rect x="30" y="0" width="5" height="40" fill="#e4e4e7" />
        <rect x="38" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="42" y="0" width="6" height="40" fill="#e4e4e7" />
        <rect x="50" y="0" width="1" height="40" fill="#e4e4e7" />
        <rect x="54" y="0" width="3" height="40" fill="#e4e4e7" />
        <rect x="60" y="0" width="5" height="40" fill="#e4e4e7" />
        <rect x="68" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="74" y="0" width="7" height="40" fill="#e4e4e7" />
        <rect x="83" y="0" width="1" height="40" fill="#e4e4e7" />
        <rect x="86" y="0" width="4" height="40" fill="#e4e4e7" />
        <rect x="92" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="96" y="0" width="6" height="40" fill="#e4e4e7" />
        <rect x="104" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="108" y="0" width="4" height="40" fill="#e4e4e7" />
        
        <rect x="114" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="118" y="0" width="5" height="40" fill="#e4e4e7" />
        <rect x="125" y="0" width="1" height="40" fill="#e4e4e7" />
        <rect x="128" y="0" width="6" height="40" fill="#e4e4e7" />
        <rect x="136" y="0" width="3" height="40" fill="#e4e4e7" />
        <rect x="142" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="146" y="0" width="5" height="40" fill="#e4e4e7" />
        <rect x="154" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="158" y="0" width="7" height="40" fill="#e4e4e7" />
        <rect x="167" y="0" width="1" height="40" fill="#e4e4e7" />
        <rect x="170" y="0" width="3" height="40" fill="#e4e4e7" />
        <rect x="175" y="0" width="5" height="40" fill="#e4e4e7" />
        <rect x="182" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="186" y="0" width="6" height="40" fill="#e4e4e7" />
        <rect x="194" y="0" width="1" height="40" fill="#e4e4e7" />
        <rect x="198" y="0" width="3" height="40" fill="#e4e4e7" />
        <rect x="204" y="0" width="6" height="40" fill="#e4e4e7" />
        <rect x="212" y="0" width="2" height="40" fill="#e4e4e7" />
        <rect x="216" y="0" width="4" height="40" fill="#e4e4e7" />

        <text x="110" y="52" fill="#7c3aed" font-family="monospace" font-size="9" font-weight="bold" letter-spacing="2" text-anchor="middle">LEVEL_C_AUTHENTIC_ID</text>
      </g>
    </g>
  </g>
</svg>"""

    lanyard_content = lanyard_template.replace("{avatar_b64}", avatar_b64).replace("{name}", name).replace("{role_upper}", role.upper()).replace("{username}", username).replace("{username_upper}", username.upper())
    with open("lanyard.svg", "w") as f:
      f.write(lanyard_content)
    print("lanyard.svg generated.")

    # 4. stats.svg (Local Stats Card - Purple/Orange Theme)
    print("Generating stats.svg...")
    stats_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 200" width="450" height="200">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09090b" />
      <stop offset="100%" stop-color="#18181b" />
    </linearGradient>
    <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#ea580c" />
    </linearGradient>
  </defs>

  <style>
    <![CDATA[
    @keyframes rotate-dashed {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    .rotating-ring {
      transform-origin: 75px 100px;
      animation: rotate-dashed 20s linear infinite;
    }
    @keyframes slide-row {
      from { transform: translateX(-30px); opacity: 0; }
      to { transform: translateX(0); opacity: 1; }
    }
    .row-anim { animation: slide-row 0.6s ease-out forwards; opacity: 0; }
    
    @keyframes pulse {
      0%, 100% { filter: drop-shadow(0 0 2px #ea580c); }
      50% { filter: drop-shadow(0 0 8px #ea580c); }
    }
    .glow-pulse {
      animation: pulse 3s infinite;
    }
    ]]>
  </style>

  <!-- Frame -->
  <rect width="450" height="200" rx="12" fill="url(#grad)" stroke="#27272a" stroke-width="1.5" style="filter: drop-shadow(0 4px 10px rgba(0,0,0,0.3));" />
  
  <!-- Left Side: Power Ring -->
  <g class="glow-pulse">
    <circle cx="75" cy="100" r="48" fill="none" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="6 6" class="rotating-ring" />
    <circle cx="75" cy="100" r="42" fill="#0c0c0e" stroke="#ea580c" stroke-width="2" style="filter: drop-shadow(0 0 4px #ea580c);" />
    <text x="75" y="108" fill="#ea580c" font-family="monospace" font-size="28" font-weight="bold" text-anchor="middle" style="filter: drop-shadow(0 0 3px #ea580c);">S</text>
  </g>
  <text x="75" y="165" fill="#ea580c" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle" letter-spacing="1">DEV RANK</text>

  <!-- Right Side: Stats Rows -->
  <g transform="translate(150, 20)">
    <text x="10" y="20" fill="#ea580c" font-family="monospace" font-size="14" font-weight="bold">// SYSTEM STATS</text>
    <line x1="10" y1="28" x2="270" y2="28" stroke="#27272a" stroke-width="1" />
    
    <!-- Row 1 -->
    <g transform="translate(10, 45)">
      <g class="row-anim" style="animation-delay: 0.2s;">
        <text x="0" y="12" fill="#e2e8f0" font-family="monospace" font-size="12">Total Commits</text>
        <text x="260" y="12" fill="#ea580c" font-family="monospace" font-size="13" font-weight="bold" text-anchor="end">1,420</text>
        <rect x="0" y="20" width="260" height="4" rx="2" fill="#18181b" />
        <rect x="0" y="20" width="230" height="4" rx="2" fill="url(#neon-cyan)" />
      </g>
    </g>

    <!-- Row 2 -->
    <g transform="translate(10, 80)">
      <g class="row-anim" style="animation-delay: 0.4s;">
        <text x="0" y="12" fill="#e2e8f0" font-family="monospace" font-size="12">Pull Requests</text>
        <text x="260" y="12" fill="#ea580c" font-family="monospace" font-size="13" font-weight="bold" text-anchor="end">184</text>
        <rect x="0" y="20" width="260" height="4" rx="2" fill="#18181b" />
        <rect x="0" y="20" width="190" height="4" rx="2" fill="url(#neon-cyan)" />
      </g>
    </g>

    <!-- Row 3 -->
    <g transform="translate(10, 115)">
      <g class="row-anim" style="animation-delay: 0.6s;">
        <text x="0" y="12" fill="#e2e8f0" font-family="monospace" font-size="12">Issues Closed</text>
        <text x="260" y="12" fill="#ea580c" font-family="monospace" font-size="13" font-weight="bold" text-anchor="end">56</text>
        <rect x="0" y="20" width="260" height="4" rx="2" fill="#18181b" />
        <rect x="0" y="20" width="150" height="4" rx="2" fill="url(#neon-cyan)" />
      </g>
    </g>

    <!-- Row 4 -->
    <g transform="translate(10, 150)">
      <g class="row-anim" style="animation-delay: 0.8s;">
        <text x="0" y="12" fill="#e2e8f0" font-family="monospace" font-size="12">Stars Earned</text>
        <text x="260" y="12" fill="#ea580c" font-family="monospace" font-size="13" font-weight="bold" text-anchor="end">92</text>
        <rect x="0" y="20" width="260" height="4" rx="2" fill="#18181b" />
        <rect x="0" y="20" width="175" height="4" rx="2" fill="url(#neon-cyan)" />
      </g>
    </g>
  </g>
</svg>
"""
    with open("stats.svg", "w") as f:
      f.write(stats_content)
    print("stats.svg generated.")

    # 5. langs.svg (Local Langs Card - Purple/Orange Theme)
    print("Generating langs.svg...")
    langs_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 200" width="450" height="200">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09090b" />
      <stop offset="100%" stop-color="#18181b" />
    </linearGradient>
    <linearGradient id="bar-ts" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>
    <linearGradient id="bar-js" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ea580c" />
      <stop offset="100%" stop-color="#ffedd5" />
    </linearGradient>
    <linearGradient id="bar-py" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#fef3c7" />
    </linearGradient>
    <linearGradient id="bar-html" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#db2777" />
      <stop offset="100%" stop-color="#fbcfe8" />
    </linearGradient>
  </defs>

  <style>
    <![CDATA[
    @keyframes load-bar {
      from { width: 0; }
    }
    .fill-bar {
      animation: load-bar 1.2s cubic-bezier(0.1, 0.8, 0.2, 1) forwards;
    }
    ]]>
  </style>

  <!-- Frame -->
  <rect width="450" height="200" rx="12" fill="url(#grad)" stroke="#ea580c" stroke-width="1.5" stroke-opacity="0.6" style="filter: drop-shadow(0 4px 10px rgba(234,88,12,0.08));" />
  
  <text x="25" y="30" fill="#ea580c" font-family="monospace" font-size="14" font-weight="bold">// LANGUAGE PROFILE</text>
  <line x1="20" y1="38" x2="430" y2="38" stroke="#27272a" stroke-width="1" />

  <g transform="translate(25, 50)" font-family="monospace" font-size="12" fill="#e2e8f0">
    <!-- TS -->
    <text x="0" y="15">TypeScript</text>
    <rect x="110" y="5" width="250" height="10" rx="5" fill="#18181b" />
    <rect class="fill-bar" x="110" y="5" width="212" height="10" rx="5" fill="url(#bar-ts)" />
    <text x="375" y="15" fill="#7c3aed" font-weight="bold">85%</text>

    <!-- JS (React/Next) -->
    <g transform="translate(0, 32)">
      <text x="0" y="15">React/JS</text>
      <rect x="110" y="5" width="250" height="10" rx="5" fill="#18181b" />
      <rect class="fill-bar" x="110" y="5" width="195" height="10" rx="5" fill="url(#bar-js)" />
      <text x="375" y="15" fill="#ea580c" font-weight="bold">78%</text>
    </g>

    <!-- Python -->
    <g transform="translate(0, 64)">
      <text x="0" y="15">Python</text>
      <rect x="110" y="5" width="250" height="10" rx="5" fill="#18181b" />
      <rect class="fill-bar" x="110" y="5" width="175" height="10" rx="5" fill="url(#bar-py)" />
      <text x="375" y="15" fill="#f59e0b" font-weight="bold">70%</text>
    </g>

    <!-- HTML/CSS -->
    <g transform="translate(0, 96)">
      <text x="0" y="15">UI/CSS/HTML</text>
      <rect x="110" y="5" width="250" height="10" rx="5" fill="#18181b" />
      <rect class="fill-bar" x="110" y="5" width="187" height="10" rx="5" fill="url(#bar-html)" />
      <text x="375" y="15" fill="#db2777" font-weight="bold">75%</text>
    </g>
  </g>
</svg>
"""
    with open("langs.svg", "w") as f:
      f.write(langs_content)
    print("langs.svg generated.")

    # 6. trophies.svg (Local Trophies Card - Purple/Orange Theme)
    print("Generating trophies.svg...")
    trophies_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 200" width="450" height="200">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#09090b" />
      <stop offset="100%" stop-color="#18181b" />
    </linearGradient>
  </defs>

  <style>
    <![CDATA[
    @keyframes cell-pop {
      from { transform: scale(0.85); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }
    .trophy-anim { animation: cell-pop 0.5s ease-out forwards; opacity: 0; }
    ]]>
  </style>

  <!-- Frame -->
  <rect width="450" height="200" rx="12" fill="url(#grad)" stroke="#ea580c" stroke-width="1.5" stroke-opacity="0.6" style="filter: drop-shadow(0 4px 10px rgba(234,88,12,0.1));" />
  
  <text x="25" y="30" fill="#ea580c" font-family="monospace" font-size="14" font-weight="bold">// SYSTEM TROPHIES</text>
  <line x1="20" y1="38" x2="430" y2="38" stroke="#27272a" stroke-width="1" />

  <!-- Cell 1 -->
  <g transform="translate(20, 52)">
    <g class="trophy-anim" style="animation-delay: 0.2s; transform-origin: 60px 57px;">
      <rect width="120" height="115" rx="8" fill="#18181b" stroke="#7c3aed" stroke-width="1.2" stroke-opacity="0.4" />
      <path d="M 0 10 V 0 H 10 M 110 0 H 120 V 10 M 120 105 V 115 H 110 M 10 115 H 0 V 105" fill="none" stroke="#7c3aed" stroke-width="1.5" />
      
      <!-- Trophy Icon -->
      <path d="M 60 20 L 75 35 H 85 V 50 H 60 H 35 V 35 H 45 Z M 57 50 V 68 H 50 V 74 H 70 V 68 H 63 V 50 Z" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 3px #7c3aed);" />
      <text x="60" y="92" fill="#7c3aed" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">CODE WARRIOR</text>
      <text x="60" y="105" fill="#cbd5e1" font-family="monospace" font-size="9" text-anchor="middle">A-RANK</text>
    </g>
  </g>

  <!-- Cell 2 -->
  <g transform="translate(165, 52)">
    <g class="trophy-anim" style="animation-delay: 0.4s; transform-origin: 60px 57px;">
      <rect width="120" height="115" rx="8" fill="#18181b" stroke="#ea580c" stroke-width="1.2" stroke-opacity="0.4" />
      <path d="M 0 10 V 0 H 10 M 110 0 H 120 V 10 M 120 105 V 115 H 110 M 10 115 H 0 V 105" fill="none" stroke="#ea580c" stroke-width="1.5" />
      
      <path d="M 50 25 H 70 L 75 42 L 60 52 L 45 42 Z M 60 52 V 68 H 50 V 74 H 70 V 68 H 60 Z" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 3px #ea580c);" />
      <text x="60" y="92" fill="#ea580c" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">PR CHAMPION</text>
      <text x="60" y="105" fill="#cbd5e1" font-family="monospace" font-size="9" text-anchor="middle">S-RANK</text>
    </g>
  </g>

  <!-- Cell 3 -->
  <g transform="translate(310, 52)">
    <g class="trophy-anim" style="animation-delay: 0.6s; transform-origin: 60px 57px;">
      <rect width="120" height="115" rx="8" fill="#18181b" stroke="#facc15" stroke-width="1.2" stroke-opacity="0.4" />
      <path d="M 0 10 V 0 H 10 M 110 0 H 120 V 10 M 120 105 V 115 H 110 M 10 115 H 0 V 105" fill="none" stroke="#facc15" stroke-width="1.5" />
      
      <circle cx="60" cy="40" r="16" fill="none" stroke="#facc15" stroke-width="2" style="filter: drop-shadow(0 0 3px #facc15);" />
      <path d="M 54 40 H 66 M 60 34 V 46" stroke="#facc15" stroke-width="2" stroke-linecap="round" />
      <text x="60" y="92" fill="#facc15" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">BUG HUNTER</text>
      <text x="60" y="105" fill="#cbd5e1" font-family="monospace" font-size="9" text-anchor="middle">A-RANK</text>
    </g>
  </g>
</svg>
"""
    with open("trophies.svg", "w") as f:
      f.write(trophies_content)
    print("trophies.svg generated.")

    # 7. github-snake.yml (GitHub Action Workflow with permissions fix and Halloween theme)
    print("Generating github-snake.yml...")
    os.makedirs(".github/workflows", exist_ok=True)
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
    print(".github/workflows/github-snake.yml generated.")

    # 8. README.md (Purple & Orange themed)
    print("Generating README.md...")
    readme_template = """<h1 align="center">ACCESS SYSTEM // {name_upper}</h1>

<p align="center">
  <!-- Auto-switching preferences banner using HTML picture element -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="banner.svg?v=2">
    <source media="(prefers-color-scheme: light)" srcset="banner-light.svg?v=2">
    <img alt="Cyberpunk Developer Banner" src="banner.svg?v=2" width="100%">
  </picture>
</p>

---

<table align="center" border="0" cellpadding="10" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto;">
  <tr style="border: 0px;">
    <!-- Swinging Badge Lanyard -->
    <td align="center" valign="top" style="border: 0px; padding: 20px; width: 45%;">
      <img src="lanyard.svg?v=2" alt="Developer ID Lanyard" width="100%" style="max-width: 320px;">
    </td>
    <!-- Bio / System Terminal Details -->
    <td valign="top" style="border: 0px; padding: 20px; width: 55%; font-family: monospace; color: #cbd5e1;">
      <h3>SYSTEM_PROFILE.bin</h3>
      <p><b>&gt; IDENTITY:</b> {name} / @{username}</p>
      <p><b>&gt; COGNITIVE_ROLE:</b> {role}</p>
      <p><b>&gt; ACCESS_PORT:</b> <a href="mailto:{email}">{email}</a></p>
      <p><b>&gt; MISSION_TAGLINE:</b> <code>{tagline}</code></p>
      <hr style="border-color: #ea580c; opacity: 0.3;">
      <h4>CORE_SKILLS:</h4>
      <p>
        {skills_html}
      </p>
      <p>
        Welcome to my digital terminal. I specialize in building responsive, high-performance web applications with clean architecture and interactive cyberpunk visual systems. Feel free to explore my source nodes below.
      </p>
    </td>
  </tr>
</table>

---

<h2 align="center">SYSTEM PERFORMANCE CARDS</h2>

<p align="center">
  <img src="stats.svg?v=2" alt="GitHub System Stats" width="48%" style="max-width: 440px; margin-right: 15px;">
  <img src="langs.svg?v=2" alt="Language Distribution" width="48%" style="max-width: 440px;">
</p>
<p align="center">
  <img src="trophies.svg?v=2" alt="System Achievement Trophies" width="98%" style="max-width: 900px; margin-top: 15px;">
</p>

---

<h2 align="center">PROJECT NODES</h2>

<table align="center" style="width: 100%; border-collapse: collapse; text-align: left; font-family: monospace; border: 1px solid #ea580c;">
  <thead>
    <tr style="background-color: #0c0c0e; color: #ea580c; border-bottom: 2px solid #ea580c;">
      <th style="padding: 12px; border: 1px solid #ea580c;">Node Name</th>
      <th style="padding: 12px; border: 1px solid #ea580c;">Operational Parameters</th>
      <th style="padding: 12px; border: 1px solid #ea580c;">Tech Spec</th>
      <th style="padding: 12px; border: 1px solid #ea580c;">Status Link</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid rgba(234, 88, 12, 0.2);">
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2); font-weight: bold;">🌌 cyber-dashboard</td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);">Futuristic network operations center dashboard in the browser.</td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);"><code>React</code> <code>Three.js</code> <code>Tailwind</code></td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);"><a href="https://github.com/{username}/cyber-dashboard">Deploy Node &gt;</a></td>
    </tr>
    <tr style="border-bottom: 1px solid rgba(234, 88, 12, 0.2);">
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2); font-weight: bold;">🛡️ sentinel-auth</td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);">Decentralized cryptographically secure authenticator system.</td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);"><code>Node.js</code> <code>TypeScript</code> <code>ECDSA</code></td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);"><a href="https://github.com/{username}/sentinel-auth">Deploy Node &gt;</a></td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2); font-weight: bold;">🔮 neural-mesh</td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);">Serverless neural network text analyzer and content summarizer.</td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);"><code>Python</code> <code>Next.js</code> <code>PyTorch</code></td>
      <td style="padding: 12px; border: 1px solid rgba(234, 88, 12, 0.2);"><a href="https://github.com/{username}/neural-mesh">Deploy Node &gt;</a></td>
    </tr>
  </tbody>
</table>

---

<h2 align="center">CONTRIBUTION GRID MESH</h2>

<p align="center">
  <!-- GitHub snake contribution graph generated from workflow -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg?v=2">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake-light.svg?v=2">
    <img alt="GitHub Snake Game" src="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg?v=2" width="100%">
  </picture>
</p>

---

<h3 align="center">CONNECT_PORTALS</h3>
<p align="center">
  <a href="https://github.com/{username}">
    <img src="https://img.shields.io/badge/GitHub-101000?style=for-the-badge&logo=github&logoColor=a855f7&labelColor=09090b&borderColor=a855f7" alt="GitHub Portal">
  </a>
  <a href="mailto:{email}">
    <img src="https://img.shields.io/badge/Email-101000?style=for-the-badge&logo=gmail&logoColor=ea580c&labelColor=09090b&borderColor=ea580c" alt="Email Direct">
  </a>
  <a href="https://linkedin.com/in/{username}">
    <img src="https://img.shields.io/badge/LinkedIn-101000?style=for-the-badge&logo=linkedin&logoColor=facc15&labelColor=09090b&borderColor=facc15" alt="LinkedIn Node">
  </a>
</p>

<p align="center" style="font-family: monospace; color: #71717a; font-size: 11px;">
  SYSTEM PROFILE VISITS: <img src="https://profile-counter.glitch.me/{username}/count.svg" alt="Views Counter" style="vertical-align: middle;"> // SECURE CONNECTIONS COMPLETED
</p>"""

    readme_content = readme_template.replace("{name}", name).replace("{name_upper}", name.upper()).replace("{username}", username).replace("{email}", email).replace("{role}", role).replace("{tagline}", tagline).replace("{skills_html}", skills_html)
    with open("README.md", "w") as f:
      f.write(readme_content)
    print("README.md generated.")
    print("All profile assets generated successfully!")

if __name__ == "__main__":
    main()
