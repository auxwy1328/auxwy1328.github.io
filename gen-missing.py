import subprocess, sys, re, urllib.request, os
from PIL import Image
script_dir = r'C:\Users\15645\.openclaw-autoclaw\skills\autoglm-generate-image'
result = subprocess.run([sys.executable, os.path.join(script_dir, 'generate-image.py'), 'Global server infrastructure map showing data center locations in China USA and Switzerland with network connections, dark theme, tech illustration'], capture_output=True, text=True, timeout=60, cwd=script_dir)
output = result.stdout + result.stderr
url_match = re.search(r'(https://[^\s"\']+\.(jpg|png|jpeg|webp))', output)
if url_match:
    img_url = url_match.group(1)
    out_path = r'C:\Projects\encrypted-chat-seo\static\images\reviews\bat-chat-security-review\server-location.jpg'
    tmp = out_path + '.tmp'
    urllib.request.urlretrieve(img_url, tmp)
    img = Image.open(tmp)
    w, h = img.size
    img.crop((0, 0, int(w*0.97), int(h*0.88))).save(out_path, 'JPEG', quality=92)
    os.remove(tmp)
    print(f'OK ({os.path.getsize(out_path)//1024}KB)')
else:
    print('FAIL')
