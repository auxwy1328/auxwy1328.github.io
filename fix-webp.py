import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:\Projects\encrypted-chat-seo'

for root, dirs, files in os.walk(os.path.join(base, 'content')):
    for f in files:
        if f == '_index.md' or not f.endswith('.md'): continue
        slug = f.replace('.md', '')
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            text = fh.read()
        
        changed = False
        # Replace .webp with .jpg in images references (only if .webp doesn't exist but .jpg does)
        for ext_old, ext_new in [('.webp', '.jpg')]:
            for match in re.finditer(r'/images/[^"\']+\.' + ext_old.lstrip('.'), text):
                ref = match.group()
                old_path = os.path.join(base, 'static', ref.lstrip('/'))
                new_path = old_path.replace(ext_old, ext_new)
                if not os.path.exists(old_path) and os.path.exists(new_path):
                    text = text.replace(ref, ref.replace(ext_old, ext_new))
                    changed = True
        
        if changed:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(text)
            print('Fixed: ' + slug)
