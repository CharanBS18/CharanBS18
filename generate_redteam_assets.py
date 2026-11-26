import os
import math
import glob
from collections import deque
from PIL import Image, ImageDraw


def setup_dirs():
    dirs = [
        "redteam",
        "redteam/banner",
        "redteam/dividers",
        "redteam/frames",
        "redteam/projects",
        "redteam/badges",
        "redteam/animations",
        "redteam/footer",
        "redteam/terminal",
        "redteam/skills",
        "redteam/stats",
        "redteam/stickers",
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print("Red Team directory structure initialized.")


def remove_white_background(img, threshold=235):
    """Flood-fill remove contiguous near-white background from the image edges."""
    img = img.convert("RGBA")
    w, h = img.size
    pix = img.load()
    visited = [[False] * h for _ in range(w)]
    queue = deque()

    def is_bg(r, g, b, a):
        return a < 20 or (r >= threshold and g >= threshold and b >= threshold)

    # Seed from all 4 borders
    for x in range(w):
        for y in (0, h - 1):
            r, g, b, a = pix[x, y]
            if is_bg(r, g, b, a) and not visited[x][y]:
                visited[x][y] = True
                queue.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            r, g, b, a = pix[x, y]
            if is_bg(r, g, b, a) and not visited[x][y]:
                visited[x][y] = True
                queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()
        pix[cx, cy] = (0, 0, 0, 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                r, g, b, a = pix[nx, ny]
                if is_bg(r, g, b, a):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    # Soften 1px fringe around removed background
    fringe = []
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            r, g, b, a = pix[x, y]
            if a > 0 and r >= 220 and g >= 220 and b >= 220:
                if any(pix[x + dx, y + dy][3] == 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    fringe.append((x, y, r, g, b))
    for x, y, r, g, b in fringe:
        pix[x, y] = (r, g, b, 90)

    return img


def process_stickers_and_avatar():
    print("Processing operator avatar and Red Team stickers...")
    # 1. Operator Avatar from avatar.png (headshot) or chtransparent.png
    avatar_src = "avatar.png" if os.path.exists("avatar.png") else "chtransparent.png"
    if os.path.exists(avatar_src):
        img = Image.open(avatar_src).convert("RGBA")
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        # Circular mask so it fits cleanly inside the biometric HUD target-lock reticle
        size = min(img.size)
        left = (img.width - size) // 2
        top = (img.height - size) // 2
        img = img.crop((left, top, left + size, top + size)).resize((180, 180), Image.Resampling.LANCZOS)

        mask = Image.new("L", (180, 180), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.ellipse((2, 2, 178, 178), fill=255)
        out = Image.new("RGBA", (180, 180), (0, 0, 0, 0))
        out.paste(img, (0, 0), mask)
        out.save("redteam/stickers/user_avatar.png")
        print(f"Saved circular operator avatar from {avatar_src} -> redteam/stickers/user_avatar.png")
    else:
        print("Warning: neither avatar.png nor chtransparent.png found.")

    # 2. Process generated raw_* stickers into clean transparent cutouts
    raw_files = sorted(glob.glob("redteam/stickers/raw_*.png") + glob.glob("redteam/stickers/raw_*.jpg"))
    for raw_path in raw_files:
        base = os.path.splitext(os.path.basename(raw_path).replace("raw_", ""))[0] + ".png"
        dst_path = os.path.join("redteam/stickers", base)
        img = Image.open(raw_path)
        cleaned = remove_white_background(img, threshold=232)
        bbox = cleaned.getbbox()
        if bbox:
            cleaned = cleaned.crop(bbox)
        cleaned.thumbnail((320, 320), Image.Resampling.LANCZOS)
        cleaned.save(dst_path)
        print(f"Processed transparent sticker: {dst_path}")


def save_transparent_gif(frames, filename, duration=100):
    palette_frames = []
    for img in frames:
        alpha = img.split()[3]
        img_rgb = img.convert("RGB")
        img_p = img_rgb.quantize(colors=255)
        mask = alpha.point(lambda x: 255 if x == 0 else 0)
        img_p.paste(255, mask)
        img_p.info["transparency"] = 255
        palette_frames.append(img_p)

    palette_frames[0].save(
        filename,
        save_all=True,
        append_images=palette_frames[1:],
        duration=duration,
        loop=0,
        disposal=2,
    )
    print(f"Generated {filename}")


def generate_animations():
    print("Generating Red Team animations...")

    # 1. Red Team Terminal Typing GIF (60 frames)
    term_frames = []
    prompt = "root@kali:~# "
    actions = [
        ("whoami", ["charanbs18 [Red Team / CTF]"]),
        ("nmap -sC -sV 10.10.14.8", ["22/tcp open ssh", "443/tcp open https [TLS]"]),
        ("burpsuite --target app", ["[+] Proxy 127.0.0.1:8080 READY"]),
        ("msfconsole -q -x status", ["[*] Handler armed | 0day lab"]),
        ("cat focus.txt", ["Pentesting | Bug Bounty | AppSec"]),
    ]

    terminal_states = []
    history_lines = []
    for cmd, outputs in actions:
        for i in range(len(cmd) + 1):
            terminal_states.append((prompt + cmd[:i], history_lines[-3:]))
        history_lines.append(prompt + cmd)
        for out in outputs:
            history_lines.append(out)
            for _ in range(3):
                terminal_states.append((prompt, history_lines[-3:]))

    while len(terminal_states) < 60:
        terminal_states.append(terminal_states[-1])
    terminal_states = terminal_states[:60]

    for idx, (curr_input, history) in enumerate(terminal_states):
        img = Image.new("RGBA", (380, 190), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Terminal Window
        draw.rectangle([4, 4, 376, 186], fill=(13, 17, 23), outline=(255, 42, 85), width=2)
        draw.rectangle([6, 6, 374, 28], fill=(24, 14, 24))
        # Window dots
        draw.ellipse([14, 14, 21, 21], fill=(255, 42, 85))
        draw.ellipse([26, 14, 33, 21], fill=(255, 183, 3))
        draw.ellipse([38, 14, 45, 21], fill=(0, 240, 255))
        draw.text((135, 11), "KALI_RECON.sh", fill=(0, 240, 255))

        y_pos = 42
        for line in history:
            if line.startswith("root@kali"):
                color = (255, 42, 85)
            elif "[+]" in line or "[*]" in line or "open" in line:
                color = (0, 240, 255)
            else:
                color = (226, 232, 240)
            draw.text((16, y_pos), line, fill=color)
            y_pos += 26

        draw.text((16, y_pos), curr_input, fill=(0, 240, 255))
        if idx % 2 == 0:
            cursor_x = 16 + len(curr_input) * 6
            if cursor_x < 362:
                draw.rectangle([cursor_x, y_pos, cursor_x + 6, y_pos + 12], fill=(255, 42, 85))

        term_frames.append(img)
    save_transparent_gif(term_frames, "redteam/terminal/terminal.gif", duration=110)

    # 2. Radar Sweep GIF (24 frames)
    radar_frames = []
    cx, cy = 60, 60
    blips = [(38, 42, 0), (80, 48, 8), (68, 82, 16)]
    for i in range(24):
        img = Image.new("RGBA", (120, 120), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.ellipse([8, 8, 112, 112], fill=(13, 17, 23), outline=(0, 240, 255), width=2)
        draw.ellipse([26, 26, 94, 94], outline=(30, 58, 74), width=1)
        draw.ellipse([44, 44, 76, 76], outline=(30, 58, 74), width=1)
        draw.line([(cx, 10), (cx, 110)], fill=(30, 58, 74), width=1)
        draw.line([(10, cy), (110, cy)], fill=(30, 58, 74), width=1)

        angle = (2 * math.pi * i) / 24
        # Trailing sector lines
        for trail in range(4):
            a = angle - trail * 0.14
            ex = cx + int(48 * math.cos(a))
            ey = cy + int(48 * math.sin(a))
            col = (0, 240, 255) if trail == 0 else (0, 120, 150)
            draw.line([(cx, cy), (ex, ey)], fill=col, width=2 if trail == 0 else 1)

        # Blips
        for bx, by, offset in blips:
            pulse = (i - offset) % 24
            if pulse < 10:
                r = 3 + (1 if pulse < 4 else 0)
                draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(255, 42, 85))
            else:
                draw.ellipse([bx - 2, by - 2, bx + 2, by + 2], fill=(120, 25, 45))

        draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(0, 240, 255))
        radar_frames.append(img)
    save_transparent_gif(radar_frames, "redteam/animations/radar_sweep.gif", duration=75)

    # 3. Cyber Shield Pulse GIF (12 frames)
    shield_frames = []
    for i in range(12):
        img = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        active_red = i % 6 < 3
        border_col = (255, 42, 85) if active_red else (0, 240, 255)
        inner_col = (0, 240, 255) if active_red else (255, 42, 85)

        shield_pts = [(50, 12), (82, 24), (78, 60), (50, 88), (22, 60), (18, 24)]
        draw.polygon(shield_pts, fill=(17, 24, 39), outline=border_col)
        inner_pts = [(50, 22), (72, 31), (69, 57), (50, 77), (31, 57), (28, 31)]
        draw.polygon(inner_pts, outline=inner_col)
        # Lock glyph inside
        draw.rectangle([42, 48, 58, 62], fill=border_col)
        draw.arc([44, 38, 56, 52], start=180, end=0, fill=inner_col, width=2)
        shield_frames.append(img)
    save_transparent_gif(shield_frames, "redteam/animations/cyber_shield.gif", duration=120)

    # 4. Packet Pulse Node GIF (16 frames)
    pulse_frames = []
    for i in range(16):
        img = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        r = 10 + int(20 * (i / 15.0))
        col = (255, 42, 85) if i < 8 else (0, 240, 255)
        draw.ellipse([40 - r, 40 - r, 40 + r, 40 + r], outline=col, width=2)
        draw.ellipse([32, 32, 48, 48], fill=(13, 17, 23), outline=(0, 240, 255), width=2)
        draw.ellipse([36, 36, 44, 44], fill=(255, 42, 85))
        pulse_frames.append(img)
    save_transparent_gif(pulse_frames, "redteam/animations/packet_pulse.gif", duration=75)


def generate_svgs():
    print("Generating Red Team Crimson/Cyan SVG assets...")

    # 1. Hero Banner (redteam/banner/hero.svg)
    hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 560" width="1280" height="560">
  <defs>
    <radialGradient id="ops-bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#1c0d1b" />
      <stop offset="55%" stop-color="#0f141d" />
      <stop offset="100%" stop-color="#0d1117" />
    </radialGradient>
    <linearGradient id="crimson-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff2a55" />
      <stop offset="50%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#00f0ff" />
    </linearGradient>
    <radialGradient id="desk-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ff2a55" stop-opacity="0.28" />
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0" />
    </radialGradient>
    <pattern id="cyber-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.8" opacity="0.45"/>
    </pattern>
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes sweep {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    @keyframes pulse-packet {
      0%, 100% { opacity: 0.35; }
      50% { opacity: 1; }
    }
    @keyframes scan-y {
      0% { transform: translateY(0px); opacity: 0.85; }
      50% { transform: translateY(180px); opacity: 0.35; }
      100% { transform: translateY(0px); opacity: 0.85; }
    }
    @keyframes kb-glow {
      0%, 100% { stroke: #ff2a55; filter: drop-shadow(0 0 4px #ff2a55); }
      50% { stroke: #00f0ff; filter: drop-shadow(0 0 8px #00f0ff); }
    }
    .radar-arm { transform-origin: 145px 165px; animation: sweep 4s linear infinite; }
    .packet-node { animation: pulse-packet 2.2s ease-in-out infinite; }
    .scan-bar { animation: scan-y 4.5s ease-in-out infinite; }
    .kb-border { animation: kb-glow 3.5s ease-in-out infinite; }
  </style>

  <!-- Background & Grid -->
  <rect width="1280" height="560" rx="16" fill="url(#ops-bg)"/>
  <rect width="1280" height="560" rx="16" fill="url(#cyber-grid)"/>
  <rect x="2" y="2" width="1276" height="556" rx="15" fill="none" stroke="url(#crimson-cyan)" stroke-width="2" opacity="0.7"/>

  <!-- Top HUD Bar -->
  <rect x="24" y="18" width="1232" height="34" rx="6" fill="#111827" stroke="#1e293b" stroke-width="1.5"/>
  <circle cx="44" cy="35" r="5" fill="#ff2a55"/>
  <circle cx="62" cy="35" r="5" fill="#ffb703"/>
  <circle cx="80" cy="35" r="5" fill="#00f0ff"/>
  <text x="104" y="40" fill="#94a3b8" font-family="monospace" font-size="13" font-weight="bold">
    SYS: <tspan fill="#00f0ff">KALI_OPS</tspan> // MODE: <tspan fill="#ff2a55">RED_TEAM</tspan> // OPERATOR: <tspan fill="#f8f9fa">CHARANBS18</tspan>
  </text>
  <text x="1235" y="40" fill="#ff2a55" font-family="monospace" font-size="12" font-weight="bold" text-anchor="end">[ AUTHORIZED RECON ONLY ]</text>

  <!-- Left HUD Radar Panel -->
  <g transform="translate(36, 75)">
    <rect width="220" height="235" rx="10" fill="#0b1017" stroke="#00f0ff" stroke-width="1.5" opacity="0.92"/>
    <text x="16" y="24" fill="#00f0ff" font-family="monospace" font-size="12" font-weight="bold">&gt; THREAT_RADAR</text>
    <line x1="12" y1="32" x2="208" y2="32" stroke="#1e293b" stroke-width="1"/>
    <circle cx="110" cy="130" r="72" fill="#0d1117" stroke="#00f0ff" stroke-width="1.5" opacity="0.8"/>
    <circle cx="110" cy="130" r="48" fill="none" stroke="#1e293b" stroke-width="1"/>
    <circle cx="110" cy="130" r="24" fill="none" stroke="#1e293b" stroke-width="1"/>
    <line x1="38" y1="130" x2="182" y2="130" stroke="#1e293b" stroke-width="1"/>
    <line x1="110" y1="58" x2="110" y2="202" stroke="#1e293b" stroke-width="1"/>
    <circle cx="82" cy="96" r="4" fill="#ff2a55" class="packet-node"/>
    <circle cx="145" cy="112" r="4" fill="#ff2a55" class="packet-node" style="animation-delay:0.8s"/>
    <circle cx="122" cy="166" r="3.5" fill="#00f0ff" class="packet-node" style="animation-delay:1.4s"/>
    <text x="16" y="222" fill="#94a3b8" font-family="monospace" font-size="11">NODES: <tspan fill="#00f0ff">12 ACTIVE</tspan> | VULNS: <tspan fill="#ff2a55">3</tspan></text>
  </g>
  <g transform="translate(1, 40)">
    <line x1="145" y1="165" x2="215" y2="165" stroke="#00f0ff" stroke-width="2" class="radar-arm" filter="url(#neon-glow)"/>
  </g>

  <!-- Left Bottom Quick Spec Box -->
  <g transform="translate(36, 326)">
    <rect width="220" height="125" rx="10" fill="#0b1017" stroke="#ff2a55" stroke-width="1.5"/>
    <text x="16" y="25" fill="#ff2a55" font-family="monospace" font-size="12" font-weight="bold">&gt; OPERATOR_ROLES</text>
    <text x="16" y="50" fill="#f8f9fa" font-family="monospace" font-size="11">[+] Ethical Hacker</text>
    <text x="16" y="72" fill="#f8f9fa" font-family="monospace" font-size="11">[+] Pentester / Bounty</text>
    <text x="16" y="94" fill="#f8f9fa" font-family="monospace" font-size="11">[+] Security Researcher</text>
    <text x="16" y="114" fill="#00f0ff" font-family="monospace" font-size="11">[+] CTF Player // THM</text>
  </g>

  <!-- Desk Ambient Glow -->
  <ellipse cx="760" cy="460" rx="460" ry="90" fill="url(#desk-glow)"/>

  <!-- Monitor 1 (Left-Center): Nmap & Recon -->
  <g transform="translate(288, 120)">
    <rect width="310" height="230" rx="8" fill="#161b22" stroke="#ff2a55" stroke-width="2.5"/>
    <rect x="10" y="10" width="290" height="210" rx="4" fill="#0b0f14"/>
    <rect x="10" y="10" width="290" height="24" rx="2" fill="#1f121d"/>
    <text x="20" y="26" fill="#ff2a55" font-family="monospace" font-size="11" font-weight="bold">NMAP // RECON_SCAN</text>
    <g transform="translate(20, 52)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#00f0ff">$ nmap -sC -sV target</text>
      <text x="0" y="22" fill="#94a3b8">PORT     STATE  SERVICE</text>
      <text x="0" y="42" fill="#f8f9fa">22/tcp   <tspan fill="#00f0ff">open</tspan>   OpenSSH</text>
      <text x="0" y="62" fill="#f8f9fa">80/tcp   <tspan fill="#00f0ff">open</tspan>   nginx</text>
      <text x="0" y="82" fill="#f8f9fa">443/tcp  <tspan fill="#00f0ff">open</tspan>   https</text>
      <text x="0" y="102" fill="#f8f9fa">8080/tcp <tspan fill="#ff2a55">open</tspan>   http-proxy</text>
      <text x="0" y="132" fill="#ffb703">[!] Enumerating endpoints...</text>
    </g>
    <line x1="12" y1="36" x2="298" y2="36" stroke="#ff2a55" stroke-width="1.5" opacity="0.6" class="scan-bar"/>
    <rect x="135" y="230" width="40" height="105" fill="#161b22"/>
    <ellipse cx="155" cy="335" rx="52" ry="8" fill="#1f2937"/>
  </g>

  <!-- Monitor 2 (Center): Burp Suite / Exploit Code -->
  <g transform="translate(618, 92)">
    <rect width="340" height="258" rx="8" fill="#161b22" stroke="#00f0ff" stroke-width="2.5"/>
    <rect x="10" y="10" width="320" height="238" rx="4" fill="#0b0f14"/>
    <rect x="10" y="10" width="320" height="26" rx="2" fill="#0d1e2b"/>
    <text x="22" y="27" fill="#00f0ff" font-family="monospace" font-size="11" font-weight="bold">BURP SUITE // INTERCEPT_ON</text>
    <g transform="translate(22, 56)" font-family="monospace" font-size="11">
      <text x="0" y="0" fill="#ff2a55">POST /api/v1/auth HTTP/1.1</text>
      <text x="0" y="20" fill="#94a3b8">Host: target.internal</text>
      <text x="0" y="40" fill="#94a3b8">Authorization: Bearer eyJhbG...</text>
      <text x="0" y="64" fill="#00f0ff">{"role":"operator","audit":true}</text>
      <line x1="0" y1="80" x2="296" y2="80" stroke="#1e293b" stroke-width="1"/>
      <text x="0" y="102" fill="#ffb703">HTTP/1.1 200 OK</text>
      <text x="0" y="124" fill="#f8f9fa">X-Security-Check: <tspan fill="#00f0ff">PASSED</tspan></text>
      <text x="0" y="146" fill="#f8f9fa">Payload-Status: <tspan fill="#ff2a55">VERIFIED</tspan></text>
      <rect x="0" y="162" width="110" height="22" rx="4" fill="#ff2a55" fill-opacity="0.2" stroke="#ff2a55"/>
      <text x="55" y="177" fill="#ff2a55" font-size="10" font-weight="bold" text-anchor="middle">FORWARD PKT</text>
      <rect x="122" y="162" width="110" height="22" rx="4" fill="#00f0ff" fill-opacity="0.15" stroke="#00f0ff"/>
      <text x="177" y="177" fill="#00f0ff" font-size="10" font-weight="bold" text-anchor="middle">SEND REPEATER</text>
    </g>
    <rect x="150" y="258" width="40" height="105" fill="#161b22"/>
    <ellipse cx="170" cy="363" rx="58" ry="9" fill="#1f2937"/>
  </g>

  <!-- Monitor 3 (Right): Network Topology & Wireshark -->
  <g transform="translate(978, 125)">
    <rect width="270" height="225" rx="8" fill="#161b22" stroke="#ff2a55" stroke-width="2.5"/>
    <rect x="10" y="10" width="250" height="205" rx="4" fill="#0b0f14"/>
    <rect x="10" y="10" width="250" height="24" rx="2" fill="#1f121d"/>
    <text x="20" y="26" fill="#00f0ff" font-family="monospace" font-size="11" font-weight="bold">WIRESHARK // PKT_FLOW</text>
    <!-- Network graph -->
    <line x1="65" y1="80" x2="135" y2="115" stroke="#00f0ff" stroke-width="2" stroke-dasharray="4 3"/>
    <line x1="135" y1="115" x2="205" y2="75" stroke="#ff2a55" stroke-width="2" stroke-dasharray="4 3"/>
    <line x1="135" y1="115" x2="195" y2="165" stroke="#00f0ff" stroke-width="2"/>
    <line x1="65" y1="80" x2="75" y2="160" stroke="#ff2a55" stroke-width="1.5"/>
    <circle cx="65" cy="80" r="10" fill="#111827" stroke="#00f0ff" stroke-width="2"/>
    <circle cx="135" cy="115" r="13" fill="#1f121d" stroke="#ff2a55" stroke-width="2.5"/>
    <circle cx="205" cy="75" r="9" fill="#111827" stroke="#ff2a55" stroke-width="2"/>
    <circle cx="195" cy="165" r="9" fill="#111827" stroke="#00f0ff" stroke-width="2"/>
    <circle cx="75" cy="160" r="8" fill="#111827" stroke="#ffb703" stroke-width="2"/>
    <text x="135" y="198" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">TLSv1.3 // CAPTURE ACTIVE</text>
    <rect x="115" y="225" width="40" height="105" fill="#161b22"/>
    <ellipse cx="135" cy="330" rx="48" ry="8" fill="#1f2937"/>
  </g>

  <!-- Programmer Desk Surface -->
  <rect x="24" y="458" width="1232" height="82" rx="8" fill="#0b0f14" stroke="#1e293b" stroke-width="2"/>
  <rect x="24" y="458" width="1232" height="5" fill="url(#crimson-cyan)" opacity="0.65"/>

  <!-- Mechanical Keyboard -->
  <g transform="translate(650, 444)">
    <rect class="kb-border" width="275" height="24" rx="5" fill="#161b22" stroke-width="2.5"/>
    <path d="M 14 8 H 261" stroke="#00f0ff" stroke-dasharray="8 4" stroke-width="2.5"/>
    <path d="M 10 16 H 265" stroke="#ff2a55" stroke-dasharray="10 4" stroke-width="2.5"/>
  </g>

  <!-- Hardware Pentest Dongle / Security Key on Desk -->
  <g transform="translate(490, 440)">
    <rect width="58" height="20" rx="4" fill="#161b22" stroke="#ff2a55" stroke-width="1.5"/>
    <rect x="58" y="4" width="12" height="12" rx="1" fill="#94a3b8"/>
    <circle cx="14" cy="10" r="3" fill="#00f0ff"/>
    <text x="36" y="13" fill="#f8f9fa" font-family="monospace" font-size="7" font-weight="bold" text-anchor="middle">0DAY</text>
  </g>

  <!-- Coffee Mug -->
  <g transform="translate(970, 418)">
    <rect width="30" height="36" rx="4" fill="#161b22" stroke="#00f0ff" stroke-width="2"/>
    <path d="M 30 8 C 38 8, 38 26, 30 26" fill="none" stroke="#00f0ff" stroke-width="2"/>
    <path d="M 10 -6 Q 6 -16, 12 -24" fill="none" stroke="#ff2a55" stroke-width="2" opacity="0.7"/>
    <path d="M 20 -4 Q 24 -14, 18 -22" fill="none" stroke="#00f0ff" stroke-width="2" opacity="0.7"/>
  </g>

  <!-- Center Hero Nameplate -->
  <text x="788" y="518" fill="#f8f9fa" font-family="monospace" font-size="22" font-weight="bold" letter-spacing="3" text-anchor="middle">
    CHARAN BS <tspan fill="#ff2a55">//</tspan> <tspan fill="#00f0ff">ETHICAL HACKER &amp; SECURITY RESEARCHER</tspan>
  </text>
</svg>"""
    with open("redteam/banner/hero.svg", "w") as f:
        f.write(hero_svg)

    # 2. Biometric HUD Profile Frame (redteam/frames/profile_frame.svg)
    profile_frame_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 260" width="240" height="260" fill="none">
  <style>
    @keyframes spin-reticle {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    @keyframes scan-line {
      0%, 100% { transform: translateY(0px); opacity: 0.7; }
      50% { transform: translateY(150px); opacity: 0.25; }
    }
    .reticle-spin { transform-origin: 120px 125px; animation: spin-reticle 18s linear infinite; }
    .bio-scan { animation: scan-line 3.5s ease-in-out infinite; }
  </style>

  <!-- Outer HUD Card -->
  <rect x="6" y="6" width="228" height="248" rx="14" fill="none" stroke="#ff2a55" stroke-width="2"/>
  <rect x="12" y="12" width="216" height="236" rx="10" fill="none" stroke="#00f0ff" stroke-width="1" stroke-dasharray="6 4" opacity="0.5"/>

  <!-- Target Lock Corner Brackets -->
  <path d="M 18 42 V 18 H 42 M 198 18 H 222 V 42 M 18 208 V 232 H 42 M 198 232 H 222 V 208" stroke="#00f0ff" stroke-width="3"/>

  <!-- Top Header Pill -->
  <rect x="44" y="14" width="152" height="20" rx="4" fill="#0d1117" stroke="#ff2a55" stroke-width="1.5"/>
  <text x="120" y="28" fill="#ff2a55" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">ID // CHARANBS18</text>

  <!-- Rotating Reticle around Avatar -->
  <circle cx="120" cy="125" r="96" stroke="#00f0ff" stroke-width="1.5" stroke-dasharray="10 6" class="reticle-spin" opacity="0.85"/>
  <circle cx="120" cy="125" r="90" stroke="#ff2a55" stroke-width="1.5" opacity="0.7"/>

  <!-- Biometric Scan Line -->
  <line x1="35" y1="50" x2="205" y2="50" stroke="#00f0ff" stroke-width="1.5" class="bio-scan"/>

  <!-- Bottom Clearance Plate -->
  <rect x="34" y="224" width="172" height="22" rx="4" fill="#0d1117" stroke="#00f0ff" stroke-width="1.5"/>
  <text x="120" y="239" fill="#00f0ff" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">RED TEAM // LEVEL 99</text>
</svg>"""
    with open("redteam/frames/profile_frame.svg", "w") as f:
        f.write(profile_frame_svg)

    # 3. Arsenal Tool Modules & Spec Cards (redteam/skills/)
    tools_data = [
        ("burpsuite", "Burp Suite", "WEB PROXY", 95, "#ff2a55", "INTERCEPT"),
        ("nmap", "Nmap", "NET RECON", 94, "#00f0ff", "DISCOVERY"),
        ("wireshark", "Wireshark", "PKT SNIFFER", 90, "#00f0ff", "TRAFFIC"),
        ("kali", "Kali Linux", "OPS OS", 95, "#ff2a55", "PLATFORM"),
        ("metasploit", "Metasploit", "EXPLOIT FW", 88, "#ff2a55", "PAYLOAD"),
        ("owaspzap", "OWASP ZAP", "DAST SCAN", 86, "#ffb703", "AUDIT"),
        ("python", "Python", "AUTOMATION", 92, "#00f0ff", "SCRIPTING"),
        ("bash", "Bash", "SHELL OPS", 90, "#ff2a55", "CLI"),
    ]

    for key, name, cat, lvl, color, tag in tools_data:
        bar_w = int(84 * (lvl / 100.0))
        tool_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 115 115" width="115" height="115" fill="none">
  <rect x="4" y="4" width="107" height="107" rx="10" fill="#0d1117" stroke="{color}" stroke-width="1.8"/>
  <path d="M 4 18 V 4 H 18 M 97 4 H 111 V 18 M 4 97 V 111 H 18 M 97 111 H 111 V 97" stroke="#f8f9fa" stroke-width="2" opacity="0.6"/>
  <!-- Hex Core -->
  <polygon points="57,18 76,29 76,51 57,62 38,51 38,29" fill="{color}" fill-opacity="0.16" stroke="{color}" stroke-width="2"/>
  <circle cx="57" cy="40" r="6" fill="{color}"/>
  <text x="57" y="77" fill="#f8f9fa" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">{name}</text>
  <text x="57" y="90" fill="{color}" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">{cat}</text>
  <rect x="15" y="97" width="84" height="5" rx="2.5" fill="#1e293b"/>
  <rect x="15" y="97" width="{bar_w}" height="5" rx="2.5" fill="{color}"/>
</svg>"""
        with open(f"redteam/skills/tool_{key}.svg", "w") as f:
            f.write(tool_svg)

    # Top 4 Tactical Spec Cards
    for key, name, cat, lvl, color, tag in tools_data[:4]:
        spec_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 140 155" width="140" height="155" fill="none">
  <rect x="2" y="2" width="136" height="151" rx="8" fill="#0b0f14" stroke="{color}" stroke-width="1.8"/>
  <rect x="8" y="8" width="124" height="18" rx="3" fill="{color}" fill-opacity="0.14"/>
  <text x="70" y="20" fill="{color}" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">[ {tag} ]</text>
  <circle cx="70" cy="64" r="24" fill="{color}" fill-opacity="0.1" stroke="{color}" stroke-width="1.8" stroke-dasharray="5 3"/>
  <text x="70" y="68" fill="#f8f9fa" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">{lvl}%</text>
  <text x="70" y="108" fill="#f8f9fa" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">{name}</text>
  <text x="70" y="124" fill="#94a3b8" font-family="monospace" font-size="9" text-anchor="middle">{cat}</text>
  <rect x="25" y="134" width="90" height="12" rx="3" fill="#161b22" stroke="{color}" stroke-width="1"/>
  <text x="70" y="143" fill="{color}" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">STATUS: ARMED</text>
</svg>"""
        with open(f"redteam/skills/spec_{key}.svg", "w") as f:
            f.write(spec_svg)

    # 4. Operations Dossier Cards (redteam/projects/)
    dossiers = [
        (
            "recon_pipeline",
            "RECON_AUTOMATION",
            "OFFENSIVE RECON",
            "Automated asset discovery, port enumeration with Nmap, and attack-surface mapping workflows.",
            "Nmap • Python • Bash",
            "#00f0ff",
        ),
        (
            "web_appsec",
            "WEB_APPSEC_LABS",
            "BUG BOUNTY &amp; OWASP",
            "OWASP Top 10 testing playbooks, Burp Suite &amp; ZAP intercept profiles, and auth/injection PoCs.",
            "Burp Suite • OWASP ZAP",
            "#ff2a55",
        ),
        (
            "ctf_exploit",
            "CTF_EXPLOIT_NOTES",
            "TRYHACKME &amp; CTFS",
            "Structured exploitation methodologies, Metasploit workflows, packet forensics, and privesc checklists.",
            "Metasploit • Wireshark • Kali",
            "#ff2a55",
        ),
    ]

    for key, title, badge, desc, stack, color in dossiers:
        dossier_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 205" width="400" height="205" fill="none">
  <rect x="2" y="2" width="396" height="201" rx="10" fill="#0d1117" stroke="{color}" stroke-width="2"/>
  <rect x="2" y="2" width="396" height="30" rx="10" fill="#161b22"/>
  <rect x="2" y="22" width="396" height="10" fill="#161b22"/>
  <circle cx="20" cy="17" r="4.5" fill="#ff2a55"/>
  <circle cx="34" cy="17" r="4.5" fill="#ffb703"/>
  <circle cx="48" cy="17" r="4.5" fill="#00f0ff"/>
  <text x="66" y="21" fill="{color}" font-family="monospace" font-size="11" font-weight="bold">DOSSIER // {title}</text>

  <rect x="20" y="46" width="145" height="20" rx="4" fill="{color}" fill-opacity="0.14" stroke="{color}" stroke-width="1"/>
  <text x="92" y="59" fill="{color}" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">{badge}</text>

  <foreignObject x="20" y="76" width="360" height="72">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: monospace; color: #e2e8f0; font-size: 12px; line-height: 1.5;">
      {desc}
    </div>
  </foreignObject>

  <line x1="20" y1="158" x2="380" y2="158" stroke="#1e293b" stroke-width="1"/>
  <text x="20" y="182" fill="#94a3b8" font-family="monospace" font-size="11">STACK: <tspan fill="#00f0ff" font-weight="bold">{stack}</tspan></text>
</svg>"""
        with open(f"redteam/projects/dossier_{key}.svg", "w") as f:
            f.write(dossier_svg)

    # 5. Security Badges & Medallions (redteam/badges/)
    medallions = [
        ("recon", "NET RECON", "#00f0ff", "M 50 18 L 78 34 V 66 L 50 82 L 22 66 V 34 Z"),
        ("websec", "WEB APPSEC", "#ff2a55", "M 50 18 A 32 32 0 1 0 50 82 A 32 32 0 1 0 50 18 Z"),
        ("bounty", "BUG HUNTER", "#ffb703", "M 50 18 L 76 42 L 66 80 H 34 L 24 42 Z"),
        ("ctf", "CTF PLAYER", "#ff2a55", "M 32 22 V 82 M 32 24 L 74 36 L 32 50"),
        ("packet", "PKT ANALYSIS", "#00f0ff", "M 20 55 L 36 35 L 48 62 L 62 28 L 80 55"),
        ("root", "ROOT ACCESS", "#ff2a55", "M 34 45 H 66 V 78 H 34 Z M 40 45 V 32 A 10 10 0 0 1 60 32 V 45"),
    ]

    for key, label, color, path_d in medallions:
        med_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 110 120" width="110" height="120" fill="none">
  <polygon points="55,6 102,28 102,82 55,104 8,82 8,28" fill="#0d1117" stroke="{color}" stroke-width="2"/>
  <g transform="translate(5, 2)">
    <path d="{path_d}" fill="{color}" fill-opacity="0.14" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <rect x="10" y="96" width="90" height="18" rx="4" fill="#161b22" stroke="{color}" stroke-width="1.2"/>
  <text x="55" y="108" fill="#f8f9fa" font-family="monospace" font-size="8.5" font-weight="bold" text-anchor="middle">{label}</text>
</svg>"""
        with open(f"redteam/badges/medallion_{key}.svg", "w") as f:
            f.write(med_svg)

    # 6. Operator Telemetry Card (redteam/stats/operator_card.svg)
    operator_card_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 250" width="450" height="250">
  <defs>
    <radialGradient id="op-back" cx="50%" cy="50%" r="80%">
      <stop offset="0%" stop-color="#1c0d1b" />
      <stop offset="100%" stop-color="#0d1117" />
    </radialGradient>
  </defs>

  <rect width="450" height="250" rx="12" fill="url(#op-back)" stroke="#ff2a55" stroke-width="2"/>
  <rect x="8" y="8" width="434" height="234" rx="8" fill="none" stroke="#00f0ff" stroke-width="1" stroke-dasharray="8 4" opacity="0.6"/>
  <path d="M 12 28 V 12 H 28 M 422 12 H 438 V 28 M 12 222 V 238 H 28 M 422 238 H 438 V 222" stroke="#00f0ff" stroke-width="2.5" fill="none"/>

  <text x="225" y="34" fill="#ff2a55" font-family="monospace" font-size="15" font-weight="bold" letter-spacing="2" text-anchor="middle">[ OPERATOR TELEMETRY ]</text>
  <line x1="25" y1="44" x2="425" y2="44" stroke="#1e293b" stroke-width="1.5"/>

  <!-- Left Shield Badge -->
  <g transform="translate(26, 62)">
    <polygon points="50,6 92,22 86,74 50,104 14,74 8,22" fill="#111827" stroke="#00f0ff" stroke-width="2"/>
    <text x="50" y="54" fill="#ff2a55" font-family="monospace" font-size="22" font-weight="bold" text-anchor="middle">#/</text>
    <text x="50" y="76" fill="#00f0ff" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">RED TEAM</text>
    <text x="50" y="126" fill="#f8f9fa" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">CharanBS18</text>
    <text x="50" y="144" fill="#ffb703" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">THM // CTF</text>
  </g>

  <!-- Right Telemetry Rows -->
  <g transform="translate(155, 68)" font-family="monospace" font-size="12.5" fill="#f8f9fa">
    <text x="0" y="14">Role: <tspan fill="#00f0ff" font-weight="bold">Ethical Hacker</tspan></text>
    <text x="0" y="42">Focus: <tspan fill="#ff2a55" font-weight="bold">Pentest / Bug Bounty</tspan></text>

    <text x="0" y="72">Recon:</text>
    <rect x="65" y="61" width="155" height="11" rx="5" fill="#161b22" stroke="#00f0ff" stroke-width="1"/>
    <rect x="65" y="61" width="146" height="11" rx="5" fill="#00f0ff"/>
    <text x="230" y="71" fill="#00f0ff" font-weight="bold">95%</text>

    <text x="0" y="102">Exploit:</text>
    <rect x="65" y="91" width="155" height="11" rx="5" fill="#161b22" stroke="#ff2a55" stroke-width="1"/>
    <rect x="65" y="91" width="138" height="11" rx="5" fill="#ff2a55"/>
    <text x="230" y="101" fill="#ff2a55" font-weight="bold">90%</text>

    <text x="0" y="132">Platform: <tspan fill="#ffb703" font-weight="bold">Kali Linux</tspan></text>
    <text x="0" y="158">Status: <tspan fill="#00f0ff" font-weight="bold">ONLINE // HUNTING</tspan></text>
  </g>
</svg>"""
    with open("redteam/stats/operator_card.svg", "w") as f:
        f.write(operator_card_svg)

    # 7. Firewall / Packet-Trace Snake Frame (redteam/stats/firewall_frame.svg)
    firewall_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 200" width="850" height="200">
  <defs>
    <linearGradient id="fw-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff2a55" />
      <stop offset="50%" stop-color="#00f0ff" />
      <stop offset="100%" stop-color="#ff2a55" />
    </linearGradient>
  </defs>

  <!-- Left & Right Tactical Pillars -->
  <g transform="translate(10, 12)">
    <rect width="36" height="176" rx="4" fill="#111827" stroke="#ff2a55" stroke-width="2"/>
    <line x1="8" y1="24" x2="28" y2="24" stroke="#00f0ff" stroke-width="2"/>
    <line x1="8" y1="152" x2="28" y2="152" stroke="#00f0ff" stroke-width="2"/>
    <line x1="18" y1="30" x2="18" y2="146" stroke="#ff2a55" stroke-width="1.5" stroke-dasharray="4 4"/>
  </g>

  <g transform="translate(804, 12)">
    <rect width="36" height="176" rx="4" fill="#111827" stroke="#00f0ff" stroke-width="2"/>
    <line x1="8" y1="24" x2="28" y2="24" stroke="#ff2a55" stroke-width="2"/>
    <line x1="8" y1="152" x2="28" y2="152" stroke="#ff2a55" stroke-width="2"/>
    <line x1="18" y1="30" x2="18" y2="146" stroke="#00f0ff" stroke-width="1.5" stroke-dasharray="4 4"/>
  </g>

  <!-- Top HUD Arch -->
  <path d="M 46 38 L 90 18 H 760 L 804 38" fill="none" stroke="url(#fw-grad)" stroke-width="3"/>
  <rect x="235" y="6" width="380" height="28" rx="6" fill="#0d1117" stroke="#00f0ff" stroke-width="1.5"/>
  <text x="425" y="25" fill="#00f0ff" font-family="monospace" font-size="14" font-weight="bold" letter-spacing="2" text-anchor="middle">
    [ PACKET TRACE // CONTRIBUTION GRID ]
  </text>

  <!-- Bottom Wire -->
  <path d="M 46 184 H 804" fill="none" stroke="#ff2a55" stroke-width="2" stroke-dasharray="8 6"/>
</svg>"""
    with open("redteam/stats/firewall_frame.svg", "w") as f:
        f.write(firewall_svg)

    # 8. Dividers (redteam/dividers/)
    circuit_trace = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 50" width="100%" height="50" fill="none">
  <path d="M 0 25 H 350 L 380 12 H 550 L 580 25 H 620 L 650 38 H 820 L 850 25 H 1200" stroke="#ff2a55" stroke-width="2"/>
  <path d="M 0 32 H 260 L 285 42 H 440" stroke="#00f0ff" stroke-width="1.5" opacity="0.7"/>
  <path d="M 760 8 H 915 L 940 18 H 1200" stroke="#00f0ff" stroke-width="1.5" opacity="0.7"/>
  <circle cx="380" cy="12" r="4" fill="#00f0ff"/>
  <circle cx="600" cy="25" r="5" fill="#ff2a55"/>
  <circle cx="820" cy="25" r="4" fill="#00f0ff"/>
</svg>"""
    with open("redteam/dividers/circuit_trace.svg", "w") as f:
        f.write(circuit_trace)

    radar_pulse = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 50" width="100%" height="50" fill="none">
  <line x1="0" y1="25" x2="500" y2="25" stroke="#1e293b" stroke-width="2"/>
  <path d="M 500 25 H 540 L 555 10 L 575 42 L 595 6 L 615 40 L 630 25 H 700" stroke="#00f0ff" stroke-width="2.5" stroke-linejoin="round"/>
  <line x1="700" y1="25" x2="1200" y2="25" stroke="#1e293b" stroke-width="2"/>
  <circle cx="595" cy="25" r="20" stroke="#ff2a55" stroke-width="1.5" stroke-dasharray="4 3"/>
</svg>"""
    with open("redteam/dividers/radar_pulse.svg", "w") as f:
        f.write(radar_pulse)

    packet_stream = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 40" width="100%" height="40" fill="none">
  <line x1="40" y1="20" x2="1160" y2="20" stroke="#ff2a55" stroke-width="1.5" stroke-dasharray="10 8"/>
  <rect x="260" y="13" width="28" height="14" rx="3" fill="#0d1117" stroke="#00f0ff" stroke-width="1.5"/>
  <rect x="586" y="13" width="28" height="14" rx="3" fill="#0d1117" stroke="#ff2a55" stroke-width="1.5"/>
  <rect x="912" y="13" width="28" height="14" rx="3" fill="#0d1117" stroke="#00f0ff" stroke-width="1.5"/>
</svg>"""
    with open("redteam/dividers/packet_stream.svg", "w") as f:
        f.write(packet_stream)

    # 9. Red Team Footer (redteam/footer/footer.svg)
    footer_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 180" width="1280" height="180">
  <defs>
    <linearGradient id="ft-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0d1117" />
      <stop offset="100%" stop-color="#1a0b16" />
    </linearGradient>
    <linearGradient id="ft-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff2a55" />
      <stop offset="50%" stop-color="#00f0ff" />
      <stop offset="100%" stop-color="#ff2a55" />
    </linearGradient>
  </defs>

  <rect width="1280" height="180" rx="12" fill="url(#ft-bg)" stroke="#1e293b" stroke-width="1.5"/>
  <path d="M 0 140 L 180 140 L 220 110 L 420 110 L 460 140 L 820 140 L 860 110 L 1060 110 L 1100 140 L 1280 140" fill="none" stroke="url(#ft-line)" stroke-width="2" opacity="0.65"/>

  <!-- Network Nodes -->
  <circle cx="220" cy="110" r="5" fill="#00f0ff"/>
  <circle cx="420" cy="110" r="5" fill="#ff2a55"/>
  <circle cx="860" cy="110" r="5" fill="#ff2a55"/>
  <circle cx="1060" cy="110" r="5" fill="#00f0ff"/>

  <text x="640" y="75" fill="#f8f9fa" font-family="monospace" font-size="20" font-weight="bold" letter-spacing="2" text-anchor="middle">
    "HACK TO PROTECT. <tspan fill="#ff2a55">BREAK TO BUILD STRONGER.</tspan>"
  </text>
  <text x="640" y="160" fill="#94a3b8" font-family="monospace" font-size="11" letter-spacing="2" text-anchor="middle">
    [ ETHICAL HACKING // RESPONSIBLE DISCLOSURE // CONTINUOUS RECON ]
  </text>
</svg>"""
    with open("redteam/footer/footer.svg", "w") as f:
        f.write(footer_svg)

    # 10. Crisp Vector Sticker Emblems (for radar & encrypted comms)
    recon_sticker_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160" fill="none">
  <circle cx="80" cy="80" r="72" fill="#0d1117" stroke="#00f0ff" stroke-width="3"/>
  <circle cx="80" cy="80" r="54" stroke="#1e293b" stroke-width="2"/>
  <circle cx="80" cy="80" r="34" stroke="#1e293b" stroke-width="2"/>
  <line x1="80" y1="12" x2="80" y2="148" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="12" y1="80" x2="148" y2="80" stroke="#1e293b" stroke-width="1.5"/>
  <path d="M 80 80 L 128 36 A 66 66 0 0 1 146 80 Z" fill="#00f0ff" fill-opacity="0.18"/>
  <line x1="80" y1="80" x2="128" y2="36" stroke="#00f0ff" stroke-width="2.5"/>
  <circle cx="110" cy="54" r="6" fill="#ff2a55"/>
  <circle cx="52" cy="102" r="4.5" fill="#ffb703"/>
  <circle cx="80" cy="80" r="5" fill="#00f0ff"/>
  <rect x="34" y="132" width="92" height="20" rx="4" fill="#161b22" stroke="#ff2a55" stroke-width="1.5"/>
  <text x="80" y="145" fill="#f8f9fa" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">RECON // LIVE</text>
</svg>"""
    with open("redteam/stickers/recon_radar.svg", "w") as f:
        f.write(recon_sticker_svg)

    comms_sticker_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160" fill="none">
  <polygon points="80,8 144,44 144,116 80,152 16,116 16,44" fill="#0d1117" stroke="#ff2a55" stroke-width="3"/>
  <polygon points="80,18 134,49 134,111 80,142 26,111 26,49" fill="none" stroke="#00f0ff" stroke-width="1.2" stroke-dasharray="6 4"/>
  <!-- Envelope + Lock -->
  <rect x="42" y="54" width="76" height="50" rx="6" fill="#161b22" stroke="#00f0ff" stroke-width="2"/>
  <path d="M 44 56 L 80 84 L 116 56" stroke="#ff2a55" stroke-width="2.5" fill="none"/>
  <circle cx="80" cy="84" r="10" fill="#ff2a55"/>
  <text x="80" y="88" fill="#f8f9fa" font-family="monospace" font-size="10" font-weight="bold" text-anchor="middle">PGP</text>
  <rect x="38" y="114" width="84" height="18" rx="4" fill="#161b22" stroke="#00f0ff" stroke-width="1.5"/>
  <text x="80" y="126" fill="#00f0ff" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">AES-256 // TLS</text>
</svg>"""
    with open("redteam/stickers/encrypted_comms.svg", "w") as f:
        f.write(comms_sticker_svg)

    print("All Red Team SVGs generated.")


def main():
    setup_dirs()
    process_stickers_and_avatar()
    generate_animations()
    generate_svgs()
    print("Red Team asset build complete!")


if __name__ == "__main__":
    main()
