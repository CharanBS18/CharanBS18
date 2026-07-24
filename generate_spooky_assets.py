import os
import math
from PIL import Image, ImageDraw

# Create directories
def setup_dirs():
    dirs = [
        "halloween",
        "halloween/banner",
        "halloween/backgrounds",
        "halloween/dividers",
        "halloween/icons",
        "halloween/decorations",
        "halloween/projects",
        "halloween/badges",
        "halloween/animations",
        "halloween/footer",
        "halloween/terminal",
        "halloween/skills",
        "halloween/contact",
        "halloween/stats",
        "halloween/stickers"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("Spooky directory structure initialized successfully.")

def clean_sticker_bfs(img):
    w, h = img.size
    pix = img.load()
    visited = [[False]*h for _ in range(w)]
    components = []
    
    for x in range(w):
        for y in range(h):
            if pix[x, y][3] > 15 and not visited[x][y]:
                comp = []
                queue = [(x, y)]
                visited[x][y] = True
                q_idx = 0
                while q_idx < len(queue):
                    cx, cy = queue[q_idx]
                    q_idx += 1
                    comp.append((cx, cy))
                    # Check 8 neighbors
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < w and 0 <= ny < h:
                                if pix[nx, ny][3] > 15 and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                components.append(comp)
                
    if not components:
        return img
        
    largest_comp = max(components, key=len)
    largest_set = set(largest_comp)
    
    clean_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    clean_pix = clean_img.load()
    for x, y in largest_set:
        clean_pix[x, y] = pix[x, y]
                
    return clean_img

def crop_stickers():
    # 1. Crop/Copy stickers
    downloads_dir = "/Users/charanbs/Downloads/stickers"
    if os.path.exists(downloads_dir):
        print(f"Using user-provided cropped stickers from {downloads_dir}...")
        for i in range(20):
            idx_offset = 68 + i
            src_path = os.path.join(downloads_dir, f"{idx_offset}.png")
            dst_path = f"halloween/stickers/sticker_{i+1}.png"
            if os.path.exists(src_path):
                img = Image.open(src_path)
                bbox = img.getbbox()
                if bbox:
                    img = img.crop(bbox)
                img.thumbnail((300, 300), Image.Resampling.LANCZOS)
                img.save(dst_path)
                print(f"Processed user sticker {i+1} from {idx_offset}.png")
            else:
                print(f"Warning: {src_path} not found!")
        print("All 20 user-provided stickers copied and processed successfully.")
    elif os.path.exists("halloch.png"):
        print("halloch.png found, cropping stickers using BFS components...")
        img = Image.open("halloch.png")
        w, h = img.size
        cols, rows = 5, 4
        col_w, row_h = w / cols, h / rows
        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c + 1
                left = int(c * col_w)
                top = int(r * row_h)
                right = int((c + 1) * col_w)
                bottom = int((r + 1) * row_h)
                box = img.crop((left, top, right, bottom))
                
                # Clean stray elements from neighbors
                box = clean_sticker_bfs(box)
                
                bbox = box.getbbox()
                if bbox:
                    box = box.crop(bbox)
                box.thumbnail((300, 300), Image.Resampling.LANCZOS)
                box.save(f"halloween/stickers/sticker_{idx}.png")
        print("All 20 stickers cropped from sheet successfully.")
    else:
        print("No sticker source found, skipping sticker cropping.")

    # 2. Crop user portrait from chtransparent.png
    if not os.path.exists("chtransparent.png"):
        print("chtransparent.png not found, skipping user avatar cropping.")
    else:
        print("Cropping user portrait from chtransparent.png...")
        img = Image.open("chtransparent.png")
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        w, h = img.size
        new_w = 160
        new_h = int(new_w * h / w)
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        img.save("halloween/stickers/user_avatar.png")
        print("Transparent user avatar cropped and saved successfully.")

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

# Generate Loop Animations
def generate_animations():
    print("Generating Spooky Loop Animations...")
    
    # 1. Haunted Terminal Typing GIF (60 frames)
    # Commands: whoami, cat skills.txt, git status, npm run build, sudo summon-octocat
    term_frames = []
    actions = [
        # (text to type, prompt line text, output lines list)
        ("whoami", "ghost@spooky:~$ ", ["Frontend Wizard"]),
        ("cat skills.txt", "ghost@spooky:~$ ", ["React, TS, Python", "Docker, Node.js"]),
        ("git status", "ghost@spooky:~$ ", ["Branch: main", "Your node is spooky"]),
        ("npm run build", "ghost@spooky:~$ ", ["Brewing Potion...", "Success! [v1.0.0]"]),
        ("sudo summon-octocat", "ghost@spooky:~$ ", ["Summoning...", "Octocat Skeleton rises!"])
    ]
    
    # Compile a sequence of text states
    terminal_states = []
    current_lines = []
    for cmd, prompt, outputs in actions:
        # Type command
        for i in range(len(cmd) + 1):
            terminal_states.append((prompt + cmd[:i], current_lines[-3:])) # Keep last 3 lines
        # Show output
        current_lines.append(prompt + cmd)
        for out in outputs:
            current_lines.append(out)
            # Hold state
            for _ in range(4):
                terminal_states.append((prompt, current_lines[-3:]))
                
    # Pad to 60 frames
    while len(terminal_states) < 60:
        terminal_states.append(terminal_states[-1])
    terminal_states = terminal_states[:60]
    
    for idx, (curr_input, history) in enumerate(terminal_states):
        img = Image.new("RGBA", (360, 180), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Draw Terminal Box
        draw.rectangle([5, 5, 355, 175], fill=(13, 17, 23), outline=(90, 24, 154), width=2)
        # Header bar
        draw.rectangle([6, 6, 354, 25], fill=(36, 0, 70))
        # Control Dots
        draw.ellipse([12, 12, 18, 18], fill=(255, 95, 86))
        draw.ellipse([22, 12, 28, 18], fill=(255, 189, 46))
        draw.ellipse([32, 12, 38, 18], fill=(39, 201, 63))
        
        # Draw History
        y_pos = 35
        for line in history:
            color = (57, 255, 20) if line.startswith("ghost@spooky") else (248, 249, 250)
            if "Success" in line or "Skeleton" in line:
                color = (255, 209, 102)
            draw.text((15, y_pos), line, fill=color)
            y_pos += 20
            
        # Draw Current Input Line
        draw.text((15, y_pos), curr_input, fill=(57, 255, 20))
        # Blinking Cursor
        if idx % 2 == 0:
            cursor_x = 15 + len(curr_input) * 6
            draw.rectangle([cursor_x, y_pos, cursor_x + 6, y_pos + 12], fill=(255, 117, 24))
            
        term_frames.append(img)
    save_transparent_gif(term_frames, "halloween/terminal/terminal.gif", duration=120)

    # 2. Candle Flicker GIF (8 frames)
    candle_frames = []
    for i in range(8):
        img = Image.new("RGBA", (80, 120), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        # Candle pillar
        draw.rectangle([32, 60, 48, 110], fill=(255, 209, 102), outline=(13, 17, 23))
        draw.ellipse([32, 56, 48, 64], fill=(232, 93, 4))
        # Wick
        draw.line([(40, 56), (40, 48)], fill=(13, 17, 23), width=2)
        # Flame swing L/R
        flicker_x = int(3 * math.sin(2 * math.pi * i / 4))
        flame_h = 22 + int(4 * math.cos(2 * math.pi * i / 3))
        draw.polygon([
            (40 + flicker_x, 48 - flame_h), 
            (35, 48), 
            (45, 48)
        ], fill=(255, 117, 24))
        draw.polygon([
            (40 + flicker_x // 2, 48 - int(flame_h * 0.7)), 
            (37, 48), 
            (43, 48)
        ], fill=(255, 209, 102))
        candle_frames.append(img)
    save_transparent_gif(candle_frames, "halloween/animations/candle_flicker.gif", duration=100)

    # 3. Floating Ghost GIF (15 frames)
    ghost_frames = []
    for i in range(15):
        img = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        y_off = int(6 * math.sin(2 * math.pi * i / 15))
        
        # Ghost body
        draw.ellipse([30, 20 + y_off, 70, 60 + y_off], fill=(248, 249, 250))
        draw.rectangle([30, 45 + y_off, 70, 75 + y_off], fill=(248, 249, 250))
        # Waves bottom
        wave = int(3 * math.sin(2 * math.pi * (i / 15 + 0.2)))
        draw.ellipse([27, 72 + y_off + wave, 42, 80 + y_off + wave], fill=(248, 249, 250))
        draw.ellipse([43, 72 + y_off - wave, 57, 80 + y_off - wave], fill=(248, 249, 250))
        draw.ellipse([58, 72 + y_off + wave, 73, 80 + y_off + wave], fill=(248, 249, 250))
        
        # Face L/R
        draw.ellipse([42, 38 + y_off, 46, 44 + y_off], fill=(90, 24, 154))
        draw.ellipse([54, 38 + y_off, 58, 44 + y_off], fill=(90, 24, 154))
        draw.ellipse([47, 50 + y_off, 53, 56 + y_off], fill=(90, 24, 154)) # mouth
        ghost_frames.append(img)
    save_transparent_gif(ghost_frames, "halloween/animations/floating_ghost.gif", duration=90)

    # 4. Pumpkin Glow GIF (12 frames)
    pumpkin_frames = []
    for i in range(12):
        img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        pulse = (math.sin(2 * math.pi * i / 12) + 1.0) / 2.0
        glow_color = (255, 117 + int(92 * pulse), 24 + int(140 * pulse))
        
        # Pumpkin shapes
        draw.ellipse([20, 30, 100, 100], fill=(232, 93, 4))
        draw.ellipse([34, 30, 86, 100], fill=(255, 117, 24))
        draw.ellipse([48, 30, 72, 100], fill=(255, 150, 50))
        # Stem
        draw.polygon([(56, 30), (64, 30), (60, 15)], fill=(36, 0, 70))
        # Face
        draw.polygon([(40, 55), (48, 50), (45, 62)], fill=glow_color)
        draw.polygon([(80, 55), (70, 50), (75, 62)], fill=glow_color)
        draw.polygon([(60, 68), (56, 74), (64, 74)], fill=glow_color)
        draw.polygon([
            (38, 80), (48, 88), (54, 82), (60, 90), (66, 82), (72, 88), (82, 80),
            (74, 94), (66, 90), (60, 96), (54, 90), (46, 94)
        ], fill=glow_color)
        pumpkin_frames.append(img)
    save_transparent_gif(pumpkin_frames, "halloween/animations/pumpkin_glow.gif", duration=100)

    # 5. Copy custom GIFs if they exist in root
    import shutil
    gif_mappings = {
        "Spooky Pumpkin.gif": "halloween/animations/spooky_pumpkin_custom.gif",
        "Halloween Potion.gif": "halloween/animations/halloween_potion_custom.gif",
        "Ghost Halloween.gif": "halloween/animations/ghost_halloween_custom.gif",
        "Halloween Pumpkin Black Cat.gif": "halloween/animations/pumpkin_black_cat_custom.gif"
    }
    for src, dst in gif_mappings.items():
        if os.path.exists(src):
            shutil.copy(src, dst)
            print(f"Copied custom animation {src} to {dst}")
        else:
            print(f"Warning: {src} not found in root, skipping copy.")



# Generate SVGs
def generate_svgs():
    print("Generating premium SVG illustrations...")
    
    # 1. Cinematic Hero Scene (halloween/banner/hero.svg)
    hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 600" width="1280" height="600">
  <defs>
    <radialGradient id="sky-back" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#240046" />
      <stop offset="50%" stop-color="#120124" />
      <stop offset="100%" stop-color="#0d1117" />
    </radialGradient>
    <radialGradient id="glow-lamp" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff7518" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rgb-neon" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff7518" />
      <stop offset="33%" stop-color="#39ff14" />
      <stop offset="66%" stop-color="#5a189a" />
      <stop offset="100%" stop-color="#ff7518" />
    </linearGradient>
    <filter id="m-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="15" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes keys-glow {
      0%, 100% { stroke: #ff7518; filter: drop-shadow(0 0 2px #ff7518); }
      50% { stroke: #39ff14; filter: drop-shadow(0 0 8px #39ff14); }
    }
    @keyframes window-ghost {
      0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.25; }
      50% { transform: translate(5px, -10px) scale(1.05); opacity: 0.4; }
    }
    @keyframes leaves-fall {
      0% { transform: translate(0, -100px) rotate(0deg); opacity: 0; }
      50% { opacity: 0.8; }
      100% { transform: translate(-80px, 600px) rotate(360deg); opacity: 0; }
    }
    .neon-border { animation: keys-glow 4s infinite; }
    .window-ghost-anim { animation: window-ghost 6s ease-in-out infinite; }
    .falling-leaf { animation: leaves-fall 10s linear infinite; }
  </style>

  <!-- Backdrop -->
  <rect width="1280" height="600" rx="16" fill="url(#sky-back)"/>

  <!-- Twinkling Stars -->
  <g fill="#ffd166">
    <circle cx="150" cy="70" r="1.5" opacity="0.8"/>
    <circle cx="380" cy="110" r="2" opacity="0.6"/>
    <circle cx="650" cy="80" r="1" opacity="0.4"/>
    <circle cx="890" cy="60" r="1.5" opacity="0.9"/>
  </g>

  <!-- Large Crescent Moon outside the window -->
  <g transform="translate(150, 80)">
    <circle cx="60" cy="60" r="90" fill="#ffd166" filter="url(#m-glow)"/>
    <circle cx="20" cy="60" r="90" fill="#120124" />
  </g>

  <!-- Haunted Tree outside the window -->
  <path d="M 0 600 L 0 350 C 30 330, 50 280, 70 240 C 90 220, 110 230, 130 190 M 70 240 C 50 210, 20 230, 10 200" fill="none" stroke="#0d1117" stroke-width="12" stroke-linecap="round"/>
  <path d="M 130 190 C 140 180, 160 190, 170 170 C 180 150, 170 120, 160 100" fill="none" stroke="#0d1117" stroke-width="6" stroke-linecap="round"/>

  <!-- Window Frame Silhouette -->
  <rect x="50" y="40" width="300" height="420" rx="150" fill="none" stroke="#0d1117" stroke-width="12"/>
  <line x1="200" y1="40" x2="200" y2="460" stroke="#0d1117" stroke-width="8"/>
  <line x1="50" y1="230" x2="350" y2="230" stroke="#0d1117" stroke-width="8"/>

  <!-- Floating ghost outside the window -->
  <path class="window-ghost-anim" d="M 120 180 C 120 160, 140 160, 140 180 C 140 195, 135 190, 130 200 C 125 190, 120 195, 120 180 Z" fill="#f8f9fa" opacity="0.3"/>

  <!-- Falling leaves decorations -->
  <path class="falling-leaf" d="M 300 0 C 290 20, 310 40, 300 60 L 295 55" fill="#e85d04" style="animation-delay: 0s;"/>
  <path class="falling-leaf" d="M 700 0 C 690 30, 710 50, 700 80 L 695 75" fill="#ff7518" style="animation-delay: 3s;"/>
  <path class="falling-leaf" d="M 1000 0 C 990 20, 1010 40, 1000 60 L 995 55" fill="#5a189a" style="animation-delay: 6s;"/>

  <!-- Programmer Desk surface -->
  <rect x="0" y="480" width="1280" height="120" fill="#0d1117" stroke="#240046" stroke-width="3"/>
  <rect x="50" y="480" width="1180" height="8" fill="#1c1c1c"/>

  <!-- Dual Monitor Setup -->
  <!-- Monitor 1 (Left): VS Code -->
  <g transform="translate(420, 160)">
    <rect width="380" height="240" rx="8" fill="#1c1c1c" stroke="#240046" stroke-width="3"/>
    <rect x="10" y="10" width="360" height="220" rx="4" fill="#0d1117"/>
    <!-- VS Code Sidebar -->
    <rect x="10" y="10" width="30" height="220" fill="#120124"/>
    <circle cx="25" cy="25" r="3" fill="#ff7518"/>
    <circle cx="25" cy="40" r="3" fill="#39ff14"/>
    <!-- VS Code Code Lines -->
    <g transform="translate(55, 25)" stroke-width="3" stroke-linecap="round">
      <line x1="0" y1="5" x2="60" y2="5" stroke="#5a189a"/>
      <line x1="70" y1="5" x2="150" y2="5" stroke="#39ff14"/>
      <line x1="20" y1="20" x2="120" y2="20" stroke="#ff7518"/>
      <line x1="40" y1="35" x2="100" y2="35" stroke="#ffd166"/>
      <line x1="20" y1="50" x2="180" y2="50" stroke="#39ff14"/>
      <line x1="0" y1="65" x2="40" y2="65" stroke="#5a189a"/>
    </g>
    <!-- Stand -->
    <rect x="165" y="240" width="50" height="60" fill="#1c1c1c"/>
    <ellipse cx="190" cy="300" rx="60" ry="10" fill="#1c1c1c"/>
  </g>

  <!-- Monitor 2 (Right): GitHub Window -->
  <g transform="translate(840, 180)">
    <rect width="360" height="220" rx="8" fill="#1c1c1c" stroke="#240046" stroke-width="3"/>
    <rect x="10" y="10" width="340" height="200" rx="4" fill="#0d1117"/>
    <!-- GitHub Contribution Grid mockup -->
    <g transform="translate(30, 40)" fill="#1c1c1c">
      <!-- Labeled rows and squares -->
      <rect x="0" y="0" width="12" height="12" rx="2" fill="#39ff14"/>
      <rect x="16" y="0" width="12" height="12" rx="2" fill="#240046"/>
      <rect x="32" y="0" width="12" height="12" rx="2" fill="#ff7518"/>
      <rect x="48" y="0" width="12" height="12" rx="2" fill="#39ff14"/>
      
      <rect x="0" y="16" width="12" height="12" rx="2" fill="#ff7518"/>
      <rect x="16" y="16" width="12" height="12" rx="2" fill="#39ff14"/>
      <rect x="32" y="16" width="12" height="12" rx="2" fill="#240046"/>
      <rect x="48" y="16" width="12" height="12" rx="2" fill="#ff7518"/>
      
      <rect x="0" y="32" width="12" height="12" rx="2" fill="#240046"/>
      <rect x="16" y="32" width="12" height="12" rx="2" fill="#ff7518"/>
      <rect x="32" y="32" width="12" height="12" rx="2" fill="#39ff14"/>
      <rect x="48" y="32" width="12" height="12" rx="2" fill="#39ff14"/>
    </g>
    <!-- Raven sitting on right monitor -->
    <path d="M 330 0 C 330 -10, 320 -20, 315 -25 C 310 -25, 305 -15, 308 0 C 300 5, 305 15, 310 15 C 315 15, 325 5, 330 0" fill="#0d1117" stroke="#120124" stroke-width="1.5"/>
    <polygon points="302,-2 296,-5 304,3" fill="#ff7518"/> <!-- Beak -->
    <!-- Stand -->
    <rect x="155" y="220" width="50" height="60" fill="#1c1c1c"/>
    <ellipse cx="180" cy="280" rx="50" ry="10" fill="#1c1c1c"/>
  </g>

  <!-- Pumpkin Lamp on Desk -->
  <g transform="translate(1070, 360)">
    <circle cx="60" cy="70" r="100" fill="url(#glow-lamp)"/>
    <ellipse cx="60" cy="90" rx="45" ry="35" fill="#ff7518" stroke="#1c1c1c" stroke-width="3"/>
    <ellipse cx="60" cy="90" rx="28" ry="35" fill="#e85d04" stroke="#1c1c1c" stroke-width="1.5"/>
    <!-- Stem -->
    <path d="M 60 55 C 58 45, 52 40, 50 40 L 55 55" stroke="#1c1c1c" stroke-width="4" fill="none"/>
    <!-- Glowing face -->
    <polygon points="40,80 50,75 45,86" fill="#ffd166"/>
    <polygon points="80,80 70,75 75,86" fill="#ffd166"/>
    <path d="M 38 100 Q 60 115 82 100 Z" fill="#ffd166"/>
  </g>

  <!-- Stacked Spellbooks & Candles L -->
  <g transform="translate(420, 420)">
    <!-- Book 1 (purple) -->
    <rect x="0" y="30" width="110" height="20" rx="3" fill="#5a189a" stroke="#0d1117" stroke-width="2"/>
    <line x1="10" y1="30" x2="10" y2="50" stroke="#ffd166" stroke-width="2"/>
    <!-- Book 2 (red) -->
    <rect x="10" y="12" width="90" height="18" rx="3" fill="#8b0000" stroke="#0d1117" stroke-width="2"/>
    <line x1="20" y1="12" x2="20" y2="30" stroke="#ffd166" stroke-width="2"/>
    <!-- Wax Candle on book -->
    <rect x="40" y="-12" width="16" height="24" fill="#ffd166" stroke="#0d1117" stroke-width="2"/>
    <path d="M 40 -12 Q 44 2, 46 -12" fill="#ffd166"/> <!-- Melted wax -->
    <line x1="48" y1="-12" x2="48" y2="-18" stroke="#0d1117" stroke-width="2"/>
    <!-- Flame -->
    <path d="M 48 -18 C 45 -22, 45 -28, 48 -32 C 51 -28, 51 -22, 48 -18 Z" fill="#ff7518"/>
  </g>

  <!-- RGB Mechanical Keyboard (Center Desk) -->
  <g transform="translate(520, 460)">
    <rect class="neon-border" width="240" height="25" rx="5" fill="#1c1c1c" stroke="url(#rgb-neon)" stroke-width="3"/>
    <!-- Row of keys -->
    <path d="M 10 7 H 230" stroke="#ffd166" stroke-dasharray="6 3" stroke-width="2"/>
    <path d="M 8 16 H 232" stroke="#39ff14" stroke-dasharray="10 4" stroke-width="2"/>
  </g>

  <!-- Coffee Mug with Ghost Steam R -->
  <g transform="translate(790, 435)">
    <rect width="25" height="30" rx="4" fill="#240046" stroke="#f8f9fa" stroke-width="2"/>
    <path d="M 25 6 C 30 6, 32 10, 32 15 C 32 20, 30 24, 25 24" fill="none" stroke="#f8f9fa" stroke-width="2"/>
    <!-- Ghost Steam -->
    <path d="M 12 -5 Q 8 -15, 12 -25 Q 18 -15, 15 -5" fill="#f8f9fa" opacity="0.6"/>
  </g>

  <!-- Witch Hat resting on desk -->
  <g transform="translate(360, 420)">
    <ellipse cx="40" cy="50" rx="45" ry="12" fill="#240046" stroke="#0d1117" stroke-width="2"/>
    <polygon points="10,48 40,10 70,48" fill="#5a189a" stroke="#0d1117" stroke-width="2"/>
    <ellipse cx="40" cy="46" rx="18" ry="4" fill="#ff7518"/>
  </g>

  <!-- Spider Web in L corner -->
  <path d="M 0 0 L 120 0 M 0 0 L 0 120 M 0 0 L 85 85" stroke="#240046" stroke-width="1.5"/>
  <path d="M 30 0 Q 30 30, 0 30 M 60 0 Q 60 60, 0 60 M 90 0 Q 90 90, 0 90" stroke="#240046" stroke-width="1" stroke-dasharray="2 2" fill="none"/>
</svg>"""
    with open("halloween/banner/hero.svg", "w") as f:
        f.write(hero_svg)
    print("Generated halloween/banner/hero.svg")

  # 2. RPG Status Sheet (halloween/stats/rpg_card.svg)
    rpg_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 250" width="450" height="250">
  <defs>
    <radialGradient id="card-back" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#240046" />
      <stop offset="100%" stop-color="#0d1117" />
    </radialGradient>
    <filter id="c-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&amp;family=Outfit:wght@400;700&amp;display=swap');
    .header-style {
      font-family: 'Cinzel', serif;
      fill: #ff7518;
      font-weight: 700;
      font-size: 16px;
      letter-spacing: 2px;
      filter: drop-shadow(0 0 4px #e85d04);
    }
    .text-style {
      font-family: 'Outfit', sans-serif;
      font-size: 13px;
      fill: #f8f9fa;
    }
    .accent-style {
      fill: #39ff14;
      font-weight: bold;
    }
  </style>

  <!-- Frame Background -->
  <rect width="450" height="250" rx="14" fill="url(#card-back)" stroke="#5a189a" stroke-width="2"/>
  <rect x="8" y="8" width="434" height="234" rx="10" fill="none" stroke="#ff7518" stroke-width="1" stroke-dasharray="8 4"/>

  <!-- Gothic Corner Ornaments -->
  <path d="M 12 25 V 12 H 25 M 438 25 V 12 H 425 M 12 225 V 238 H 25 M 438 225 V 238 H 425" stroke="#ffd166" stroke-width="2.5" fill="none"/>

  <text class="header-style" x="225" y="32" text-anchor="middle">🎃 STATUS SHEET 🎃</text>
  <line x1="30" y1="42" x2="420" y2="42" stroke="#240046" stroke-width="2"/>

  <!-- Left: Character info -->
  <g transform="translate(30, 65)">
    <!-- Tiny pumpkin outline -->
    <ellipse cx="40" cy="50" rx="30" ry="25" fill="#ff7518" stroke="#0d1117" stroke-width="1.5"/>
    <path d="M 40 25 L 42 18" stroke="#0d1117" stroke-width="2"/>
    <text class="text-style" x="40" y="95" text-anchor="middle" font-weight="bold">Pumpkin Mage</text>
    <text class="text-style" x="40" y="112" text-anchor="middle" fill="#ffd166">LEVEL 99</text>
  </g>

  <!-- Right: Stats detail -->
  <g transform="translate(160, 65)" class="text-style">
    <!-- Class -->
    <text x="0" y="15">Class: <tspan class="accent-style">Frontend Wizard</tspan></text>
    
    <!-- Mana -->
    <g transform="translate(0, 32)">
      <text x="0" y="15">Mana:</text>
      <rect x="55" y="5" width="160" height="10" rx="5" fill="#120124" stroke="#5a189a"/>
      <rect x="55" y="5" width="160" height="10" rx="5" fill="#39ff14"/>
      <text x="225" y="15" fill="#39ff14" font-weight="bold">MAX</text>
    </g>

    <!-- Bug Slayer -->
    <g transform="translate(0, 62)">
      <text x="0" y="15">Slayer:</text>
      <text x="55" y="15" fill="#ffd166" font-size="14">★★★★★★★★★☆</text>
    </g>

    <!-- Coffee -->
    <g transform="translate(0, 92)">
      <text x="0" y="15">Coffee:</text>
      <text x="55" y="15" fill="#ff7518" font-weight="bold" font-size="16">∞</text>
    </g>

    <!-- Open Source -->
    <g transform="translate(0, 122)">
      <text x="0" y="15">OS Rank:</text>
      <text x="55" y="15" fill="#ffd166" font-weight="bold">LEGENDARY</text>
    </g>
  </g>
</svg>"""
    with open("halloween/stats/rpg_card.svg", "w") as f:
        f.write(rpg_svg)
    print("Generated halloween/stats/rpg_card.svg")

    # 3. Potion Skill Bottles & Spell Cards (halloween/skills/)
    print("Generating Potion Skill System and Spell Cards...")
    skills_data = {
        "react": ("React", 95, "#39ff14", "Light"),
        "ts": ("TypeScript", 90, "#5a189a", "Arcane"),
        "node": ("Node.js", 85, "#7fff00", "Acid"),
        "python": ("Python", 80, "#ffd166", "Venom"),
        "docker": ("Docker", 75, "#240046", "Crate"),
        "k8s": ("Kubernetes", 70, "#e85d04", "Control"),
        "rust": ("Rust", 65, "#8b0000", "Iron"),
        "go": ("Go", 60, "#f8f9fa", "Speed")
    }

    for key, (name, lvl, color, element) in skills_data.items():
        # A. Potion Bottle SVG
        liquid_y = 90 - int(45 * (lvl / 100.0))
        potion_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 120" width="80" height="120" fill="none">
  <!-- Cork -->
  <polygon points="35,10 45,10 42,22 38,22" fill="#ffd166" stroke="#0d1117" stroke-width="1.5"/>
  <!-- Neck -->
  <rect x="36" y="22" width="8" height="15" fill="#f8f9fa" fill-opacity="0.1" stroke="#ffd166" stroke-width="1.5"/>
  <!-- Bottle body -->
  <path d="M 36 37 Q 15 50, 15 85 C 15 110, 65 110, 65 85 Q 65 50, 44 37 Z" fill="#f8f9fa" fill-opacity="0.05" stroke="#ffd166" stroke-width="2"/>
  
  <!-- Liquid Content -->
  <path d="M 16 85 C 16 108, 64 108, 64 85 C 64 78, 60 {liquid_y}, 40 {liquid_y} C 20 {liquid_y}, 16 78, 16 85 Z" fill="{color}" fill-opacity="0.75"/>
  
  <!-- Bubble detail -->
  <circle cx="35" cy="80" r="3" fill="#f8f9fa" opacity="0.6"/>
  <circle cx="48" cy="90" r="4" fill="#f8f9fa" opacity="0.4"/>
  <circle cx="40" cy="70" r="2.5" fill="#f8f9fa" opacity="0.5"/>

  <!-- Text Label -->
  <rect x="15" y="105" width="50" height="12" rx="4" fill="#1c1c1c" stroke="#ffd166" stroke-width="1"/>
  <text x="40" y="114" fill="#ffd166" font-family="monospace" font-size="7" font-weight="bold" text-anchor="middle">{name.upper()}</text>
</svg>"""
        with open(f"halloween/skills/potion_{key}.svg", "w") as f:
            f.write(potion_svg)

        # B. Spell Card SVG
        spell_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 150" width="100" height="150" fill="none">
  <!-- Card Base -->
  <rect width="100" height="150" rx="8" fill="#0d1117" stroke="#ff7518" stroke-width="1.5"/>
  <rect x="5" y="5" width="90" height="140" rx="6" fill="none" stroke="{color}" stroke-opacity="0.3" stroke-width="1"/>
  
  <!-- Runes decoration -->
  <path d="M 12 12 H 25 M 88 12 H 75 M 12 138 H 25 M 88 138 H 75" stroke="{color}" stroke-width="1.5"/>
  
  <!-- Spell Core Icon (Mini Potion shape) -->
  <path d="M 45 40 H 55 V 45 H 45 Z M 42 45 Q 30 65, 30 80 C 30 95, 70 95, 70 80 Q 70 65, 58 45 Z" fill="{color}" fill-opacity="0.2" stroke="{color}" stroke-width="1.5"/>
  
  <!-- Info Text -->
  <text x="50" y="105" fill="#f8f9fa" font-family="monospace" font-weight="bold" font-size="8" text-anchor="middle">{name}</text>
  <text x="50" y="118" fill="{color}" font-family="monospace" font-size="7" text-anchor="middle">Element: {element}</text>
  <text x="50" y="130" fill="#ffd166" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">PWR {lvl}%</text>
</svg>"""
        with open(f"halloween/skills/spell_{key}.svg", "w") as f:
            f.write(spell_svg)

    # 4. Contribution Graveyard Frame (halloween/stats/graveyard_frame.svg)
    graveyard_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 200" width="850" height="200">
  <defs>
    <linearGradient id="column-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#240046" />
      <stop offset="100%" stop-color="#0d1117" />
    </linearGradient>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&amp;display=swap');
    .graveyard-title {
      font-family: 'Creepster', cursive;
      font-size: 28px;
      fill: #ff7518;
      letter-spacing: 4px;
      filter: drop-shadow(0 0 8px #ff7518);
    }
  </style>

  <!-- Left Column -->
  <g transform="translate(10, 10)">
    <rect width="40" height="180" rx="4" fill="url(#column-grad)" stroke="#ff7518" stroke-width="2"/>
    <path d="M 0 30 H 40 M 0 150 H 40" stroke="#ff7518" stroke-width="1.5"/>
    <path d="M 10 30 V 150" stroke="#ff7518" stroke-width="1" stroke-dasharray="3 3"/>
    <!-- Pumpkin at base -->
    <ellipse cx="20" cy="170" rx="14" ry="10" fill="#e85d04" stroke="#0d1117"/>
    <path d="M 20 160 Q 22 155, 20 160" stroke="#0d1117" stroke-width="2"/>
  </g>

  <!-- Right Column -->
  <g transform="translate(800, 10)">
    <rect width="40" height="180" rx="4" fill="url(#column-grad)" stroke="#ff7518" stroke-width="2"/>
    <path d="M 0 30 H 40 M 0 150 H 40" stroke="#ff7518" stroke-width="1.5"/>
    <path d="M 30 30 V 150" stroke="#ff7518" stroke-width="1" stroke-dasharray="3 3"/>
    <ellipse cx="20" cy="170" rx="14" ry="10" fill="#e85d04" stroke="#0d1117"/>
  </g>

  <!-- Top Gothic Arch frame -->
  <path d="M 50 40 C 200 15, 650 15, 800 40" fill="none" stroke="#ff7518" stroke-width="4"/>
  <path d="M 50 50 C 200 25, 650 25, 800 50" fill="none" stroke="#5a189a" stroke-width="1.5" stroke-dasharray="4 4"/>
  
  <text class="graveyard-title" x="425" y="48" text-anchor="middle">🪦 THE ANCIENT GRAVEYARD 🪦</text>

  <!-- Bottom vines -->
  <path d="M 50 185 C 200 195, 650 195, 800 185" fill="none" stroke="#7fff00" stroke-width="2"/>
</svg>"""
    with open("halloween/stats/graveyard_frame.svg", "w") as f:
        f.write(graveyard_svg)
    print("Generated halloween/stats/graveyard_frame.svg")

    # 5. Featured Projects Spellbook cards (halloween/projects/)
    print("Generating Project Spellbooks...")
    projects_data = {
        "spellcaster": ("spellcaster-compiler", "TS/JS AST compiler for reactive spells.", "#5a189a"),
        "cauldron": ("cauldron-db", "Lightweight NoSQL key-value cache recipe book.", "#39ff14")
    }
    
    for key, (title, desc, color) in projects_data.items():
        spellbook_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 220" width="420" height="220" fill="none">
  <!-- Open Book Base -->
  <path d="M 10 200 Q 205 180, 205 20 C 205 20, 105 15, 10 25 Z" fill="#240046" stroke="#ff7518" stroke-width="2"/>
  <path d="M 410 200 Q 215 180, 215 20 C 215 20, 315 15, 410 25 Z" fill="#0d1117" stroke="#ff7518" stroke-width="2"/>
  
  <!-- Left Page Cover details with Wax Seal -->
  <g transform="translate(30, 40)">
    <rect width="140" height="120" rx="6" fill="#120124" stroke="{color}" stroke-width="1.5"/>
    <!-- Runes -->
    <path d="M 15 15 H 35 M 15 15 V 35 M 125 15 H 105 M 125 15 V 35 M 15 105 H 35 M 15 105 V 85 M 125 105 H 105 M 125 105 V 85" stroke="{color}" stroke-width="1"/>
    <!-- Wax Seal -->
    <circle cx="70" cy="60" r="16" fill="#8b0000" stroke="#0d1117" stroke-width="1.5"/>
    <text x="70" y="65" fill="#ff7518" font-family="monospace" font-weight="bold" font-size="14" text-anchor="middle">RIP</text>
  </g>

  <!-- Right Page details -->
  <g transform="translate(235, 40)">
    <!-- Title -->
    <text x="0" y="20" fill="#ff7518" font-family="monospace" font-weight="bold" font-size="14">{title}</text>
    <!-- Description -->
    <foreignObject x="0" y="35" width="160" height="80">
      <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: monospace; color: #f8f9fa; font-size: 11px; line-height: 1.4;">
        {desc}
      </div>
    </foreignObject>
    <!-- Wax ribbon tag -->
    <rect x="0" y="115" width="70" height="18" rx="4" fill="{color}" fill-opacity="0.1" stroke="{color}"/>
    <text x="35" y="127" fill="{color}" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">ENCHANTED</text>
  </g>
</svg>"""
        with open(f"halloween/projects/spellbook_{key}.svg", "w") as f:
            f.write(spellbook_svg)

    # 6. Achievement Relics (halloween/badges/)
    print("Generating Achievement Relics...")
    relics = {
        "orb": ("Crystal Orb", "#39ff14", "M 50 15 C 25 15, 20 40, 20 60 C 20 80, 40 95, 50 95 C 60 95, 80 80, 80 60 C 80 40, 75 15, 50 15 Z"),
        "skull": ("Skull Trophy", "#f8f9fa", "M 35 40 Q 35 15, 50 15 Q 65 15, 65 40 C 65 55, 60 60, 60 70 L 40 70 C 40 60, 35 55, 35 40 Z"),
        "crown": ("Ancient Crown", "#ffd166", "M 20 70 L 30 30 L 50 50 L 70 30 L 80 70 Z"),
        "candle": ("Haunted Candle", "#e85d04", "M 42 40 H 58 V 80 H 42 Z"),
        "staff": ("Magic Staff", "#5a189a", "M 48 20 H 52 V 90 H 48 Z"),
        "pumpkin": ("Golden Pumpkin", "#ff7518", "M 50 85 C 25 85, 20 60, 20 50 C 20 40, 35 25, 50 25 C 65 25, 80 40, 80 50 C 80 60, 75 85, 50 85 Z")
    }
    
    for key, (name, color, path_data) in relics.items():
        relic_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 120" width="100" height="120" fill="none">
  <!-- Pedestal stand -->
  <path d="M 25 100 H 75 L 60 85 H 40 Z" fill="#1c1c1c" stroke="#ff7518" stroke-width="2"/>
  
  <!-- Relic shape -->
  <path d="{path_data}" fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="2.5" style="filter: drop-shadow(0 0 4px {color});"/>
  
  <!-- Small glowing particles -->
  <circle cx="50" cy="50" r="2" fill="#ffd166"/>
  <circle cx="35" cy="45" r="1.5" fill="#f8f9fa"/>
  <circle cx="65" cy="55" r="1" fill="#f8f9fa"/>
  
  <!-- Title label -->
  <text x="50" y="114" fill="#ffd166" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">{name.upper()}</text>
</svg>"""
        with open(f"halloween/badges/relic_{key}.svg", "w") as f:
            f.write(relic_svg)

    # 7. Premium SVG Dividers
    print("Generating Dividers...")
    
    # Vines Divider
    vines = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 80" width="100%" height="80" fill="none">
  <path d="M 0 40 C 150 10, 300 70, 450 40 C 600 10, 750 70, 900 40 C 1050 10, 1200 40, 1200 40" stroke="#7fff00" stroke-width="4" stroke-linecap="round"/>
  <path d="M 120 32 Q 130 15, 145 28 Z" fill="#240046" stroke="#7fff00" stroke-width="1.5"/>
  <path d="M 520 48 Q 530 65, 545 52 Z" fill="#240046" stroke="#7fff00" stroke-width="1.5"/>
  <path d="M 820 32 Q 830 15, 845 28 Z" fill="#240046" stroke="#7fff00" stroke-width="1.5"/>
  <line x1="280" y1="48" x2="285" y2="60" stroke="#7fff00" stroke-width="2"/>
  <line x1="700" y1="32" x2="695" y2="20" stroke="#7fff00" stroke-width="2"/>
</svg>"""
    with open("halloween/dividers/vines.svg", "w") as f:
        f.write(vines)

    # Gothic Arches Divider
    gothic_arches = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 60" width="100%" height="60" fill="none">
  <path d="M 0 50 Q 75 0, 150 50 Q 225 0, 300 50 Q 375 0, 450 50 Q 525 0, 600 50 Q 675 0, 750 50 Q 825 0, 900 50 Q 975 0, 1050 50 Q 1125 0, 1200 50" stroke="#ff7518" stroke-width="2.5"/>
  <path d="M 0 55 Q 75 10, 150 55 Q 225 10, 300 55 Q 375 10, 450 55 Q 525 10, 600 55 Q 675 10, 750 55 Q 825 10, 900 55 Q 975 10, 1050 55 Q 1125 10, 1200 55" stroke="#240046" stroke-width="1.5"/>
</svg>"""
    with open("halloween/dividers/gothic_arches.svg", "w") as f:
        f.write(gothic_arches)

    # Magic Circle Divider
    magic_circle = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 80" width="100%" height="80" fill="none">
  <!-- Line connecting center circles -->
  <line x1="0" y1="40" x2="1200" y2="40" stroke="#5a189a" stroke-width="2" stroke-dasharray="10 15"/>
  <!-- L Magic Circle -->
  <g transform="translate(300, 40)">
    <circle cx="0" cy="0" r="25" stroke="#ff7518" stroke-width="2"/>
    <circle cx="0" cy="0" r="18" stroke="#ff7518" stroke-width="1" stroke-dasharray="4 2"/>
    <polygon points="0,-18 15,10 -15,10" stroke="#ffd166" stroke-width="1"/>
    <polygon points="0,18 15,-10 -15,-10" stroke="#ffd166" stroke-width="1"/>
  </g>
  <!-- R Magic Circle -->
  <g transform="translate(900, 40)">
    <circle cx="0" cy="0" r="25" stroke="#ff7518" stroke-width="2"/>
    <circle cx="0" cy="0" r="18" stroke="#ff7518" stroke-width="1" stroke-dasharray="4 2"/>
    <polygon points="0,-18 15,10 -15,10" stroke="#ffd166" stroke-width="1"/>
    <polygon points="0,18 15,-10 -15,-10" stroke="#ffd166" stroke-width="1"/>
  </g>
</svg>"""
    with open("halloween/dividers/magic_circle.svg", "w") as f:
        f.write(magic_circle)

    # Web Divider
    webs = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 80" width="100%" height="80" fill="none">
  <path d="M 0 10 Q 150 40, 300 10 Q 450 40, 600 10 Q 750 40, 900 10 Q 1050 40, 1200 10" stroke="#5a189a" stroke-width="2"/>
  <path d="M 0 22 Q 150 52, 300 22 Q 450 52, 600 22 Q 750 52, 900 22 Q 1050 52, 1200 22" stroke="#5a189a" stroke-width="1.5" stroke-dasharray="3 3"/>
</svg>"""
    with open("halloween/dividers/webs.svg", "w") as f:
        f.write(webs)

    # 8. Reusable Background Patterns (halloween/backgrounds/spooky_pattern.svg)
    print("Generating Background Patterns...")
    bg_pattern = """<svg xmlns="http://www.w3.org/2000/svg" width="60" height="60" viewBox="0 0 60 60">
  <rect width="60" height="60" fill="#0d1117"/>
  <!-- Tiny ghost outlines -->
  <g stroke="#240046" stroke-width="1" fill="none" opacity="0.25">
    <path d="M 10 20 C 10 10, 20 10, 20 20 C 20 25, 18 23, 15 25 C 12 23, 10 25, 10 20 Z"/>
    <!-- Mini star -->
    <path d="M 45 40 L 47 43 L 50 43 L 48 45 L 49 48 L 45 46 L 41 48 L 42 45 L 40 43 L 43 43 Z"/>
  </g>
</svg>"""
    with open("halloween/backgrounds/spooky_pattern.svg", "w") as f:
        f.write(bg_pattern)

    # 9. Spooky Forest Footer (halloween/footer/footer.svg)
    print("Generating Spooky Footer...")
    footer_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 200" width="1280" height="200">
  <defs>
    <linearGradient id="sky-dark" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#120124" />
      <stop offset="100%" stop-color="#0d1117" />
    </linearGradient>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Creepster&amp;display=swap');
    .footer-quote {
      font-family: 'Creepster', cursive;
      font-size: 24px;
      fill: #ff7518;
      letter-spacing: 2px;
      filter: drop-shadow(0 0 6px #e85d04);
    }
  </style>

  <!-- Sky background -->
  <rect width="1280" height="200" fill="url(#sky-dark)"/>

  <!-- Haunted Forest Silhouettes -->
  <g fill="#0d1117" stroke="#000" stroke-width="1">
    <!-- Tree 1 -->
    <polygon points="100,200 130,80 160,200"/>
    <polygon points="115,140 130,50 145,140"/>
    
    <!-- Tree 2 -->
    <polygon points="250,200 270,110 290,200"/>
    
    <!-- Tree 3 -->
    <polygon points="900,200 930,90 960,200"/>
    <polygon points="915,130 930,60 945,130"/>

    <!-- Tree 4 -->
    <polygon points="1100,200 1120,100 1140,200"/>
  </g>

  <!-- Ground -->
  <rect y="180" width="1280" height="20" fill="#0d1117"/>

  <!-- Quote -->
  <text class="footer-quote" x="640" y="110" text-anchor="middle">"Every line of code tells a story."</text>

  <!-- Small bats -->
  <path d="M 300 40 Q 310 20, 315 35 Q 320 20, 330 40 Q 315 45, 300 40 Z" fill="#0d1117"/>
  <path d="M 850 50 Q 860 30, 865 45 Q 870 30, 880 50 Q 865 55, 850 50 Z" fill="#0d1117"/>
</svg>"""
    with open("halloween/footer/footer.svg", "w") as f:
        f.write(footer_svg)
    print("Generated halloween/footer/footer.svg")


# Generate README.md with Story sections
def generate_readme():
    print("Writing upgraded README.md...")
    username = "CharanBS18"
    email = "charan201204@gmail.com"
    
    readme_content = f"""<h1 align="center">🔮 THE GRIMOIRE ACCESS NODE // {username.upper()} 🔮</h1>

<p align="center">
  <img alt="Premium Spooky Halloween Workspace Hero" src="halloween/banner/hero.svg" width="100%">
</p>

<!-- Spooky Decorative Panel -->
<p align="center">
  <img src="halloween/dividers/webs.svg" width="100%">
</p>

<!-- Story Section 1: The Legend -->
<a id="legend"></a>
<h2 align="center">📜 THE LEGEND</h2>

<table align="center" border="0" cellpadding="15" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto; background-color: #0d1117;">
  <tr style="border: 0px;">
    <!-- Profile Frame with spooky avatar overlay -->
    <td align="center" valign="middle" style="border: 0px; padding: 10px; width: 40%;">
      <div style="position: relative; display: inline-block; width: 240px; height: 280px;">
        <img src="halloween/stickers/user_avatar.png" alt="Spooky Avatar" width="160" style="position: absolute; top: 40px; left: 40px; z-index: 1; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));">
        <img src="halloween/frames/profile_frame.svg" alt="Tombstone Frame" width="240" style="position: absolute; top: 0; left: 0; z-index: 2; pointer-events: none;">
        <!-- Spooky Pumpkin custom GIF at bottom-right of tombstone -->
        <img src="halloween/animations/spooky_pumpkin_custom.gif" alt="Spooky Pumpkin Animation" width="80" style="position: absolute; bottom: -5px; right: -5px; z-index: 3;">
      </div>
    </td>
    <!-- Bio Monospace Details -->
    <td valign="top" style="border: 0px; padding: 20px; width: 60%; font-family: monospace; color: #f8f9fa;">
      <div style="float: right; margin-left: 10px; transform: rotate(-5deg); filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4));" title="The Warlock at the Spooky House (Sticker 12)">
        <img src="halloween/stickers/sticker_12.png" width="95" alt="Warlock Haunted House">
      </div>
      <div style="float: left; margin-right: 10px; transform: rotate(5deg); filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4));" title="Friendly Warlock with familiar cat (Sticker 11)">
        <img src="halloween/stickers/sticker_11.png" width="90" alt="Warlock with Cat">
      </div>
      <h3 style="color: #ff7518; margin-top: 0;">&gt; COFFIN_NODE.conf</h3>
      <p><b>&gt; IDENTITY:</b> Charan BS / @{username}</p>
      <p><b>&gt; ACCESS_PORT:</b> <a href="mailto:{email}" style="color: #39ff14;">{email}</a></p>
      <p><b>&gt; ALIGNMENT:</b> <code style="color: #ffd166;">Frontend Wizard [Level 99]</code></p>
      <hr style="border: 1px solid #240046; opacity: 0.8; margin: 15px 0;">
      <p style="line-height: 1.6; color: #f8f9fa; clear: both;">
        Welcome, mortal visitor, to the spectral repository node. I craft responsive, high-performance web structures using midnight potions, green slime, and dark-mode coding rituals. I believe in clean code, robust architectures, and pixel-perfect design craftsmanship.
      </p>
    </td>
  </tr>
</table>

<p align="center">
  <img src="halloween/dividers/gothic_arches.svg" width="100%">
</p>

<!-- Story Section 2: Potion Ingredients (Skills) -->
<a id="potion-ingredients"></a>
<h2 align="center">🧪 POTION INGREDIENTS</h2>

<!-- Potion bottle skills grids -->
<p align="center">
  <!-- Potion Drinking Warlock (Sticker 17) -->
  <img src="halloween/stickers/sticker_17.png" width="95" style="transform: rotate(-6deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4)); vertical-align: middle; margin-right: 15px;" alt="Potion Drinker" title="Warlock drinking from potion bottle (Sticker 17)">
  
  <img src="halloween/skills/potion_react.svg" width="85" alt="React">
  <img src="halloween/skills/potion_ts.svg" width="85" alt="TypeScript">
  <img src="halloween/skills/potion_node.svg" width="85" alt="Node.js">
  <img src="halloween/skills/potion_python.svg" width="85" alt="Python">

  <!-- Custom Potion GIF -->
  <img src="halloween/animations/halloween_potion_custom.gif" width="90" style="vertical-align: middle; margin: 0 10px;" alt="Custom Bubbling Potion" title="Brewing Potion magic">

  <img src="halloween/skills/potion_docker.svg" width="85" alt="Docker">
  <img src="halloween/skills/potion_k8s.svg" width="85" alt="Kubernetes">
  <img src="halloween/skills/potion_rust.svg" width="85" alt="Rust">
  <img src="halloween/skills/potion_go.svg" width="85" alt="Go">
  
  <!-- Spell Casting Warlock (Sticker 14) -->
  <img src="halloween/stickers/sticker_14.png" width="95" style="transform: rotate(6deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4)); vertical-align: middle; margin-left: 15px;" alt="Spell Caster" title="Warlock casting magic spell (Sticker 14)">
</p>

<!-- Spell cards details -->
<table align="center" border="0" cellpadding="10" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto;">
  <tr style="border: 0px;">
    <td style="border: 0px;"><img src="halloween/skills/spell_react.svg" width="100"></td>
    <td style="border: 0px;"><img src="halloween/skills/spell_ts.svg" width="100"></td>
    <td style="border: 0px;"><img src="halloween/skills/spell_node.svg" width="100"></td>
    <td style="border: 0px;"><img src="halloween/skills/spell_python.svg" width="100"></td>
  </tr>
</table>

<p align="center">
  <img src="halloween/dividers/magic_circle.svg" width="100%">
</p>

<!-- Story Section 3: Haunted Laboratory (Current Work) -->
<a id="haunted-laboratory"></a>
<h2 align="center">🕯 HAUNTED LABORATORY</h2>

<table align="center" border="0" cellpadding="15" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto; background-color: #0d1117;">
  <tr style="border: 0px;">
    <!-- Terminal GIF -->
    <td align="center" valign="middle" style="border: 0px; padding: 10px; width: 45%;">
      <img src="halloween/terminal/terminal.gif" alt="Haunted Terminal typing" width="100%" style="max-width: 360px;">
    </td>
    <!-- Status Text -->
    <td valign="top" style="border: 0px; padding: 20px; width: 55%; font-family: monospace; color: #f8f9fa; line-height: 1.6;">
      <!-- Warlock exploring with a lantern (Sticker 13) -->
      <div style="float: right; transform: rotate(4deg); filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4)); margin-left: 10px;" title="Warlock exploring with lantern (Sticker 13)">
        <img src="halloween/stickers/sticker_13.png" width="90" alt="Lantern Explorer">
      </div>
      <!-- Frankenstein's Monster Lab Creation (Sticker 6) -->
      <div style="float: left; transform: rotate(-5deg); filter: drop-shadow(0 4px 6px rgba(0,0,0,0.45)); margin-right: 10px;" title="Lab Creation Frankenstein (Sticker 6)">
        <img src="halloween/stickers/sticker_6.png" width="85" alt="Frankenstein Creation">
      </div>
      <h3 style="color: #ff7518; margin-top: 0; clear: both;">&gt; ACTIVE_EXPERIMENT.bin</h3>
      <p><b>&gt; STATUS:</b> Brewing spell-check algorithms</p>
      <p><b>&gt; OBJECTIVE:</b> Building lightweight, pixel-perfect layout nodes</p>
      <p><b>&gt; INGREDIENTS:</b> <code>TailwindCSS</code> <code>Next.js</code> <code>Pillow</code></p>
      
      <!-- Custom Lab Mascot (Sticker Pumpkin + Cat GIF) -->
      <p align="center" style="margin-top: 15px; margin-bottom: 0;">
        <img src="halloween/animations/pumpkin_black_cat_custom.gif" width="80" alt="Lab Mascot Pumpkin Cat" title="Lab Mascot Pumpkin & Cat">
      </p>
    </td>
  </tr>
</table>

<p align="center">
  <img src="halloween/dividers/vines.svg" width="100%">
</p>

<!-- Story Section 4: Spellbook (Projects) -->
<a id="spellbook"></a>
<h2 align="center">📖 SPELLBOOK</h2>

<table align="center" border="0" cellpadding="15" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto; width: 100%; max-width: 900px;">
  <tr style="border: 0px;">
    <!-- Project 1 Spellbook Card -->
    <td valign="top" style="border: 0px; width: 50%; padding: 15px; text-align: center;">
      <img src="halloween/projects/spellbook_spellcaster.svg" width="100%" alt="spellcaster-compiler Book">
      <br>
      <!-- Warlock riding broomstick (Sticker 10) -->
      <img src="halloween/stickers/sticker_10.png" width="115" style="transform: rotate(-6deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4)); margin-top: 15px;" alt="Warlock Broom Ride" title="Warlock riding broom (Sticker 10)">
    </td>
    <!-- Project 2 Spellbook Card -->
    <td valign="top" style="border: 0px; width: 50%; padding: 15px; text-align: center;">
      <img src="halloween/projects/spellbook_cauldron.svg" width="100%" alt="cauldron-db Book">
      <br>
      <!-- Witch riding broomstick (Sticker 3) -->
      <img src="halloween/stickers/sticker_3.png" width="115" style="transform: rotate(6deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4)); margin-top: 15px;" alt="Witch Broom Ride" title="Witch riding broom (Sticker 3)">
    </td>
  </tr>
</table>

<p align="center">
  <img src="halloween/dividers/webs.svg" width="100%">
</p>

<!-- Story Section 5: Ancient Relics (Achievements) -->
<a id="ancient-relics"></a>
<h2 align="center">🏆 ANCIENT RELICS</h2>

<p align="center">
  <!-- Warlock surrounded by pumpkins / trophies (Sticker 16) -->
  <img src="halloween/stickers/sticker_16.png" width="100" style="transform: rotate(-5deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); vertical-align: middle; margin-right: 25px;" alt="Pumpkin Relics" title="Warlock and jack-o'-lanterns trophy display (Sticker 16)">
  
  <img src="halloween/badges/relic_orb.svg" width="90" alt="Crystal Orb">
  <img src="halloween/badges/relic_skull.svg" width="90" alt="Skull Trophy">
  <img src="halloween/badges/relic_crown.svg" width="90" alt="Ancient Crown">
  <img src="halloween/badges/relic_candle.svg" width="90" alt="Haunted Candle">
  <img src="halloween/badges/relic_staff.svg" width="90" alt="Magic Staff">
  <img src="halloween/badges/relic_pumpkin.svg" width="90" alt="Golden Pumpkin">
</p>

<p align="center">
  <img src="halloween/dividers/gothic_arches.svg" width="100%">
</p>

<!-- Story Section 6: Moonlit Activity (Stats & Contributions) -->
<a id="moonlit-activity"></a>
<h2 align="center">🌙 MOONLIT ACTIVITY</h2>

<table align="center" border="0" cellpadding="10" cellspacing="0" style="border: 0px; border-collapse: collapse; margin: 0px auto;">
  <tr style="border: 0px;">
    <!-- Character RPG Status Card -->
    <td align="center" valign="middle" style="border: 0px; padding: 10px;">
      <img src="halloween/stats/rpg_card.svg" alt="Mage Character Card" width="440">
      <br>
      <!-- Warlock running away from ghost (Sticker 15) -->
      <img src="halloween/stickers/sticker_15.png" width="105" style="transform: rotate(-5deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4)); margin-top: 15px;" alt="Running from Ghost" title="Warlock running from ghost (Sticker 15)">
    </td>
    <!-- Commits and languages grids -->
    <td align="center" valign="middle" style="border: 0px; padding: 10px;">
      <div style="position: relative; display: inline-block;">
        <img src="stats.svg" alt="Stats Summary" width="400" style="border: 2px solid #ff7518; border-radius: 8px;">
        <img src="halloween/animations/pumpkin_glow.gif" alt="Glowing Pumpkin" width="65" style="position: absolute; top: -25px; left: -25px;">
      </div>
      <br>
      <!-- Werewolf howling at the moon (Sticker 7) -->
      <img src="halloween/stickers/sticker_7.png" width="105" style="transform: rotate(5deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4)); margin-top: 15px;" alt="Howling Werewolf" title="Werewolf howling at moon (Sticker 7)">
    </td>
  </tr>
</table>

<!-- Graveyard Wrapped Contribution Graph -->
<p align="center" style="margin-top: 40px; position: relative; max-width: 860px; margin-left: auto; margin-right: auto;">
  <!-- Custom Ghost floating over graveyard (Ghost Halloween GIF) -->
  <img src="halloween/animations/ghost_halloween_custom.gif" width="75" style="position: absolute; top: -35px; right: 20px; z-index: 10;" alt="Graveyard Ghost" title="Graveyard Guardian Ghost">
  <!-- Contribution Graveyard Arch frame -->
  <img src="halloween/stats/graveyard_frame.svg" alt="Graveyard Frame" width="100%" style="display: block;">
</p>
<p align="center" style="margin-top: -125px; padding-bottom: 50px; width: 100%;">
  <!-- Contribution grid snake game (offset behind columns) -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg?v=2">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake-light.svg?v=2">
    <img alt="GitHub Snake Game" src="https://raw.githubusercontent.com/{username}/{username}/output/github-contribution-grid-snake.svg?v=2" width="85%">
  </picture>
</p>

<!-- Trophies Display -->
<p align="center" style="margin-top: 20px;">
  <img src="trophies.svg" alt="Trophies display" width="100%" style="max-width: 850px; border: 2px solid #5a189a; border-radius: 8px;">
</p>

<p align="center">
  <img src="halloween/dividers/magic_circle.svg" width="100%">
</p>

<!-- Story Section 6.5: Familiar Spirits (Collage of all remaining stickers) -->
<a id="familiar-spirits"></a>
<h2 align="center">🦇 FAMILIAR SPIRITS</h2>
<p align="center" style="font-family: monospace; color: #cbd5e1; font-size: 13px;">
  The many spectral forms and familiars conjured inside this Halloween code capsule:
</p>
<p align="center" style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; max-width: 900px; margin: 20px auto;">
  <img src="halloween/stickers/sticker_1.png" width="105" style="transform: rotate(-4deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin: 10px;" alt="Ghost Sticker" title="Floating ghost (Sticker 1)">
  <img src="halloween/stickers/sticker_2.png" width="105" style="transform: rotate(5deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin: 10px;" alt="Vampire Sticker" title="Vampire warlock (Sticker 2)">
  <img src="halloween/stickers/sticker_4.png" width="105" style="transform: rotate(-6deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin: 10px;" alt="Skeleton Sticker" title="Spooky skeleton (Sticker 4)">
  <img src="halloween/stickers/sticker_5.png" width="105" style="transform: rotate(3deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin: 10px;" alt="Mummy Sticker" title="Bandage mummy (Sticker 5)">
  <img src="halloween/stickers/sticker_8.png" width="105" style="transform: rotate(-3deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin: 10px;" alt="Zombie Sticker" title="Green zombie (Sticker 8)">
  <img src="halloween/stickers/sticker_9.png" width="105" style="transform: rotate(4deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin: 10px;" alt="Trick or Treat Sticker" title="Trick-or-treat candy bucket (Sticker 9)">
  <img src="halloween/stickers/sticker_19.png" width="105" style="transform: rotate(-5deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin: 10px;" alt="Pumpkin Warlock Sticker" title="Warlock with jack-o'-lantern (Sticker 19)">
</p>

<p align="center">
  <img src="halloween/dividers/bats.svg" width="100%">
</p>

<!-- Story Section 7: Raven Mail (Contact) -->
<a id="raven-mail"></a>
<h2 align="center">📮 RAVEN MAIL</h2>

<p align="center" style="display: flex; justify-content: center; align-items: center; margin-top: 30px;">
  <!-- Waving Warlock with speech bubble (Sticker 18) -->
  <img src="halloween/stickers/sticker_18.png" width="105" style="transform: rotate(-5deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin-right: 15px;" alt="Happy Halloween Mascot" title="Waving Happy Halloween! (Sticker 18)">
  
  <a href="mailto:{email}" style="display: inline-block; background-color: #240046; color: #ff7518; border: 2px solid #ff7518; padding: 12px 24px; border-radius: 6px; text-decoration: none; font-weight: bold; font-family: monospace; height: fit-content; align-self: center;">
    📧 SEND RAVEN SUMMONS
  </a>
  
  <!-- Warlock with familiar cat and bats (Sticker 20) -->
  <img src="halloween/stickers/sticker_20.png" width="105" style="transform: rotate(5deg); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.45)); margin-left: 15px;" alt="Summons Mascot" title="Warlock with familiar cat (Sticker 20)">
</p>

<!-- Spooky Forest Footer -->
<p align="center" style="margin-top: 70px;">
  <img src="halloween/footer/footer.svg" width="100%">
</p>

<p align="center" style="font-family: monospace; color: #5a189a; font-size: 11px;">
  PORTAL SECURED VISITORS: <img src="https://profile-counter.glitch.me/{username}/count.svg" alt="Views Counter" style="vertical-align: middle;"> // SECURE CONNECTIONS COMPLETED // STAY SPOOKY 🎃
</p>
"""
    with open("README.md", "w") as f:
        f.write(readme_content)
    print("Upgraded README.md written successfully.")


def main():
    setup_dirs()
    crop_stickers()
    generate_animations()
    generate_svgs()
    generate_readme()
    print("All upgraded spooky assets built successfully!")


if __name__ == "__main__":
    main()
