"""Fix chatjiami.com missing webp images - replace with jpg where available, remove og_image references"""
import re, os, sys
sys.stdout.reconfigure(encoding='utf-8')
base = r'C:\Projects\encrypted-chat-seo'

for root, dirs, files in os.walk(os.path.join(base, 'content')):
    for f in files:
        if f == '_index.md' or not f.endswith('.md'): continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            text = fh.read()
        
        original = text
        
        # Fix all webp references where jpg exists
        webp_refs = set(re.findall(r'/images/[^\s"]+\.webp', text))
        for ref in webp_refs:
            full_path = os.path.join(base, 'static', ref.lstrip('/'))
            if not os.path.exists(full_path):
                jpg_path = ref.replace('.webp', '.jpg')
                jpg_full = os.path.join(base, 'static', jpg_path.lstrip('/'))
                if os.path.exists(jpg_full):
                    text = text.replace(ref, jpg_path)
                    print(f'  Replace: {ref} -> {jpg_path}')
                else:
                    # Neither webp nor jpg exists - remove the reference
                    # For og_image lines, remove the whole line
                    # For figure shortcodes, remove the whole shortcode
                    if 'og_image' in ref:
                        text = re.sub(r'og_image:\s*"' + re.escape(ref) + r'"\n?', '', text)
                        print(f'  Remove og_image: {ref}')
                    else:
                        # Remove {{< figure >}} shortcodes referencing this file
                        pattern = r'\{\{<\s+figure\s+src="' + re.escape(ref) + r'[^}]*\}\}\n?'
                        text = re.sub(pattern, '', text)
                        print(f'  Remove figure: {ref}')
        
        if text != original:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(text)

print('\nDone!')
