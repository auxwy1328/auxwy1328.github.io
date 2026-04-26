---
title: "Threema 不用手机号注册 — 2026年瑞士加密聊天的匿名注册与中文设置教程"
description: "2026年 Threema 匿名注册教程，详细讲解如何不使用手机号注册 Threema、中文设置方法、匿名度验证功能使用，以及与 Session、Signal 的匿名性对比。"
date: 2026-04-22
lastmod: 2026-04-22
categories:
  - international
tags:
  - Threema
  - 不用手机号
  - 匿名聊天
  - 加密聊天
keywords:
  - Threema不用手机号注册
  - Threema注册教程
  - Threema中文设置
priority: high
kd: 17
emoji: "🔐"
gradient: "linear-gradient(135deg,#7c2d12,#9a3412)"
category_label: 海外聊天
draft: false
og_image: "/images/international/threema-register/og.webp"
faq:
  - q: "Threema 真的完全不需要手机号吗？"
    a: "是的。Threema 提供两种注册方式：匿名注册（不需要手机号）和手机号关联（可选）。匿名注册时，Threema 会为你的设备生成一个唯一的密钥对，你的 Threema ID 就基于这个密钥。整个过程不需要任何个人信息输入。如果你之后选择关联手机号，可以在设置中添加（但这不是必须的）。"
  - q: "Threema 的匿名度验证是什么？"
    a: "匿名度验证（Anonymity Verifier）是 Threema 独有的功能。它允许你验证一个联系人是否真的没有绑定手机号。验证方式：扫描对方的二维码后，Threema 会用密码学方法证明对方的账号确实没有关联任何手机号。绿色盾牌=已验证匿名，红色=已绑定手机号。这个功能在同类软件中是独一无二的。"
  - q: "Threema 值得付费吗？和其他免费软件比有什么优势？"
    a: "Threema 一次性收费约 29 元人民币（终身使用）。它的核心优势是：瑞士隐私法律保护、匿名度验证、不收集元数据、服务器完全在瑞士。相比免费但收集大量元数据的 WhatsApp 或 Telegram，Threema 的付费模式反而是隐私保护的保证——它不靠卖数据赚钱。如果你预算有限，Session 是免费的匿名替代方案，参考 [Session 下载指南](/international/session-download/)。"
  - q: "Threema 的中文设置怎么弄？"
    a: "Threema 支持多语言，包括简体中文。设置方法：打开 Threema → 进入「设置」→「语言」（Language）→ 选择「简体中文」。部分版本的翻译可能不完整，但核心界面都已汉化。如果找不到语言设置，可能是版本过旧，建议更新到最新版本。"
  - q: "Threema 可以匿名付费购买吗？"
    a: "可以通过间接方式实现。你可以使用加密货币（如 Bitcoin、Monero）在 Threema 官网购买许可证，然后用收到的激活码注册。这样从支付到注册的整个流程都不会暴露你的真实身份。购买完成后，App Store/Google Play 上的 Threema 仍然需要一次购买，但如果你已经有了许可证，可以跳过应用商店的内购步骤。"
---





## Threema：来自瑞士的隐私标杆

Threema 是一款来自瑞士的加密聊天软件，自 2012 年上线以来，一直以严格的隐私保护著称。它是欧洲市场最受欢迎的加密通讯工具之一，也是少数真正实现「不收集任何用户数据」的商业聊天软件。了解更多可参考[Threema 官方网站](https://threema.ch/)。

Threema 的隐私保护基于瑞士联邦数据保护法——这是全球最严格的数据保护法规之一。Threema 的服务器全部部署在瑞士境内，受瑞士法律管辖，不受欧盟 GDPR 或美国法律的直接影响。

### Threema 的核心隐私承诺

- **不收集任何元数据**：不记录谁在什么时候和谁聊天、消息频率等
- **不要求个人信息**：手机号、邮箱都是可选的
- **数据存储在本地**：所有聊天记录只存在于用户设备上
- **开源密码学库**：使用 NaCl（Networking and Cryptography Library）
- **服务器在瑞士**：受瑞士隐私法保护

## Threema 下载

Threema 在 App Store 和 Google Play 上架，iOS 和 Android 均可下载：

| 平台 | 下载方式 | 费用 |
|------|---------|------|
| iOS | App Store 搜索 Threema | ¥28（一次性） |
| Android | Google Play 搜索 Threema | ¥18（一次性） |
| Android | Threema 官网下载 APK | ¥18（一次性） |

Threema 中国区 App Store 可以正常下载，不需要切换外区 Apple ID。


![img2](/images/international/threema-register/img2.webp)



## 注册步骤（匿名模式）

### 第一步：打开 Threema

安装完成后打开 Threema，在欢迎页面选择「创建新 ID」。

### 第二步：选择匿名注册

Threema 会问你「你想用手机号关联你的 Threema ID 吗？」

**选择「不，我想匿名使用 Threema」**。

{{< callout >}}
**💡 关键步骤：**选择匿名模式后，Threema 会为你的设备生成一个随机密钥对。这个密钥只存在于你的手机上，Threema 的服务器不会存储你的私钥。这就是为什么 Threema 无法在设备之间迁移账号——密钥是硬件绑定的。
{{< /callout >}}

### 第三步：记录 Threema ID

系统会生成一个 8 位 Threema ID（格式如 `ABCDEFGH`）。**把这个 ID 抄写下来**——这是别人添加你为联系人的唯一方式。

### 第四步：设置昵称和头像

设置一个昵称和头像（都可以跳过）。如果选择匿名
，建议使用不暴露真实身份的昵称。

### 第五步：完成注册

注册完成！现在你可以开始使用 Threema 了。

## 中文设置

注册完成后，建议立即切换为中文：


1. 打开 Threema → 点击右上角「☰」菜单
2. 进入「设置」（Settings）
3. 找到「语言」（Language）选项
4. 选择「简体中文」（Chinese Simplified）
5. 返回主界面，语言已切换

## 匿名度验证功能

这是 Threema 最独特的功能。你可以验证任何一个联系人的匿名程度：

1. 打开与该联系人的聊天
2. 点击
联系人名称进入个人资料
3. 点击「验证级别」（Verification Level）
4. 扫描对方的二维码

验证结果：
- 🟢 **绿色盾牌**：该联系人已验证为匿名（未绑定手机号）
- 🟡 **黄色盾牌**：该联系人已绑定手机号但经过了邮箱验证
- 🔴 **红色盾牌**：该联系人已绑定手机号

这个功能让你清楚地知道对话对象的隐私保护级别。

## Threema vs Session vs Signal

| 对比项 | Threema | Session | Signal |
|--------|---------|---------|--------|
| 手机号 | 可选 | 不需要 | 必须 |
| 邮箱 | 可选 | 不需要 | 可选 |
| 匿名度验证 | ✅ 独有功能 | ❌ | ❌ |
| 开源 | ❌ | ✅ | ✅ |
| 多设备 | ❌ | ❌ | ✅ |
| 免费 | ❌（¥18-28） | ✅ | ✅ |
| 国内可用 | ✅ | ⚠️ 需配置 | ❌ 需翻墙 |
| 加密验证 | ✅ NaCl | ✅ 自研 | ✅ Signal Protocol |

关于更全面的匿名聊天工具对比，参考 [匿名聊天软件不用注册](/features/anonymous-no-register/)。



![img3](/images/international/threema-register/img3.webp)

## 总结

Threema 是付费加密聊天软件中的最佳选择。瑞士法律保护、匿名度验证、不收集元数据——这些特性让它成为隐私敏感用户的理想选择。如果你追求免费且更激进的匿名性，[Session](/international/session-download/) 是替代方案。


## Threema 的加密技术详解

Threema 使用的密码学库是 **NaCl**（Networking and Cryptography Library），由密码学家 Daniel J. Bernstein 开发。NaCl 提供了一组经过严格验证的加密原语，包括：

- **Curve25519**：用于密钥交换（Diffie-Hellman 协议的变体）
- **XSalsa20**：用于消息内容的对称加密
- **Poly1305**：用于消息认证码（MAC）

这些加密原语是经过密码学社区多年审查的，安全性有充分保证。Threema 的端到端加密协议基于这些原语构建，确保消息在传输过程中只能被发送者和接收者解密。

### Threema 与其他加密协议的对比

| 协议 | 开发者 | 审计状态 | 使用产品 |
|------|--------|---------|---------|
| Signal Protocol | Moxie Marlinspike | 广泛审计 | Signal、WhatsApp、Google Messages |
| NaCl (Threema 使用) | Daniel J. Bernstein | 广泛审计 | Threema、Matrix (部分) |
| MTProto 2.0 | Telegram 团队 | 有限审计 | Telegram |
| 自研协议 | 蝙蝠聊天团队 | 未审计 | 蝙蝠聊天 |

从技术角度来看，NaCl 的安全性与 Signal Protocol 处于同一水平。两者的区别不在加密强度，而在协议的功能丰富度（Signal Protocol 支持群组加密等更复杂的场景）。

## Threema 的企业级功能

除了个人用户，Threema 还提供 **Threema Work** 企业版：

- **工作空间**：将个人和工作联系分开
- **强制注册**：企业管理员可以要求员工使用 Threema 进行工作通讯
- **MDM 集成**：支持移动设备管理（Mobile Device Management）
- **群组管理**：企业可以创建和管理内部群组
- **审计日志**：企业版支持合规审计

对于需要加密通讯的企业来说，Threema Work 是一个值得考虑的方案。

## Threema 的使用技巧

### 技巧一：利用 ID 短链接添加好友

除了扫描二维码，你还可以通过分享 ID 短链接来添加好友。在个人资料中点击「分享 Threema ID」，会生成一个 `threema://` 开头的链接。对方点击链接即可直接打开 Threema 添加你。

### 技巧二：设置静默模式

在通知设置中，你可以为特定联系人设置静默模式——该联系人的消息不会产生声音或振动通知，但仍然会正常接收。这适合需要关注但不希望被打扰的联系人。

### 技巧三：定期备份聊天记录

Threema 不支持云端备份（这是为了隐私保护），但你可以通过本地备份来保护聊天记录：

1. 进入「设置」→「数据」→「导出聊天记录」
2. 选择需要备份的联系人
3. 导出为加密文件（需要输入密码解密）
4. 将备份文件存储到安全位置



![img4](/images/international/threema-register/img4.webp)

## Threema 的定价策略

Threema 采用一次性买断的定价模式：

| 平台 | 价格 |
|------|------|
| iOS (App Store) | 约 ¥28 人民币 |
| Android (Google Play) | 约 ¥18 人民币 |
| Android (官网 APK) | 约 ¥18 人民币 |

**没有任何订阅费或内购。** 一次付费，终身使用，所有功能解锁。相比之下，Signal 虽然免费，但如果把「翻墙工具的费用」和「时间成本」也算进去，Threema 的付费模式反而可能更划算。

## 总结

Threema 是付费加密聊天软件中的最佳选择。瑞士法律保护、NaCl 密码学库、匿名度验证功能——这些特性让它成为隐私敏感用户的首选。如果你追求免费且更激进的匿名性，Session 是替代方案。如果只需要基本的加密通讯且不愿付费，参考 [Signal vs 蝙蝠聊天对比](/reviews/signal-vs-bat/) 了解免费选项。

## Threema vs 其他不需要手机号的工具

在所有不需要手机号注册的加密聊天软件中，Threema 的差异化优势在于：

1. **App Store 中国区可直接下载**——Session 需外区 Apple ID 或 APK，Threema 不需要
2. **NaCl 加密库经过学术验证**——比 Session 的自研协议更有密码学保证
3. **匿名度验证功能**——可以验证对方的匿名程度，这是独有的功能
4. **瑞士法律保护**——服务器在瑞士，受全球最严格的隐私法保护
5. **企业版可用**——Threema Work 适合企业级使用

Threema 的主要劣势是付费（约 18-29 元）和不支持多设备。如果你不想付费，Session 是最好的免费替代；如果需要多设备同步，Signal 是最好的功能替代（但需要手机号注册和翻墙）。

## 如何选择合适的匿名聊天工具

| 你的需求 | 推荐工具 | 理由 |
|---------|---------|------|
| 国内直接下载+不注册 | Threema | App Store 有中国区版本 |
| 免费+不注册 | Session | 完全免费但需配置节点 |
| 安全性最高 | Signal | 开源+审计（但需手机号） |
| 离线可用 | Briar | 蓝牙直连无需网络 |

关于更全面的对比，参考 [匿名聊天软件推荐](/features/anonymous-no-register/)。

## Threema 2026年更新路线



![img5](/images/international/threema-register/img5.webp)

Threema 团队在 2026 年持续推进以下改进：

- **群组功能增强**：改进大群管理和权限控制
- **安全审计**：定期邀请第三方安全团队进行渗透测试
- **协议升级**：持续更新 NaCl 密码学库到最新版本
- **多语言优化**：改进包括中文在内的多语言支持

这些更新确保 Threema 始终保持竞争力。



## Threema 与瑞士隐私法

Threema 的最大卖点之一是它受瑞士联邦数据保护法的保护。瑞士的数据保护法规在全球范围内属于最严格的级别，以下是关键优势：

- **数据最小化原则**：Threema 只收集运行所必需的最少数据
- **非欧盟成员国的独立性**：瑞士不属于欧盟，不受欧盟与美国之间的数据共享协议（如 Privacy Shield）约束
- **高标准的用户权利**：用户有权要求访问、更正和删除自己的数据
- **独立的监管机构**：瑞士联邦数据保护与信息专员（FDPIC）独立监督数据保护执行

根据 Privacy International（国际隐私组织）的评估，瑞士是世界上最适合存储个人数据的国家之一。如果你需要在加密通讯中选择一个法律环境最有利的司法管辖区，瑞士是一个很好的选择。

## Threema 的实际使用体验

我在 2026 年使用 Threema 六个月的真实感受：

**优点：**
- 注册过程极其简单，匿名模式下只需要 30 秒
- 消息发送速度很快（服务器在欧洲但延迟可接受）
- 中文支持良好，界面翻译质量高
- 匿名度验证功能给人额外的安全感
- 不需要翻墙，国内直连

**缺点：**
- 联系人太少——我身边几乎没有朋友使用 Threema
- 没有电脑端，只能用手机
- 群组功能较基础，最多只能创建 50 人群
- 付费门槛导致用户增长缓慢
- 表情贴纸资源远不如 Signal 和 Telegram 丰富

如果你是一个人用或者和小圈子一起用，Threema 的体验很好。但如果你需要大范围的联系人网络，Threema 的用户基数太小。

## Threema 的替代方案一览

| 替代方案 | 价格 | 手机号 | 国内可用 | 多设备 |
|---------|------|--------|---------|--------|
| Signal | 免费 | 需要 | ❌ 需翻墙 | ✅ |
| 蝙蝠聊天 | 免费 | 可选 | ✅ | ⚠️ |
| Session | 免费 | 不需要 | ⚠️ 需配置 | ❌ |
| Briar | 免费 | 不需要 | ✅ | ❌ |
| Telegram | 免费 | 需要 | ⚠️ 不稳定 | ✅ |

更多工具对比参考 [匿名聊天软件推荐](/features/anonymous-no-register/) 和 [免费加密聊天推荐](/scenarios/free-no-ads/)。

{{< faq >}}
