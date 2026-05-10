import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:\Projects\encrypted-chat-seo'

# Fix articles where images references .webp but file doesn't exist (should use .jpg instead)
fixed = 0
for root, dirs, files in os.walk(os.path.join(base, 'content')):
    for f in files:
        if f == '_index.md' or not f.endswith('.md'): continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            text = fh.read()
        
        # Find all image references in front matter
        fm_m = re.search(r'^---(.*?)---', text, re.DOTALL)
        if not fm_m: continue
        fm = fm_m.group(1)
        
        # Find webp references
        webp_refs = re.findall(r'/images/[^\s"]+\.webp', fm)
        changed = False
        for ref in webp_refs:
            full_path = os.path.join(base, 'static', ref.lstrip('/'))
            if not os.path.exists(full_path):
                jpg_path = ref.replace('.webp', '.jpg')
                jpg_full = os.path.join(base, 'static', jpg_path.lstrip('/'))
                if os.path.exists(jpg_full):
                    text = text.replace(ref, jpg_path)
                    changed = True
                    print(f'  {f}: {ref} -> {jpg_path}')
        
        if changed:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(text)
            fixed += 1

print(f'\nFixed {fixed} files')
