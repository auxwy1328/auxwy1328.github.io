"""Generate cover + body images for 2 new chatjiami articles"""
import os, re, subprocess, sys, time, urllib.request
from PIL import Image

script_dir = r'C:\Users\15645\.openclaw-autoclaw\skills\autoglm-generate-image'
script_path = os.path.join(script_dir, 'generate-image.py')
project_dir = r'C:\Projects\encrypted-chat-seo'

images = [
    # Article 1: bat-chat-security-review
    ("reviews/bat-chat-security-review", [
        ("cover.jpg", "Professional security audit concept for a Chinese messaging app, shield icon with lock symbol, dark blue and green color scheme, digital privacy theme, 16:9 ratio", "cover"),
        ("encryption-diagram.jpg", "End-to-end encryption diagram showing sender device encrypting message, server transmitting ciphertext, receiver device decrypting, with lock icons and key symbols", "body1"),
        ("server-location.jpg", "World map highlighting China server location versus US and Switzerland server locations for messaging apps, with data flow arrows and flag icons", "body2"),
        ("privacy-comparison.jpg", "Privacy policy comparison table visualization for three messaging apps, showing checkmarks and crosses for data collection practices, clean infographic style", "body3"),
    ]),
    # Article 2: cross-platform-encrypted-chat
    ("scenarios/cross-platform-encrypted-chat", [
        ("cover.jpg", "iPhone and Android phone side by side with encrypted chat bubbles between them, padlock icons on messages, modern clean design, blue and green gradient, 16:9 ratio", "cover"),
        ("signal-crossplatform.jpg", "Signal app running on iPhone and Android simultaneously showing encrypted conversation, both screens visible with matching message bubbles", "body1"),
        ("platform-grid.jpg", "Grid comparison of 6 messaging app icons arranged by platform support, iOS Android Desktop columns with checkmark indicators, clean table layout", "body2"),
        ("device-sync.jpg", "Smartphone tablet and laptop showing synchronized encrypted messages across devices, cloud sync arrows connecting them, privacy shield overlay", "body3"),
    ]),
]

success = 0
fail = 0

for slug, imgs in images:
    for filename, prompt, img_type in imgs:
        out_dir = os.path.join(project_dir, "static", "images", slug.replace('/', os.sep))
        out_path = os.path.join(out_dir, filename)
        print(f"[{slug}/{filename}]...", end=" ", flush=True)
        
        try:
            result = subprocess.run(
                [sys.executable, script_path, prompt],
                capture_output=True, text=True, timeout=60,
                cwd=script_dir
            )
            output = result.stdout + result.stderr
            url_match = re.search(r'(https://[^\s"\']+\.(jpg|png|jpeg|webp))', output)
            if not url_match:
                print("FAIL (no URL)")
                fail += 1
                continue
            
            img_url = url_match.group(1)
            os.makedirs(out_dir, exist_ok=True)
            tmp_path = out_path + '.tmp'
            urllib.request.urlretrieve(img_url, tmp_path)
            
            img = Image.open(tmp_path)
            w, h = img.size
            if img_type == "cover":
                img_cropped = img.crop((0, 0, w, int(h * 0.88)))
            else:
                img_cropped = img.crop((0, 0, int(w * 0.97), int(h * 0.88)))
            img_cropped.save(out_path, 'JPEG', quality=92)
            os.remove(tmp_path)
            print(f"OK ({os.path.getsize(out_path)//1024}KB)")
            success += 1
        except Exception as e:
            print(f"FAIL ({e})")
            fail += 1
        
        time.sleep(0.5)

print(f"\nImages: {success}/{success+fail} success")
