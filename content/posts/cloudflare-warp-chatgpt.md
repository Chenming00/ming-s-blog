---
title: "Unlock Chat GPT with Cloudflare WARP"
date: 2023-02-11T13:33:35+08:00
draft: false
---

## 原理分析
**Cloudflare WARP**拥有很多IP，而ChatGPT的CDN又是Cloudflare提供的，也就是说，能不能访问完全取决于Cloudflare。因此使用Cloudflare自己的IP大概率不会被Ban。除了WARP之外，iCloud Private Relay也是Cloudflare的IP哦。

## 具体步骤
**本文的方案仅改变IPv6出口IP，不会改变IPv4出口IP，更不会改变路由。**

1. 准备一台VPS，需要是OpenGPT支持的161个国家之一。因为你的网络在哪里，WARP就会使用你所在地的IP。比如香港就不行。

[Supported countries and territories](https://platform.openai.com/docs/supported-countries)

2. 使用以下命令安装WARP。
```
bash <(curl -fsSL git.io/warp.sh) proxy
```

3. 配置XrayR/V2Ray的出站规则和路由。（以XrayR为例，XrayR/V2Ray的使用本文略过）
```json
# custom_outbound.json
{
    "tag": "socks5-warp",
    "protocol": "socks",
    "settings": {
        "servers": [{
            "address": "127.0.0.1",
            "port": 40000
        }]
    }
}
# route.json
{
    "type": "field",
    "outboundTag": "socks5-warp",
    "ip": ["::/0"]
}
```
简单解释一下，出站规则是指出站走40000端口的SOCKS代理。路由规则是指所有IPv6出站均走SOCKS代理。

4. 如果你只是想让OpenAI走WARP的IPv6，可以这样写。
```json
# route.json
{
    "type": "field",
    "outboundTag": "socks5-warp",
    "domain": ["openai.com"]
}
```




