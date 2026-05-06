#!/usr/bin/env python3
# generate-missing-images.py — 生成剩余的图片

import sys
import json
import hashlib
import time
import urllib.request
import os

# ── 配置 ──────────────────────────────────────────
APP_ID  = "100003"
APP_KEY = "38d2391985e2369a5fb8227d8e6cd5e5"
URL     = "https://autoglm-api.zhipuai.cn/agentdr/v1/assistant/skills/generate-image"
TOKEN_URL = "http://127.0.0.1:18432/get_token"

def get_token():
    """获取token"""
    try:
        with urllib.request.urlopen(TOKEN_URL) as resp:
            token = resp.read().decode("utf-8").strip()
        if not token.lower().startswith("bearer "):
            token = f"Bearer {token}"
        return token
    except Exception as e:
        print(f"ERROR: 无法从本地服务获取 token: {e}")
        return None

def generate_image(prompt, output_path):
    """生成图片并保存"""
    token = get_token()
    if not token:
        return False
    
    # 生成签名
    timestamp = str(int(time.time()))
    sign_data = f"{APP_ID}&{timestamp}&{APP_KEY}"
    sign = hashlib.md5(sign_data.encode("utf-8")).hexdigest()
    
    # 发起请求
    payload = json.dumps({"text": prompt}).encode("utf-8")
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "X-Auth-Appid": APP_ID,
        "X-Auth-TimeStamp": timestamp,
        "X-Auth-Sign": sign,
    }
    
    try:
        req = urllib.request.Request(URL, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            
            if result.get("code") == 0 and "data" in result and "image_url" in result["data"]:
                image_url = result["data"]["image_url"]
                
                # 下载图片
                urllib.request.urlretrieve(image_url, output_path)
                print(f"=== 图片已保存: {output_path} ===")
                return True
            else:
                print(f"=== 图片生成失败: {result} ===")
                return False
                
    except Exception as e:
        print(f"=== 请求失败: {e} ===")
        return False

def main():
    # 需要生成的图片
    images = [
        {
            "prompt": "手机屏幕展示多款加密通讯软件对比界面，包括Signal、蝙蝠聊天、Telegram等应用的图标和特点，界面清晰易懂，科技感十足，背景为深色主题",
            "filename": "encryption-apps-comparison.webp"
        },
        {
            "prompt": "阅后即焚功能示意图，手机屏幕上显示一条消息正在消失，带有沙漏计时器图标，背景为渐变紫色，体现消息短暂性和私密性，UI界面现代化",
            "filename": "burn-after-read-feature.webp"
        }
    ]
    
    # 图片保存目录
    output_dir = "C:\\Projects\\encrypted-chat-seo\\static\\images\\scenarios\\couple-private-chat"
    
    print("=== 开始生成剩余图片 ===")
    
    for i, image_info in enumerate(images, 1):
        print(f"\n=== 生成第{i}张图片 ===")
        output_path = os.path.join(output_dir, image_info["filename"])
        
        if generate_image(image_info["prompt"], output_path):
            print(f"=== 第{i}张图片生成成功 ===")
        else:
            print(f"=== 第{i}张图片生成失败 ===")
    
    print("\n=== 所有剩余图片生成完成 ===")

if __name__ == "__main__":
    main()