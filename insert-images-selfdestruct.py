import re

path = r'C:\Projects\encrypted-chat-seo\content\features\self-destructing-message.md'
raw = open(path, 'rb').read().decode('utf-8')

# Add cover to front matter images
cover_line = '\nimages: ["/images/features/self-destructing-message/cover.jpg"]'
raw = raw.replace('date: 2026-04-26', 'date: 2026-04-26' + cover_line, 1)

# Find H2 positions in body (after front matter)
body_start = raw.index('---', raw.index('---') + 3) + 3
body = raw[body_start:]
h2_matches = list(re.finditer(r'^## .+$', body, re.MULTILINE))

if len(h2_matches) >= 4:
    inserts = []
    # After H2 index 1
    pos1 = body_start + h2_matches[1].end()
    inserts.append((pos1, '\n\n![聊天消息自动删除功能对比](/images/features/self-destructing-message/body1.jpg)\n'))
    # After H2 index 2
    pos2 = body_start + h2_matches[2].end()
    inserts.append((pos2, '\n\n![各应用阅后即焚设置界面](/images/features/self-destructing-message/body2.jpg)\n'))
    # After H2 index 3
    pos3 = body_start + h2_matches[3].end()
    inserts.append((pos3, '\n\n![数据彻底删除与恢复方法](/images/features/self-destructing-message/body3.jpg)\n'))

    offset = 0
    for pos, img_md in sorted(inserts, key=lambda x: x[0], reverse=True):
        actual = pos + offset
        raw = raw[:actual] + img_md + raw[actual:]
        offset += len(img_md)

open(path, 'w', encoding='utf-8').write(raw)

img_count = raw.count('![')
print(f'Images in article: {img_count}')
print(f'Cover in front matter: {"images:" in raw}')
