"""Fix chatjiami.com missing images front matter and generate missing cover images"""
import re, os, sys, hashlib, json, urllib.request, time
from PIL import Image
from io import BytesIO

sys.stdout.reconfigure(encoding='utf-8')
base = r'C:\Projects\encrypted-chat-seo'

# Articles that need fixing
articles = []
for root, dirs, files in os.walk(os.path.join(base, 'content')):
    for f in files:
        if f == '_index.md' or not f.endswith('.md'): continue
        slug = f.replace('.md', '')
        if slug in ('about', 'about-site', 'privacy', 'disclaimer', 'contact', 'terms'): continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            text = fh.read()
        img_m = re.search(r'images:\s*\["([^"]+)"\]', text)
        if not img_m:
            section = os.path.basename(root)
            img_path = f'/images/{section}/{slug}/cover.jpg'
            articles.append((path, slug, section, img_path))

print(f'Found {len(articles)} articles missing images front matter')

# Step 1: Add images front matter
for path, slug, section, img_path in articles:
    with open(path, 'r', encoding='utf-8') as fh:
        text = fh.read()
    # Add images after readtime or before faq, whichever comes first
    insert_after = re.search(r'(readtime:\s*\d+)', text)
    if not insert_after:
        insert_after = re.search(r'(card_icon:.+)', text)
    if not insert_after:
        insert_after = re.search(r'(description:.+)', text)
    
    if insert_after:
        pos = insert_after.end()
        text = text[:pos] + f'\nimages: ["{img_path}"]' + text[pos:]
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
        print(f'  Added images FM: {slug}')
    else:
        print(f'  SKIP (no insert point): {slug}')

# Step 2: Generate missing cover images
try:
    req = urllib.request.Request('http://127.0.0.1:18432/get_token')
    with urllib.request.urlopen(req, timeout=10) as resp:
        token = resp.read().decode().strip()
    if not token.startswith('Bearer '): token = 'Bearer ' + token
except Exception as e:
    print(f'ERROR getting token: {e}')
    sys.exit(1)

api_url = 'https://autoglm-api.zhipuai.cn/agentdr/v1/assistant/skills/generate-image'
crop_w, crop_h = 0.97, 0.88

# Descriptions for each article
desc_map = {
    'anti-spying-software': 'Shield icon protecting chat messages from surveillance, secure communication concept, dark teal gradient',
    'can-encrypted-chat-be-monitored': 'Question mark over encrypted chat bubble, surveillance eye watching messages, dark teal theme',
    'can-provider-read-messages': 'Server icon reading encrypted messages with lock symbol, privacy concept, dark teal',
    'encrypt-chat-history': 'Chat history with lock encryption symbol, secure backup concept, dark teal gradient',
    'encrypted-voice-call': 'Phone with lock icon and voice waveform, encrypted call concept, dark teal theme',
    'what-is-e2ee': 'End to end encryption diagram with two devices and lock, E2EE concept, dark teal',
    'signal-guide': 'Signal app logo with tutorial steps, messaging guide concept, dark teal blue',
    'best-encrypted-chat': 'Podium with encrypted chat app icons ranked, best of ranking, dark teal',
    'encrypted-chat-ranking': 'Numbered list of encrypted chat apps with ratings, ranking comparison, dark teal',
    'safest-encrypted-chat': 'Fortress shield with lock and chat bubble, safest app concept, dark teal',
    'telegram-vs-signal': 'Split comparison Telegram and Signal logos face to face, vs battle concept, dark teal',
    'whatsapp-vs-signal': 'Split comparison WhatsApp and Signal logos face to face, vs battle concept, dark teal',
    'couple-private-chat': 'Heart lock icon with two chat bubbles, private couple messaging, dark teal gradient',
    'enterprise-chat': 'Office building with encrypted chat and shield, enterprise security, dark teal',
}

for path, slug, section, img_path in articles:
    out_dir = os.path.join(base, 'static', 'images', section, slug)
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'cover.jpg')
    if os.path.exists(out_file):
        print(f'  SKIP (cover exists): {slug}')
        continue
    
    desc = desc_map.get(slug, 'Encrypted messaging app interface, secure communication, dark teal theme')
    print(f'  Generating: {slug}...')
    
    appid, ts = '100003', str(int(time.time()))
    sign = hashlib.md5(f'{appid}&{ts}&38d2391985e2369a5fb8227d8e6cd5e5'.encode()).hexdigest()
    headers = {'Authorization': token, 'X-Auth-Appid': appid, 'X-Auth-TimeStamp': ts, 'X-Auth-Sign': sign, 'Content-Type': 'application/json'}
    data = json.dumps({'text': desc}).encode()
    req = urllib.request.Request(api_url, data=data, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
        if result.get('code') == 0 and result.get('data', {}).get('image_url'):
            img_url = result['data']['image_url']
            with urllib.request.urlopen(img_url, timeout=30) as resp2:
                img_data = resp2.read()
            img = Image.open(BytesIO(img_data))
            w, h = img.size
            img = img.crop((0, 0, int(w * crop_w), int(h * crop_h)))
            img.save(out_file, 'JPEG', quality=92)
            print(f'    Saved: {out_file} ({os.path.getsize(out_file)//1024}KB)')
    except Exception as e:
        print(f'    ERROR: {e}')
    time.sleep(2)

print('\nDone with chatjiami.com!')
