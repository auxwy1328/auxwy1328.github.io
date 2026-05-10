import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:\Projects\encrypted-chat-seo'

for root, dirs, files in os.walk(os.path.join(base, 'content')):
    for f in files:
        if f == '_index.md' or not f.endswith('.md'): continue
        slug = f.replace('.md', '')
        if slug in ('about', 'about-site', 'privacy', 'disclaimer', 'contact', 'terms'): continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            text = fh.read()
        
        # Count occurrences of 'images:' in front matter
        fm = text.split('---')[1] if text.count('---') >= 2 else ''
        count = fm.count('images:')
        if count <= 1:
            continue
        
        # Remove the single-line images: [...] that we added (keeps the multi-line array)
        # Pattern: a line like "images: ["/images/..."]" 
        text = re.sub(r'\nimages:\s*\["[^\]]*"\]\n', '\n', text, count=1)
        
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(text)
        print('Fixed: ' + slug)
