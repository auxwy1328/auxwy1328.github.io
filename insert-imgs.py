"""Insert body images into 2 new chatjiami articles"""
import os

project_dir = r'C:\Projects\encrypted-chat-seo'

# Article 1
path1 = os.path.join(project_dir, 'content', 'reviews', 'bat-chat-security-review.md')
with open(path1, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '## 1. 加密方式：端到端加密是否名副其实？',
    '## 1. 加密方式：端到端加密是否名副其实？\n\n![蝙蝠聊天加密机制示意图](/images/reviews/bat-chat-security-review/encryption-diagram.jpg)'
)
c = c.replace(
    '## 2. 服务器与数据存储：你的数据在哪里？',
    '## 2. 服务器与数据存储：你的数据在哪里？\n\n![全球服务器位置分布图](/images/reviews/bat-chat-security-review/server-location.jpg)'
)
c = c.replace(
    '## 3. 隐私政策分析：条款里的隐藏风险',
    '## 3. 隐私政策分析：条款里的隐藏风险\n\n![隐私政策对比分析](/images/reviews/bat-chat-security-review/privacy-comparison.jpg)'
)

with open(path1, 'w', encoding='utf-8') as f:
    f.write(c)
print("Article 1: 3 body images inserted")

# Article 2
path2 = os.path.join(project_dir, 'content', 'scenarios', 'cross-platform-encrypted-chat.md')
with open(path2, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '## 1. Signal — 跨平台体验最一致',
    '## 1. Signal — 跨平台体验最一致\n\n![Signal跨平台加密聊天](/images/scenarios/cross-platform-encrypted-chat/signal-crossplatform.jpg)'
)
c = c.replace(
    '## 跨平台加密聊天软件对比总结',
    '## 跨平台加密聊天软件对比总结\n\n![6款加密聊天软件跨平台对比](/images/scenarios/cross-platform-encrypted-chat/platform-grid.jpg)'
)
c = c.replace(
    '## 怎么选择？',
    '## 怎么选择？\n\n![多设备加密消息同步](/images/scenarios/cross-platform-encrypted-chat/device-sync.jpg)'
)

with open(path2, 'w', encoding='utf-8') as f:
    f.write(c)
print("Article 2: 3 body images inserted")
