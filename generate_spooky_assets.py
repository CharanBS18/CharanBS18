import os
import math
from PIL import Image, ImageDraw

# Create directories
def setup_dirs():
    dirs = [
        "halloween",
        "halloween/animations",
        "halloween/illustrations",
        "halloween/dividers",
        "halloween/headers",
        "halloween/icons",
        "halloween/frames",
        "halloween/badges",
        "halloween/backgrounds",
        "halloween/decorations"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("Directories initialized successfully.")

# Helper to save transparent GIFs in Pillow
def save_transparent_gif(frames, filename, duration=100):
    palette_frames = []
    for img in frames:
        alpha = img.split()[3]
        img_rgb = img.convert('RGB')
        img_p = img_rgb.quantize(colors=255)
        
        # Paste the transparent index (255) wherever alpha was transparent (0)
        mask = alpha.point(lambda x: 255 if x == 0 else 0)
        img_p.paste(255, mask)
        img_p.info['transparency'] = 255
        palette_frames.append(img_p)
        
    palette_frames[0].save(
        filename,
        save_all=True,
        append_images=palette_frames[1:],
        duration=duration,
        loop=0,
        disposal=2  # Clear previous frame
    )
    print(f"Generated {filename}")

# Generate Animated GIFs
def generate_gifs():
    print("Generating animated GIFs...")
    
    # 1. flying_bats.gif
    bat_frames = []
    for i in range(10):
        img = Image.new("RGBA", (120, 80), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # Bat wing swing factor
        swing = math.sin(2 * math.pi * i / 10)
        # Draw body
        draw.ellipse([54, 35, 66, 45], fill=(13, 17, 23))  # Head
        draw.polygon([(52, 38), (56, 32), (58, 38)], fill=(13, 17, 23))  # Ear L
        draw.polygon([(62, 38), (64, 32), (68, 38)], fill=(13, 17, 23))  # Ear R
        draw.ellipse([48, 42, 72, 60], fill=(36, 0, 70))  # Body
        
        # Draw wings
        # L Wing
        wing_l = [(48, 46), (15, 30 + int(20 * swing)), (35, 52), (48, 52)]
        draw.polygon(wing_l, fill=(138, 43, 226) if i % 2 == 0 else (13, 17, 23))
        # R Wing
        wing_r = [(72, 46), (105, 30 + int(20 * swing)), (85, 52), (72, 52)]
        draw.polygon(wing_r, fill=(138, 43, 226) if i % 2 == 0 else (13, 17, 23))
        
        # Eyes (glowing yellow)
        draw.ellipse([57, 40, 59, 42], fill=(255, 209, 102))
        draw.ellipse([61, 40, 63, 42], fill=(255, 209, 102))
        bat_frames.append(img)
    save_transparent_gif(bat_frames, "halloween/animations/flying_bats.gif", duration=80)

    # 2. floating_ghost.gif
    ghost_frames = []
    for i in range(15):
        img = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        y_off = int(8 * math.sin(2 * math.pi * i / 15))
        
        # Draw ghost body shape
        draw.ellipse([30, 20 + y_off, 70, 60 + y_off], fill=(248, 249, 250))
        draw.rectangle([30, 45 + y_off, 70, 75 + y_off], fill=(248, 249, 250))
        
        # Wavy bottom tail
        wave = int(4 * math.sin(2 * math.pi * (i / 15 + 0.25)))
        draw.ellipse([27, 70 + y_off + wave, 42, 80 + y_off + wave], fill=(248, 249, 250))
        draw.ellipse([43, 70 + y_off - wave, 57, 80 + y_off - wave], fill=(248, 249, 250))
        draw.ellipse([58, 70 + y_off + wave, 73, 80 + y_off + wave], fill=(248, 249, 250))
        
        # Arms
        draw.ellipse([20, 40 + y_off, 34, 52 + y_off], fill=(248, 249, 250))
        draw.ellipse([66, 40 + y_off, 80, 52 + y_off], fill=(248, 249, 250))
        
        # Spooky glowing purple eyes
        draw.ellipse([42, 38 + y_off, 47, 46 + y_off], fill=(90, 24, 154))
        draw.ellipse([53, 38 + y_off, 58, 46 + y_off], fill=(90, 24, 154))
        draw.ellipse([46, 52 + y_off, 54, 58 + y_off], fill=(90, 24, 154))  # Mouth
        
        ghost_frames.append(img)
    save_transparent_gif(ghost_frames, "halloween/animations/floating_ghost.gif", duration=100)

    # 3. candle_flicker.gif
    candle_frames = []
    for i in range(12):
        img = Image.new("RGBA", (80, 120), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # Melted candle stick
        draw.rectangle([30, 50, 50, 110], fill=(255, 209, 102))
        draw.ellipse([30, 45, 50, 55], fill=(232, 93, 4))  # top surface
        
        # Wax drips
        draw.ellipse([32, 53, 36, 75], fill=(255, 209, 102))
        draw.ellipse([44, 53, 48, 85], fill=(255, 209, 102))
        
        # Wick
        draw.line([(40, 48), (40, 40)], fill=(13, 17, 23), width=2)
        
        # Flickering flame
        flame_w = 12 + int(3 * math.sin(2 * math.pi * i / 6))
        flame_h = 24 + int(4 * math.cos(2 * math.pi * i / 4))
        flicker_x = int(3 * math.sin(2 * math.pi * i / 3))
        
        # Draw outer flame (orange)
        draw.polygon([
            (40 + flicker_x, 40 - flame_h), 
            (40 - flame_w // 2, 40), 
            (40 + flame_w // 2, 40)
        ], fill=(255, 117, 24))
        
        # Draw inner flame (yellow)
        draw.polygon([
            (40 + flicker_x // 2, 40 - int(flame_h * 0.7)), 
            (40 - int(flame_w * 0.3), 40), 
            (40 + int(flame_w * 0.3), 40)
        ], fill=(255, 209, 102))
        
        candle_frames.append(img)
    save_transparent_gif(candle_frames, "halloween/animations/candle_flicker.gif", duration=90)

    # 4. moving_fog.gif
    fog_frames = []
    for i in range(20):
        img = Image.new("RGBA", (300, 80), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        offset = (i * 15) % 300
        
        # Draw two layers of transparent fog waves
        for layer, color, opacity in [(0, (90, 24, 154, 40), 8), (1, (248, 249, 250, 30), 12)]:
            pts = []
            for x in range(0, 301, 20):
                wave_y = 40 + layer * 10 + int(10 * math.sin(2 * math.pi * (x + offset * (layer + 1)) / 150))
                pts.append((x, wave_y))
            pts.append((300, 80))
            pts.append((0, 80))
            draw.polygon(pts, fill=color)
        fog_frames.append(img)
    save_transparent_gif(fog_frames, "halloween/animations/moving_fog.gif", duration=120)

    # 5. falling_leaves.gif
    leaf_frames = []
    for i in range(20):
        img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Leaf 1 (Orange)
        y1 = (i * 6) % 120
        x1 = 30 + int(15 * math.sin(2 * math.pi * i / 10))
        # Draw a leaf shape
        draw.ellipse([x1 - 10, y1 - 5, x1 + 10, y1 + 5], fill=(255, 117, 24))
        draw.line([(x1 - 12, y1), (x1 + 12, y1)], fill=(232, 93, 4), width=1)
        
        # Leaf 2 (Burnt Purple)
        y2 = ((i * 5) + 60) % 120
        x2 = 80 + int(12 * math.cos(2 * math.pi * i / 12))
        draw.ellipse([x2 - 8, y2 - 6, x2 + 8, y2 + 6], fill=(90, 24, 154))
        draw.line([(x2 - 10, y2), (x2 + 10, y2)], fill=(36, 0, 70), width=1)
        
        leaf_frames.append(img)
    save_transparent_gif(leaf_frames, "halloween/animations/falling_leaves.gif", duration=100)

    # 6. twinkling_stars.gif
    star_frames = []
    for i in range(10):
        img = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Twinkling stars at fixed positions with pulsing size
        stars = [(20, 25), (60, 15), (45, 55), (15, 60)]
        for idx, (x, y) in enumerate(stars):
            pulse = math.sin(2 * math.pi * (i / 10 + idx / 4))
            size = 4 + int(5 * (pulse + 1.0) / 2.0)
            # Draw 4-point star
            draw.line([(x - size, y), (x + size, y)], fill=(255, 209, 102), width=2)
            draw.line([(x, y - size), (x, y + size)], fill=(255, 209, 102), width=2)
            # Center core
            draw.ellipse([x-2, y-2, x+2, y+2], fill=(248, 249, 250))
            
        star_frames.append(img)
    save_transparent_gif(star_frames, "halloween/animations/twinkling_stars.gif", duration=120)

    # 7. magic_particles.gif
    particle_frames = []
    particles = [
        {"x": 20, "y": 80, "speed": 4, "color": (57, 255, 20)},     # neon green
        {"x": 40, "y": 60, "speed": 3, "color": (255, 117, 24)},    # orange
        {"x": 60, "y": 90, "speed": 5, "color": (255, 209, 102)},   # yellow
        {"x": 80, "y": 70, "speed": 3, "color": (127, 255, 0)},     # haunted green
        {"x": 50, "y": 40, "speed": 4, "color": (90, 24, 154)}      # deep purple
    ]
    for i in range(15):
        img = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        for p in particles:
            cur_y = (p["y"] - i * p["speed"]) % 100
            cur_x = p["x"] + int(6 * math.sin(2 * math.pi * (i / 15 + p["x"] / 100)))
            size = max(1, int(4 * (cur_y / 100.0)))  # shrinks as it rises
            alpha = int(255 * (cur_y / 100.0))
            draw.ellipse([cur_x - size, cur_y - size, cur_x + size, cur_y + size], fill=p["color"] + (alpha,))
            
        particle_frames.append(img)
    save_transparent_gif(particle_frames, "halloween/animations/magic_particles.gif", duration=90)

    # 8. pumpkin_glow.gif
    pumpkin_frames = []
    for i in range(12):
        img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Pulse factor for glow
        glow_factor = (math.sin(2 * math.pi * i / 12) + 1.0) / 2.0
        glow_color = (255, 117 + int(92 * glow_factor), 24 + int(140 * glow_factor))
        
        # Pumpkin Body (Orange)
        draw.ellipse([20, 30, 100, 100], fill=(232, 93, 4))
        draw.ellipse([35, 30, 85, 100], fill=(255, 117, 24))
        draw.ellipse([48, 30, 72, 100], fill=(255, 150, 50))
        # Stem
        draw.polygon([(56, 30), (64, 30), (60, 15)], fill=(36, 0, 70))
        
        # Eyes
        draw.polygon([(40, 55), (48, 50), (46, 65)], fill=glow_color)
        draw.polygon([(80, 55), (72, 50), (74, 65)], fill=glow_color)
        
        # Nose
        draw.polygon([(60, 68), (56, 75), (64, 75)], fill=glow_color)
        
        # Mouth
        draw.polygon([
            (38, 80), (48, 88), (54, 82), (60, 90), (66, 82), (72, 88), (82, 80),
            (74, 94), (66, 90), (60, 96), (54, 90), (46, 94)
        ], fill=glow_color)
        
        pumpkin_frames.append(img)
    save_transparent_gif(pumpkin_frames, "halloween/animations/pumpkin_glow.gif", duration=100)

    # 9. typing_terminal.gif
    term_frames = []
    full_text = "cat user.json && hack --spooky"
    for i in range(20):
        img = Image.new("RGBA", (260, 80), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # Background
        draw.rectangle([5, 5, 255, 75], fill=(13, 17, 23), outline=(90, 24, 154), width=2)
        # Header dots
        draw.ellipse([12, 12, 16, 16], fill=(255, 95, 86))
        draw.ellipse([20, 12, 24, 16], fill=(255, 189, 46))
        draw.ellipse([28, 12, 32, 16], fill=(39, 201, 63))
        
        # Text typing
        char_count = int(len(full_text) * (i / 16.0))
        char_count = min(char_count, len(full_text))
        disp_text = full_text[:char_count]
        
        # Draw terminal text prompt
        draw.text((15, 30), "ghost@spooky:~$", fill=(57, 255, 20))
        draw.text((120, 30), disp_text, fill=(248, 249, 250))
        
        # Cursor
        if i % 2 == 0:
            cursor_x = 120 + len(disp_text) * 6
            draw.rectangle([cursor_x, 30, cursor_x + 6, 42], fill=(255, 117, 24))
            
        term_frames.append(img)
    save_transparent_gif(term_frames, "halloween/animations/typing_terminal.gif", duration=150)

    # 10. floating_witch_hat.gif
    hat_frames = []
    for i in range(15):
        img = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        y_off = int(6 * math.sin(2 * math.pi * i / 15))
        
        # Brim
        draw.ellipse([15, 65 + y_off, 85, 78 + y_off], fill=(36, 0, 70))
        # Cone
        draw.polygon([
            (50, 20 + y_off), 
            (32, 68 + y_off), 
            (68, 68 + y_off)
        ], fill=(90, 24, 154))
        # Ribbon
        draw.ellipse([30, 64 + y_off, 70, 71 + y_off], fill=(255, 117, 24))
        # Gold Buckle
        draw.rectangle([45, 62 + y_off, 55, 70 + y_off], fill=(255, 209, 102), outline=(13, 17, 23))
        
        hat_frames.append(img)
    save_transparent_gif(hat_frames, "halloween/animations/floating_witch_hat.gif", duration=100)


# Generate SVGs
def generate_svgs():
    print("Generating SVG Assets...")
    
    # 1. Main Premium Banner (halloween/banner.svg)
    banner_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 600" width="1280" height="600">
  <defs>
    <!-- Background Space Gradient -->
    <radialGradient id="space-grad" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#240046" />
      <stop offset="60%" stop-color="#0f021f" />
      <stop offset="100%" stop-color="#0d1117" />
    </radialGradient>
    
    <!-- Moon Glow Filter -->
    <filter id="moon-glow-effect" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Cauldron Glow -->
    <radialGradient id="cauldron-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#39ff14" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <style>
    .title-text {
      font-family: 'Creepster', 'Luminari', 'Chiller', 'Impact', 'Arial Black', sans-serif;
      font-size: 58px;
      fill: #ff7518;
      letter-spacing: 4px;
      filter: drop-shadow(0 0 8px #e85d04);
    }
    
    .body-text {
      font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 18px;
      fill: #f8f9fa;
      opacity: 0.9;
    }

    .neon-text {
      fill: #39ff14;
      font-weight: bold;
      filter: drop-shadow(0 0 5px #39ff14);
    }

    /* Keyframe Animations */
    @keyframes float-ghost {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-12px) rotate(1deg); }
    }
    @keyframes float-hat {
      0%, 100% { transform: translateY(0px) rotate(-1deg); }
      50% { transform: translateY(-8px) rotate(1deg); }
    }
    @keyframes flap-wings {
      0%, 100% { transform: scaleY(1); }
      50% { transform: scaleY(0.4); }
    }
    @keyframes drift-clouds {
      0% { transform: translateX(0px); }
      100% { transform: translateX(-400px); }
    }
    @keyframes flicker-lantern {
      0%, 100% { fill: #ffd166; filter: drop-shadow(0 0 8px #ff7518); }
      50% { fill: #e85d04; filter: drop-shadow(0 0 2px #e85d04); }
    }

    .animated-ghost { animation: float-ghost 4s ease-in-out infinite; }
    .animated-hat { animation: float-hat 3.5s ease-in-out infinite; }
    .bat-wing { animation: flap-wings 0.3s ease-in-out infinite; transform-origin: center; }
    .ambient-clouds { animation: drift-clouds 45s linear infinite; }
    .lantern-eye { animation: flicker-lantern 0.25s infinite; }
  </style>

  <!-- Sky background -->
  <rect width="1280" height="600" rx="16" fill="url(#space-grad)"/>

  <!-- Stars -->
  <g fill="#f8f9fa">
    <circle cx="120" cy="80" r="1.5" opacity="0.6"/>
    <circle cx="340" cy="120" r="2" opacity="0.9"/>
    <circle cx="560" cy="70" r="1" opacity="0.4"/>
    <circle cx="890" cy="140" r="1.5" opacity="0.7"/>
    <circle cx="1020" cy="90" r="2.5" opacity="0.8"/>
  </g>

  <!-- Large Crescent Moon -->
  <g transform="translate(1050, 60)">
    <circle cx="50" cy="50" r="80" fill="#ffd166" filter="url(#moon-glow-effect)"/>
    <circle cx="20" cy="50" r="80" fill="#240046" />
  </g>

  <!-- Parallax drifting clouds -->
  <g class="ambient-clouds" opacity="0.25">
    <path d="M 100 200 C 180 180, 260 220, 320 200 C 380 180, 480 230, 540 210 L 1700 210 L 1700 600 Z" fill="#5a189a"/>
    <path d="M -100 300 C 20 280, 180 340, 260 300 C 380 280, 580 350, 680 300 L 1700 300 L 1700 600 Z" fill="#0d1117"/>
  </g>

  <!-- Hand-drawn Twisted Tree L -->
  <path d="M 0 600 C 80 500, 60 380, 120 300 C 140 280, 180 290, 210 270 M 120 300 C 90 280, 60 250, 30 260 M 70 410 C 150 360, 200 370, 220 340" fill="none" stroke="#0d1117" stroke-width="12" stroke-linecap="round"/>
  <!-- Hand-drawn Twisted Tree R -->
  <path d="M 1280 600 C 1200 500, 1220 400, 1160 320 C 1120 300, 1080 320, 1040 290 M 1160 320 C 1190 290, 1210 260, 1230 270" fill="none" stroke="#0d1117" stroke-width="12" stroke-linecap="round"/>

  <!-- Left: Developer Cauldron Station -->
  <g transform="translate(100, 120)">
    <!-- Cauldron Glow -->
    <circle cx="160" cy="300" r="180" fill="url(#cauldron-glow)"/>
    
    <!-- Cauldron Body -->
    <path d="M 80 360 C 80 460, 240 460, 240 360 C 240 330, 80 330, 80 360 Z" fill="#1c1c1c" stroke="#5a189a" stroke-width="4"/>
    <ellipse cx="160" cy="335" rx="76" ry="14" fill="#240046" stroke="#5a189a" stroke-width="3"/>
    
    <!-- Bubbling Green Potion inside -->
    <ellipse cx="160" cy="335" rx="70" ry="10" fill="#39ff14"/>
    
    <!-- Glowing eyes from cauldron base -->
    <polygon points="120,400 130,395 125,405" fill="#39ff14" />
    <polygon points="200,400 190,395 195,405" fill="#39ff14" />
    
    <!-- Coffee Mug next to cauldron -->
    <rect x="250" y="390" width="30" height="35" rx="6" fill="#8b0000" stroke="#f8f9fa" stroke-width="2"/>
    <path d="M 280 398 C 285 398, 288 402, 288 406 C 288 410, 285 414, 280 414" fill="none" stroke="#f8f9fa" stroke-width="2"/>
    <!-- Ghost Steam -->
    <path d="M 265 380 Q 270 370, 265 362 Q 275 370, 270 382 Z" fill="#f8f9fa" opacity="0.8"/>
  </g>

  <!-- Center Text and Info Panel -->
  <g transform="translate(380, 180)">
    <text class="title-text" x="0" y="40">CHARAN BS</text>
    <text class="body-text" x="0" y="80">&gt; <tspan class="neon-text">SPOOKY FULL-STACK WIZARD</tspan></text>
    
    <!-- Code Box (Terminal Style) -->
    <g transform="translate(0, 110)">
      <rect width="520" height="150" rx="10" fill="#0d1117" stroke="#ff7518" stroke-width="2" style="filter: drop-shadow(0 8px 16px rgba(0,0,0,0.5));"/>
      <path d="M 0 30 H 520" stroke="#ff7518" stroke-width="1.5"/>
      <circle cx="15" cy="15" r="5" fill="#8b0000"/>
      <circle cx="30" cy="15" r="5" fill="#ff7518"/>
      <circle cx="45" cy="15" r="5" fill="#39ff14"/>
      <text x="260" y="20" fill="#f8f9fa" font-family="monospace" font-size="12" text-anchor="middle">spooky_terminal.sh</text>
      
      <!-- Text inside Terminal -->
      <g font-family="monospace" font-size="14" fill="#f8f9fa" transform="translate(20, 55)">
        <text x="0" y="10" fill="#39ff14">&gt; npm run cast-spells</text>
        <text x="0" y="35" fill="#ffd166">&gt; Compiling witch brew...</text>
        <text x="0" y="60" fill="#ff7518">&gt; Power Level: INF_SPOOKY</text>
        <!-- Blinking cursor -->
        <rect x="235" y="48" width="8" height="15" fill="#ff7518">
          <animate attributeName="visibility" values="visible;hidden" dur="1s" repeatCount="indefinite"/>
        </rect>
      </g>
    </g>
  </g>

  <!-- Right: Handcrafted Jack-o'-lantern & Ghost -->
  <g class="animated-ghost" transform="translate(980, 260)">
    <!-- Cute Ghost -->
    <path d="M 30 70 C 30 20, 90 20, 90 70 C 90 90, 80 85, 60 95 C 40 85, 30 90, 30 70 Z" fill="#f8f9fa" stroke="#240046" stroke-width="3"/>
    <circle cx="50" cy="50" r="3.5" fill="#0d1117"/>
    <circle cx="70" cy="50" r="3.5" fill="#0d1117"/>
    <path d="M 56 60 Q 60 64, 64 60" stroke="#0d1117" stroke-width="2" fill="none"/>
  </g>

  <g transform="translate(1000, 370)">
    <!-- Pumpkin -->
    <ellipse cx="60" cy="65" rx="50" ry="40" fill="#ff7518" stroke="#0d1117" stroke-width="3"/>
    <ellipse cx="60" cy="65" rx="30" ry="40" fill="#e85d04" stroke="#0d1117" stroke-width="2"/>
    <!-- Stem -->
    <path d="M 60 25 C 58 15, 52 10, 50 10 L 55 25" stroke="#0d1117" stroke-width="4" fill="none"/>
    <!-- Flashing Yellow-Orange Eyes -->
    <polygon class="lantern-eye" points="40,55 50,50 45,62" fill="#ffd166"/>
    <polygon class="lantern-eye" points="80,55 70,50 75,62" fill="#ffd166"/>
    <!-- Scary Mouth -->
    <path class="lantern-eye" d="M 35,75 Q 60,95 85,75 Q 70,80 60,77 Q 50,80 35,75 Z" fill="#ffd166"/>
  </g>

  <!-- Floating Witch Hat on Cauldron L -->
  <g class="animated-hat" transform="translate(210, 200)">
    <!-- Hat -->
    <path d="M 10 50 Q 40 45, 70 50 Q 40 55, 10 50 Z" fill="#240046" stroke="#0d1117" stroke-width="2"/>
    <path d="M 22 47 L 40 10 L 58 47 Z" fill="#5a189a" stroke="#0d1117" stroke-width="2"/>
    <rect x="33" y="42" width="14" height="6" fill="#e85d04"/>
  </g>

  <!-- Floating Bats -->
  <g transform="translate(720, 100)">
    <path class="bat-wing" d="M 0 10 Q 15 -10, 25 5 Q 35 -10, 50 10 Q 25 15, 0 10 Z" fill="#0d1117"/>
  </g>
  <g transform="translate(850, 70)">
    <path class="bat-wing" d="M 0 8 Q 10 -8, 18 4 Q 26 -8, 36 8 Q 18 12, 0 8 Z" fill="#0d1117"/>
  </g>
</svg>"""
    with open("halloween/banner.svg", "w") as f:
        f.write(banner_content)
    print("Generated halloween/banner.svg")

    # 2. SVG Illustrations
    print("Generating SVG Illustrations...")
    # A. Witch Hat
    witch_hat = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <path d="M 15 90 C 45 80, 75 80, 105 90 C 75 100, 45 100, 15 90 Z" fill="#240046" stroke="#0d1117" stroke-width="3"/>
  <path d="M 35 85 Q 45 20, 65 15 Q 70 20, 85 85 Z" fill="#5a189a" stroke="#0d1117" stroke-width="3"/>
  <path d="M 37 84 C 55 78, 65 78, 83 84 L 81 75 C 65 70, 55 70, 39 75 Z" fill="#e85d04" stroke="#0d1117" stroke-width="1.5"/>
  <rect x="54" y="72" width="12" height="10" fill="#ffd166" stroke="#0d1117" stroke-width="2"/>
</svg>"""
    with open("halloween/illustrations/witch_hat.svg", "w") as f:
        f.write(witch_hat)

    # B. Jack-o'-lantern
    jack = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <ellipse cx="60" cy="65" rx="45" ry="38" fill="#ff7518" stroke="#0d1117" stroke-width="3"/>
  <ellipse cx="60" cy="65" rx="28" ry="38" fill="#e85d04" stroke="#0d1117" stroke-width="2"/>
  <ellipse cx="60" cy="65" rx="14" ry="38" fill="#d04e00" stroke="#0d1117" stroke-width="1"/>
  <path d="M 60 27 C 58 18, 52 12, 50 12 L 55 27 Z" fill="#240046" stroke="#0d1117" stroke-width="2"/>
  <polygon points="42,55 52,50 48,60" fill="#ffd166" stroke="#0d1117" stroke-width="1.5"/>
  <polygon points="78,55 68,50 72,60" fill="#ffd166" stroke="#0d1117" stroke-width="1.5"/>
  <polygon points="60,65 56,71 64,71" fill="#ffd166" stroke="#0d1117" stroke-width="1.5"/>
  <path d="M 38 80 Q 60 100 82 80 Q 70 85 60 82 Q 50 85 38 80 Z" fill="#ffd166" stroke="#0d1117" stroke-width="1.5"/>
</svg>"""
    with open("halloween/illustrations/jack_o_lantern.svg", "w") as f:
        f.write(jack)

    # C. Ghost
    ghost = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <path d="M 35 70 C 35 25, 85 25, 85 70 C 85 90, 75 85, 60 95 C 45 85, 35 90, 35 70 Z" fill="#f8f9fa" stroke="#240046" stroke-width="3"/>
  <circle cx="50" cy="50" r="3.5" fill="#0d1117"/>
  <circle cx="70" cy="50" r="3.5" fill="#0d1117"/>
  <path d="M 55 62 Q 60 66, 65 62" stroke="#0d1117" stroke-width="2" fill="none"/>
</svg>"""
    with open("halloween/illustrations/ghost.svg", "w") as f:
        f.write(ghost)

    # D. Bat
    bat = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <path d="M 15 60 Q 45 35, 55 55 Q 65 35, 105 60 Q 80 75, 60 65 Q 40 75, 15 60 Z" fill="#0d1117" stroke="#5a189a" stroke-width="2"/>
  <circle cx="56" cy="53" r="1.5" fill="#8b0000"/>
  <circle cx="64" cy="53" r="1.5" fill="#8b0000"/>
</svg>"""
    with open("halloween/illustrations/bat.svg", "w") as f:
        f.write(bat)

    # E. Potion Cauldron
    potion = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <path d="M 30 70 C 30 95, 90 95, 90 70 C 90 55, 30 55, 30 70 Z" fill="#1c1c1c" stroke="#5a189a" stroke-width="3"/>
  <ellipse cx="60" cy="58" rx="28" ry="6" fill="#240046" stroke="#5a189a" stroke-width="2"/>
  <ellipse cx="60" cy="58" rx="25" ry="4" fill="#39ff14"/>
  <circle cx="50" cy="40" r="5" fill="#39ff14" opacity="0.8"/>
  <circle cx="70" cy="35" r="3" fill="#39ff14" opacity="0.6"/>
  <circle cx="58" cy="45" r="4" fill="#39ff14" opacity="0.7"/>
</svg>"""
    with open("halloween/illustrations/potion.svg", "w") as f:
        f.write(potion)

    # F. Skull
    skull = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <rect x="40" y="30" width="40" height="42" rx="16" fill="#f8f9fa" stroke="#0d1117" stroke-width="3"/>
  <rect x="48" y="65" width="24" height="20" rx="4" fill="#f8f9fa" stroke="#0d1117" stroke-width="3"/>
  <circle cx="50" cy="50" r="6" fill="#0d1117"/>
  <circle cx="70" cy="50" r="6" fill="#0d1117"/>
  <path d="M 58 60 L 60 55 L 62 60 Z" fill="#0d1117"/>
  <line x1="53" y1="75" x2="53" y2="82" stroke="#0d1117" stroke-width="2"/>
  <line x1="60" y1="75" x2="60" y2="82" stroke="#0d1117" stroke-width="2"/>
  <line x1="67" y1="75" x2="67" y2="82" stroke="#0d1117" stroke-width="2"/>
</svg>"""
    with open("halloween/illustrations/skull.svg", "w") as f:
        f.write(skull)

    # G. Haunted Tree
    haunted_tree = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <path d="M 55 110 C 55 80, 40 70, 30 60 C 20 50, 15 35, 10 35 M 30 60 C 35 55, 42 62, 48 50 C 52 40, 50 30, 48 20 M 65 110 C 65 80, 80 70, 90 60 C 100 50, 105 35, 110 35 M 90 60 C 85 55, 78 62, 72 50 C 68 40, 70 30, 72 20" stroke="#0d1117" stroke-width="6" stroke-linecap="round"/>
  <path d="M 45 40 Q 60 30, 55 10" stroke="#0d1117" stroke-width="3" stroke-linecap="round"/>
</svg>"""
    with open("halloween/illustrations/haunted_tree.svg", "w") as f:
        f.write(haunted_tree)

    # H. Spider Web
    spider_web = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <line x1="10" y1="10" x2="110" y2="110" stroke="#5a189a" stroke-width="1.5"/>
  <line x1="110" y1="10" x2="10" y2="110" stroke="#5a189a" stroke-width="1.5"/>
  <line x1="60" y1="10" x2="60" y2="110" stroke="#5a189a" stroke-width="1.5"/>
  <line x1="10" y1="60" x2="110" y2="60" stroke="#5a189a" stroke-width="1.5"/>
  
  <path d="M 60 35 Q 42 42, 35 60 Q 42 78, 60 85 Q 78 78, 85 60 Q 78 42, 60 35 Z" stroke="#5a189a" stroke-width="1" stroke-dasharray="2 2"/>
  <path d="M 60 20 Q 32 32, 20 60 Q 32 88, 60 100 Q 88 88, 100 60 Q 88 32, 60 20 Z" stroke="#5a189a" stroke-width="1" stroke-dasharray="2 2"/>
</svg>"""
    with open("halloween/illustrations/spider_web.svg", "w") as f:
        f.write(spider_web)

    # I. Octocat wearing witch hat
    octo_witch = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120" fill="none">
  <path d="M 60 30 C 40 30, 30 42, 30 62 C 30 82, 45 92, 60 92 C 75 92, 90 82, 90 62 C 90 42, 80 30, 60 30 Z" fill="#0d1117" stroke="#ffd166" stroke-width="3"/>
  <polygon points="32,38 20,20 40,32" fill="#0d1117" stroke="#ffd166" stroke-width="2"/>
  <polygon points="88,38 100,20 80,32" fill="#0d1117" stroke="#ffd166" stroke-width="2"/>
  <ellipse cx="48" cy="58" rx="4" ry="6" fill="#ffd166"/>
  <ellipse cx="72" cy="58" rx="4" ry="6" fill="#ffd166"/>
  <polygon points="58,66 62,66 60,69" fill="#ff7518"/>
  
  <g transform="translate(10, -5)">
    <path d="M 25 45 C 40 40, 60 40, 75 45 C 60 50, 40 50, 25 45 Z" fill="#240046" stroke="#0d1117" stroke-width="1.5"/>
    <path d="M 35 43 L 50 15 L 65 43 Z" fill="#5a189a" stroke="#0d1117" stroke-width="1.5"/>
    <rect x="46" y="38" width="8" height="5" fill="#e85d04"/>
  </g>
</svg>"""
    with open("halloween/illustrations/octocat_witch.svg", "w") as f:
        f.write(octo_witch)

    # 3. SVG Dividers
    print("Generating Dividers...")
    # Vines Divider
    vines = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 80" width="100%" height="80" fill="none">
  <path d="M 0 40 C 150 10, 300 70, 450 40 C 600 10, 750 70, 900 40 C 1050 10, 1200 40, 1200 40" stroke="#7fff00" stroke-width="4" stroke-linecap="round"/>
  <path d="M 120 32 Q 130 15, 145 28 Z" fill="#240046" stroke="#7fff00" stroke-width="1.5"/>
  <path d="M 520 48 Q 530 65, 545 52 Z" fill="#240046" stroke="#7fff00" stroke-width="1.5"/>
  <path d="M 820 32 Q 830 15, 845 28 Z" fill="#240046" stroke="#7fff00" stroke-width="1.5"/>
  <line x1="280" y1="48" x2="285" y2="60" stroke="#7fff00" stroke-width="2"/>
  <line x1="700" y1="32" x2="695" y2="20" stroke="#7fff00" stroke-width="2"/>
  <g transform="translate(380, 45)">
    <line x1="0" y1="0" x2="0" y2="20" stroke="#5a189a" stroke-width="1" stroke-dasharray="2 2"/>
    <circle cx="0" cy="22" r="4" fill="#0d1117" stroke="#ff7518" stroke-width="1"/>
  </g>
  <g transform="translate(980, 32)">
    <line x1="0" y1="0" x2="0" y2="25" stroke="#5a189a" stroke-width="1" stroke-dasharray="2 2"/>
    <circle cx="0" cy="27" r="4" fill="#0d1117" stroke="#ff7518" stroke-width="1"/>
  </g>
</svg>"""
    with open("halloween/dividers/vines.svg", "w") as f:
        f.write(vines)

    # Web Divider
    webs = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 80" width="100%" height="80" fill="none">
  <path d="M 0 10 Q 150 40, 300 10 Q 450 40, 600 10 Q 750 40, 900 10 Q 1050 40, 1200 10" stroke="#5a189a" stroke-width="2"/>
  <path d="M 0 22 Q 150 52, 300 22 Q 450 52, 600 22 Q 750 52, 900 22 Q 1050 52, 1200 22" stroke="#5a189a" stroke-width="1.5" stroke-dasharray="3 3"/>
  <line x1="150" y1="25" x2="150" y2="70" stroke="#5a189a" stroke-width="1"/>
  <line x1="450" y1="25" x2="450" y2="70" stroke="#5a189a" stroke-width="1"/>
  <line x1="750" y1="25" x2="750" y2="70" stroke="#5a189a" stroke-width="1"/>
  <line x1="1050" y1="25" x2="1050" y2="70" stroke="#5a189a" stroke-width="1"/>
</svg>"""
    with open("halloween/dividers/webs.svg", "w") as f:
        f.write(webs)

    # Skulls Divider
    skulls = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" width="100%" height="60" fill="none">
  <path d="M 0 30 H 1200" stroke="#e85d04" stroke-width="2" stroke-dasharray="12 24"/>
  <g transform="translate(200, 15)">
    <rect x="0" y="0" width="20" height="20" rx="8" fill="#f8f9fa" stroke="#0d1117" stroke-width="2"/>
    <circle cx="6" cy="8" r="2.5" fill="#0d1117"/>
    <circle cx="14" cy="8" r="2.5" fill="#0d1117"/>
  </g>
  <g transform="translate(600, 15)">
    <rect x="0" y="0" width="20" height="20" rx="8" fill="#f8f9fa" stroke="#0d1117" stroke-width="2"/>
    <circle cx="6" cy="8" r="2.5" fill="#0d1117"/>
    <circle cx="14" cy="8" r="2.5" fill="#0d1117"/>
  </g>
  <g transform="translate(1000, 15)">
    <rect x="0" y="0" width="20" height="20" rx="8" fill="#f8f9fa" stroke="#0d1117" stroke-width="2"/>
    <circle cx="6" cy="8" r="2.5" fill="#0d1117"/>
    <circle cx="14" cy="8" r="2.5" fill="#0d1117"/>
  </g>
</svg>"""
    with open("halloween/dividers/skulls.svg", "w") as f:
        f.write(skulls)

    # Moon and Stars Divider
    moon_stars = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" width="100%" height="60" fill="none">
  <path d="M 0 30 Q 300 50, 600 30 Q 900 10, 1200 30" stroke="#ff7518" stroke-width="2" stroke-opacity="0.5"/>
  <g transform="translate(150, 15)" fill="#ffd166">
    <path d="M 10 0 C 15 5, 15 15, 10 20 C 5 15, 5 5, 10 0 Z" />
  </g>
  <g transform="translate(450, 15)" fill="#ffd166">
    <path d="M 10 0 C 15 5, 15 15, 10 20 C 5 15, 5 5, 10 0 Z" />
  </g>
  <g transform="translate(750, 15)" fill="#ffd166">
    <path d="M 10 0 C 15 5, 15 15, 10 20 C 5 15, 5 5, 10 0 Z" />
  </g>
  <g transform="translate(1050, 15)" fill="#ffd166">
    <path d="M 10 0 C 15 5, 15 15, 10 20 C 5 15, 5 5, 10 0 Z" />
  </g>
</svg>"""
    with open("halloween/dividers/moon_stars.svg", "w") as f:
        f.write(moon_stars)

    # Bats Divider
    bats_div = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" width="100%" height="60" fill="none">
  <path d="M 50 30 Q 60 10, 65 25 Q 70 10, 80 30 Q 65 35, 50 30 Z" fill="#0d1117" stroke="#240046" stroke-width="2"/>
  <path d="M 350 30 Q 360 10, 365 25 Q 370 10, 380 30 Q 365 35, 350 30 Z" fill="#0d1117" stroke="#240046" stroke-width="2"/>
  <path d="M 650 30 Q 660 10, 665 25 Q 670 10, 680 30 Q 665 35, 650 30 Z" fill="#0d1117" stroke="#240046" stroke-width="2"/>
  <path d="M 950 30 Q 960 10, 965 25 Q 970 10, 980 30 Q 965 35, 950 30 Z" fill="#0d1117" stroke="#240046" stroke-width="2"/>
</svg>"""
    with open("halloween/dividers/bats.svg", "w") as f:
        f.write(bats_div)

    # 4. Section Headers
    print("Generating Section Headers...")
    headers = {
        "about.svg": ("ABOUT ME", "#ff7518", "ghost.svg"),
        "skills.svg": ("TECH STACK", "#39ff14", "potion.svg"),
        "stats.svg": ("GHOSTLY STATS", "#ffd166", "skull.svg"),
        "projects.svg": ("PORTAL PROJECTS", "#8b0000", "witch_hat.svg"),
        "contact.svg": ("SUMMON ME", "#7fff00", "bat.svg"),
        "achievements.svg": ("GRIMOIRE ARCHIVES", "#ff7518", "jack_o_lantern.svg")
    }
    
    for filename, (title, color, icon_file) in headers.items():
        header_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 60" width="400" height="60" fill="none">
  <defs>
    <filter id="h-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <style>
    .header-text {{
      font-family: 'Creepster', 'Luminari', 'Chiller', 'Impact', 'Arial Black', sans-serif;
      font-size: 28px;
      letter-spacing: 2px;
    }}
  </style>
  <text x="70" y="42" fill="{color}" class="header-text" filter="url(#h-glow)">{title}</text>
  <path d="M 10 15 L 20 15 M 10 15 L 10 45 L 20 45" stroke="{color}" stroke-width="2"/>
  <circle cx="20" cy="15" r="3" fill="{color}"/>
  <circle cx="20" cy="45" r="3" fill="{color}"/>
</svg>"""
        with open(f"halloween/headers/{filename}", "w") as f:
            f.write(header_svg)

    # 5. Halloween-styled Programming Icons
    print("Generating Spooky Programming Icons...")
    
    # HTML: Tombstone
    html_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <path d="M 20 80 C 20 30, 80 30, 80 80 Z" fill="#0d1117" stroke="#e85d04" stroke-width="3"/>
  <text x="50" y="55" fill="#ff7518" font-family="monospace" font-weight="bold" font-size="18" text-anchor="middle">&lt;H5&gt;</text>
  <text x="50" y="75" fill="#f8f9fa" font-family="monospace" font-size="10" text-anchor="middle">HTML RIP</text>
</svg>"""
    with open("halloween/icons/html.svg", "w") as f:
        f.write(html_ico)

    # CSS: Spiderweb
    css_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <circle cx="50" cy="50" r="35" stroke="#5a189a" stroke-width="2"/>
  <line x1="50" y1="15" x2="50" y2="85" stroke="#5a189a" stroke-width="2"/>
  <line x1="15" y1="50" x2="85" y2="50" stroke="#5a189a" stroke-width="2"/>
  <path d="M 50 30 Q 38 38, 30 50 Q 38 62, 50 70 Q 62 62, 70 50 Q 62 38, 50 30 Z" stroke="#5a189a" stroke-width="1.5" stroke-dasharray="2 2"/>
  <text x="50" y="58" fill="#ffd166" font-family="monospace" font-weight="bold" font-size="28" text-anchor="middle">{ }</text>
</svg>"""
    with open("halloween/icons/css.svg", "w") as f:
        f.write(css_ico)

    # JS: Spellbook
    js_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <rect x="25" y="15" width="55" height="70" rx="4" fill="#240046" stroke="#ff7518" stroke-width="3"/>
  <rect x="20" y="15" width="8" height="70" rx="2" fill="#5a189a" stroke="#ff7518" stroke-width="1.5"/>
  <rect x="42" y="38" width="22" height="22" fill="#ff7518"/>
  <text x="53" y="55" fill="#240046" font-family="sans-serif" font-weight="bold" font-size="16" text-anchor="middle">JS</text>
  <path d="M 45 75 Q 48 70, 52 75" stroke="#ffd166" stroke-width="1.5"/>
</svg>"""
    with open("halloween/icons/js.svg", "w") as f:
        f.write(js_ico)

    # Python: Skull and Snakes
    python_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <rect x="35" y="30" width="30" height="30" rx="10" fill="#f8f9fa" stroke="#0d1117" stroke-width="2"/>
  <rect x="40" y="55" width="20" height="12" fill="#f8f9fa" stroke="#0d1117" stroke-width="2"/>
  <circle cx="43" cy="42" r="3.5" fill="#0d1117"/>
  <circle cx="57" cy="42" r="3.5" fill="#0d1117"/>
  <path d="M 25 35 Q 35 20, 50 25 Q 65 30, 75 15" stroke="#39ff14" stroke-width="4" stroke-linecap="round"/>
  <path d="M 75 65 Q 65 80, 50 75 Q 35 70, 25 85" stroke="#ffd166" stroke-width="4" stroke-linecap="round"/>
</svg>"""
    with open("halloween/icons/python.svg", "w") as f:
        f.write(python_ico)

    # React: Atomic web
    react_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <ellipse cx="50" cy="50" rx="42" ry="14" stroke="#7fff00" stroke-width="1.5" transform="rotate(30 50 50)"/>
  <ellipse cx="50" cy="50" rx="42" ry="14" stroke="#7fff00" stroke-width="1.5" transform="rotate(90 50 50)"/>
  <ellipse cx="50" cy="50" rx="42" ry="14" stroke="#7fff00" stroke-width="1.5" transform="rotate(150 50 50)"/>
  <circle cx="50" cy="50" r="4" fill="#ff7518"/>
  <path d="M 50 50 L 56 46 M 50 50 L 56 54 M 50 50 L 44 46 M 50 50 L 44 54" stroke="#ff7518" stroke-width="1.5"/>
</svg>"""
    with open("halloween/icons/react.svg", "w") as f:
        f.write(react_ico)

    # Node: Cauldron
    node_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <path d="M 25 55 C 25 78, 75 78, 75 55 C 75 45, 25 45, 25 55 Z" fill="#1c1c1c" stroke="#39ff14" stroke-width="2.5"/>
  <ellipse cx="50" cy="48" rx="23" ry="5" fill="#240046" stroke="#39ff14" stroke-width="2"/>
  <ellipse cx="50" cy="48" rx="20" ry="3" fill="#39ff14"/>
  <circle cx="45" cy="32" r="3.5" fill="#39ff14" opacity="0.8"/>
  <circle cx="58" cy="28" r="4.5" fill="#39ff14" opacity="0.6"/>
  <text x="50" y="68" fill="#f8f9fa" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">NODE</text>
</svg>"""
    with open("halloween/icons/node.svg", "w") as f:
        f.write(node_ico)

    # Docker: Whale
    docker_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <path d="M 15 60 C 15 40, 50 35, 65 48 C 75 48, 85 52, 80 62 C 75 64, 50 62, 15 60 Z" fill="#f8f9fa" stroke="#e85d04" stroke-width="2"/>
  <rect x="35" y="32" width="10" height="10" fill="#ff7518" stroke="#0d1117"/>
  <rect x="47" y="32" width="10" height="10" fill="#e85d04" stroke="#0d1117"/>
  <rect x="41" y="20" width="10" height="10" fill="#ffd166" stroke="#0d1117"/>
</svg>"""
    with open("halloween/icons/docker.svg", "w") as f:
        f.write(docker_ico)

    # Git: Branching Roots
    git_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <path d="M 50 90 L 50 50 M 50 50 L 30 30 M 50 65 L 70 45" stroke="#8b0000" stroke-width="4" stroke-linecap="round"/>
  <circle cx="50" cy="50" r="5" fill="#8b0000" stroke="#f8f9fa" stroke-width="1.5"/>
  <circle cx="30" cy="30" r="5" fill="#8b0000" stroke="#f8f9fa" stroke-width="1.5"/>
  <circle cx="70" cy="45" r="5" fill="#8b0000" stroke="#f8f9fa" stroke-width="1.5"/>
  <text x="50" y="18" fill="#8b0000" font-family="monospace" font-weight="bold" font-size="12" text-anchor="middle">BRANCH</text>
</svg>"""
    with open("halloween/icons/git.svg", "w") as f:
        f.write(git_ico)

    # GitHub: Cat skull
    github_ico = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100" fill="none">
  <path d="M 50 25 C 32 25, 25 35, 25 52 C 25 68, 38 78, 50 78 C 62 78, 75 68, 75 52 C 75 35, 68 25, 50 25 Z" fill="#0d1117" stroke="#39ff14" stroke-width="2.5"/>
  <polygon points="28,32 18,15 35,26" fill="#0d1117" stroke="#39ff14" stroke-width="2"/>
  <polygon points="72,32 82,15 65,26" fill="#0d1117" stroke="#39ff14" stroke-width="2"/>
  <circle cx="42" cy="48" r="3" fill="#39ff14"/>
  <circle cx="58" cy="48" r="3" fill="#39ff14"/>
</svg>"""
    with open("halloween/icons/github.svg", "w") as f:
        f.write(github_ico)

    # 6. Frames
    print("Generating Frames...")
    # Profile Picture Frame
    profile_frame = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 280" width="240" height="280" fill="none">
  <path d="M 20 260 C 20 80, 220 80, 220 260 Z" fill="#0d1117" stroke="#ffd166" stroke-width="4"/>
  <text x="120" y="100" fill="#ffd166" font-family="'Creepster', cursive" font-size="28" text-anchor="middle">RIP</text>
  <path d="M 20 180 Q 40 170, 50 150 M 20 160 Q 32 155, 35 140" stroke="#ffd166" stroke-width="1.5" stroke-opacity="0.6"/>
  <path d="M 220 180 Q 200 170, 190 150 M 220 160 Q 208 155, 205 140" stroke="#ffd166" stroke-width="1.5" stroke-opacity="0.6"/>
</svg>"""
    with open("halloween/frames/profile_frame.svg", "w") as f:
        f.write(profile_frame)

    # Cauldron stats frame
    stats_frame = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 200" width="450" height="200" fill="none">
  <rect width="450" height="200" rx="14" fill="#0d1117" stroke="#39ff14" stroke-width="2"/>
  <path d="M 15 15 L 30 15 M 15 15 L 15 30" stroke="#39ff14" stroke-width="3"/>
  <path d="M 435 15 L 420 15 M 435 15 L 435 30" stroke="#39ff14" stroke-width="3"/>
  <path d="M 15 185 L 30 185 M 15 185 L 15 170" stroke="#39ff14" stroke-width="3"/>
  <path d="M 435 185 L 420 185 M 435 185 L 435 170" stroke="#39ff14" stroke-width="3"/>
</svg>"""
    with open("halloween/frames/stats_frame.svg", "w") as f:
        f.write(stats_frame)

    # 7. Badges
    print("Generating Badges...")
    badge_dev = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 40" width="160" height="40" fill="none">
  <rect width="160" height="40" rx="8" fill="#240046" stroke="#ffd166" stroke-width="1.5"/>
  <text x="80" y="25" fill="#ffd166" font-family="monospace" font-weight="bold" font-size="12" text-anchor="middle">SPOOKY DEV</text>
  <circle cx="15" cy="20" r="4" fill="#ff7518"/>
  <circle cx="145" cy="20" r="4" fill="#ff7518"/>
</svg>"""
    with open("halloween/badges/badge_dev.svg", "w") as f:
        f.write(badge_dev)

    # 8. Background Patterns
    print("Generating Background Patterns...")
    bg_pattern = """<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 60 60">
  <rect width="60" height="60" fill="#0d1117"/>
  <g fill="#240046" opacity="0.3">
    <rect x="25" y="20" width="10" height="10" rx="4"/>
    <rect x="27" y="28" width="6" height="4" rx="1"/>
    <circle cx="28" cy="23" r="1"/>
    <circle cx="32" cy="23" r="1"/>
  </g>
  <path d="M 5 5 Q 15 0, 18 3 Q 21 0, 30 5 Q 18 8, 5 5 Z" fill="#240046" opacity="0.2"/>
</svg>"""
    with open("halloween/backgrounds/spooky_pattern.svg", "w") as f:
        f.write(bg_pattern)

    # 9. Floating Decorations
    print("Generating Decorations...")
    spider = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" width="40" height="40" fill="none">
  <circle cx="20" cy="20" r="6" fill="#0d1117" stroke="#ff7518" stroke-width="2"/>
  <path d="M 15 18 C 10 16, 5 18, 5 22" stroke="#ff7518" stroke-width="1.5"/>
  <path d="M 14 20 C 8 18, 4 22, 4 26" stroke="#ff7518" stroke-width="1.5"/>
  <path d="M 15 22 C 10 22, 6 26, 6 30" stroke="#ff7518" stroke-width="1.5"/>
  <path d="M 25 18 C 30 16, 35 18, 35 22" stroke="#ff7518" stroke-width="1.5"/>
  <path d="M 26 20 C 32 18, 36 22, 36 26" stroke="#ff7518" stroke-width="1.5"/>
  <path d="M 25 22 C 30 22, 34 26, 34 30" stroke="#ff7518" stroke-width="1.5"/>
</svg>"""
    with open("halloween/decorations/spider.svg", "w") as f:
        f.write(spider)

    print("SVG assets generated successfully.")


# Generate README.md
def generate_readme():
    print("Writing new README.md...")
    username = "CharanBS18"
    email = "charan201204@gmail.com"
    
    readme_content = f"""<h1 align="center">🔮 GRIMOIRE ACCESS NODE // {username.upper()} 🔮</h1>

<p align="center">
  <img alt="Premium Spooky Halloween Banner" src="halloween/banner.svg" width="100%">
</p>

<!-- Spooky Decorative Panel -->
<p align="center">
  <img src="halloween/dividers/webs.svg" width="100%">
</p>

<!-- Bio Section -->
<a id="about-me"></a>
<p align="center">
  <img src="halloween/headers/about.svg" width="380">
</p>

<table align="center" border="0" cellpadding="15" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto; background-color: #0d1117;">
  <tr style="border: 0px;">
    <!-- Profile Frame -->
    <td align="center" valign="middle" style="border: 0px; padding: 10px; width: 40%;">
      <div style="position: relative; display: inline-block; width: 240px; height: 280px;">
        <!-- Spooky Avatar Image (positioned inside the frame) -->
        <img src="halloween/spooky_avatar.png" alt="Spooky Avatar" width="160" style="position: absolute; top: 90px; left: 40px; border-radius: 50%; border: 3px solid #ff7518; z-index: 1;">
        <!-- Tombstone Frame overlay -->
        <img src="halloween/frames/profile_frame.svg" alt="Tombstone Frame" width="240" style="position: absolute; top: 0; left: 0; z-index: 2; pointer-events: none;">
        <!-- Floating ghost animation -->
        <img src="halloween/animations/floating_ghost.gif" alt="Animated Ghost" width="80" style="position: absolute; bottom: -5px; right: -5px; z-index: 3;">
      </div>
    </td>
    <!-- Bio Monospace Details -->
    <td valign="top" style="border: 0px; padding: 20px; width: 60%; font-family: monospace; color: #f8f9fa;">
      <h3 style="color: #ff7518; margin-top: 0;">&gt; COFFIN_NODE.conf</h3>
      <p><b>&gt; IDENTITY:</b> Charan BS / @{username}</p>
      <p><b>&gt; ACCESS_PORT:</b> <a href="mailto:{email}" style="color: #39ff14;">{email}</a></p>
      <p><b>&gt; ALIGNMENT:</b> <code style="color: #ffd166;">Chaotic Creative Developer</code></p>
      <hr style="border: 1px solid #240046; opacity: 0.8; margin: 15px 0;">
      <p style="line-height: 1.6; color: #f8f9fa;">
        Welcome, mortal visitor, to the spectral repository node. I craft responsive, high-performance web structures using midnight potions, green slime, and dark-mode coding rituals. I believe in clean code, robust architectures, and pixel-perfect design craftsmanship.
      </p>
    </td>
  </tr>
</table>

<p align="center">
  <img src="halloween/dividers/vines.svg" width="100%">
</p>

<!-- Tech Stack Section -->
<a id="tech-stack"></a>
<p align="center">
  <img src="halloween/headers/skills.svg" width="380">
</p>

<p align="center">
  <img src="halloween/icons/html.svg" width="75" alt="HTML">
  <img src="halloween/icons/css.svg" width="75" alt="CSS">
  <img src="halloween/icons/js.svg" width="75" alt="JS">
  <img src="halloween/icons/python.svg" width="75" alt="Python">
  <img src="halloween/icons/react.svg" width="75" alt="React">
  <img src="halloween/icons/node.svg" width="75" alt="Node.js">
  <img src="halloween/icons/docker.svg" width="75" alt="Docker">
  <img src="halloween/icons/git.svg" width="75" alt="Git">
  <img src="halloween/icons/github.svg" width="75" alt="GitHub">
</p>

<!-- Cauldron and witch hat animation -->
<p align="center">
  <img src="halloween/animations/magic_particles.gif" width="75" alt="Bubbling Potion Particle">
  <img src="halloween/animations/floating_witch_hat.gif" width="75" alt="Floating Witch Hat">
  <img src="halloween/animations/candle_flicker.gif" width="55" alt="Flickering Candle">
</p>

<p align="center">
  <img src="halloween/dividers/skulls.svg" width="100%">
</p>

<!-- Stats Section -->
<a id="stats"></a>
<p align="center">
  <img src="halloween/headers/stats.svg" width="380">
</p>

<table align="center" border="0" cellpadding="10" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto;">
  <tr style="border: 0px;">
    <td align="center" valign="middle" style="border: 0px;">
      <!-- Stats image with custom frame styling -->
      <div style="position: relative; display: inline-block;">
        <img src="stats.svg" alt="Stats Summary" width="420" style="border: 2px solid #5a189a; border-radius: 8px;">
        <img src="halloween/animations/pumpkin_glow.gif" alt="Glowing Pumpkin" width="60" style="position: absolute; top: -25px; left: -25px;">
      </div>
    </td>
    <td align="center" valign="middle" style="border: 0px;">
      <!-- Languages summary -->
      <div style="position: relative; display: inline-block;">
        <img src="langs.svg" alt="Languages Summary" width="420" style="border: 2px solid #39ff14; border-radius: 8px;">
        <img src="halloween/animations/twinkling_stars.gif" alt="Twinkling Stars" width="60" style="position: absolute; bottom: -25px; right: -25px;">
      </div>
    </td>
  </tr>
</table>

<p align="center" style="margin-top: 20px;">
  <!-- Coffin trophies summary -->
  <img src="trophies.svg" alt="Spooky Trophies" width="100%" style="max-width: 860px; border: 2px solid #ff7518; border-radius: 8px;">
</p>

<p align="center">
  <img src="halloween/dividers/moon_stars.svg" width="100%">
</p>

<!-- Contribution Graph Section -->
<a id="contributions"></a>
<h3 align="center" style="font-family: monospace; color: #ff7518;">🎃 CONTRIBUTION SPIDER GRID 🎃</h3>

<p align="center">
  <!-- Contribution grid snake -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg?v=2">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake-light.svg?v=2">
    <img alt="GitHub Snake Game" src="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg?v=2" width="100%">
  </picture>
</p>

<p align="center">
  <img src="halloween/dividers/bats.svg" width="100%">
</p>

<!-- Featured Projects Section -->
<a id="projects"></a>
<p align="center">
  <img src="halloween/headers/projects.svg" width="380">
</p>

<table align="center" border="0" cellpadding="15" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto; width: 100%; max-width: 900px;">
  <tr style="border: 0px;">
    <!-- Project 1 Card -->
    <td valign="top" style="border: 0px; width: 50%; padding: 15px;">
      <div style="background-color: #0d1117; border: 2px solid #5a189a; border-radius: 8px; padding: 20px; font-family: monospace; min-height: 180px;">
        <h4 style="color: #ff7518; margin-top: 0;">🔮 spellcaster-compiler</h4>
        <p style="color: #f8f9fa; font-size: 13px;">A high-performance JS/TS AST analyzer that compiles spooky commands into clean, reactive pipelines. Supports custom plugin extensions.</p>
        <div style="margin-top: 15px;">
          <span style="border: 1px solid #7fff00; color: #7fff00; padding: 2px 6px; border-radius: 4px; font-size: 10px; margin-right: 5px;">TypeScript</span>
          <span style="border: 1px solid #ff7518; color: #ff7518; padding: 2px 6px; border-radius: 4px; font-size: 10px;">AST</span>
        </div>
      </div>
    </td>
    <!-- Project 2 Card -->
    <td valign="top" style="border: 0px; width: 50%; padding: 15px;">
      <div style="background-color: #0d1117; border: 2px solid #39ff14; border-radius: 8px; padding: 20px; font-family: monospace; min-height: 180px;">
        <h4 style="color: #ff7518; margin-top: 0;">💀 cauldron-db</h4>
        <p style="color: #f8f9fa; font-size: 13px;">Lightweight NoSQL key-value cache layer written in Python. Uses custom memory compression algorithms to store potion recipes efficiently.</p>
        <div style="margin-top: 15px;">
          <span style="border: 1px solid #ff7518; color: #ff7518; padding: 2px 6px; border-radius: 4px; font-size: 10px; margin-right: 5px;">Python</span>
          <span style="border: 1px solid #ffd166; color: #ffd166; padding: 2px 6px; border-radius: 4px; font-size: 10px;">Database</span>
        </div>
      </div>
    </td>
  </tr>
</table>

<p align="center">
  <img src="halloween/dividers/webs.svg" width="100%">
</p>

<!-- Summon / Contact Section -->
<a id="contact"></a>
<p align="center">
  <img src="halloween/headers/contact.svg" width="380">
</p>

<p align="center" style="font-family: monospace; color: #f8f9fa; font-size: 14px;">
  Send a message through the dark portal if you dare to collaborate:
  <br><br>
  <a href="mailto:{email}" style="display: inline-block; background-color: #240046; color: #ff7518; border: 2px solid #ff7518; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold;">
    📧 SUMMON THE WIZARD
  </a>
</p>

<!-- Spooky Footer -->
<p align="center" style="margin-top: 50px;">
  <img src="halloween/dividers/vines.svg" width="100%">
</p>

<p align="center" style="font-family: monospace; color: #5a189a; font-size: 11px;">
  PORTAL SECURED VISITORS: <img src="https://profile-counter.glitch.me/{username}/count.svg" alt="Views Counter" style="vertical-align: middle;"> // SECURE CONNECTIONS COMPLETED // STAY SPOOKY 🎃
</p>
"""
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("Generated README.md successfully.")


def main():
    setup_dirs()
    generate_gifs()
    generate_svgs()
    generate_readme()
    print("All spooky assets built successfully!")


if __name__ == "__main__":
    main()
