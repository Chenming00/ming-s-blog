---
title: "Unlock ChatGPT with Cloudflare WARP"
date: 2023-02-11T13:33:35+08:00
draft: false
tags: [ChatGPT, ChatGPT Plus, OpenAI, WARP, Cloudflare]
---

## 原理分析
**Cloudflare WARP** 拥有很多 IP，而 ChatGPT 的 CDN 又是 Cloudflare 提供的，也就是说，能不能访问完全取决于 Cloudflare。因此使用 Cloudflare 自己的 IP 大概率不会被 Ban。除了 WARP 之外，iCloud Private Relay 也是 Cloudflare 的 IP 哦。

## 具体步骤
**本文的方案仅改变 IPv6 出口 IP，不会改变 IPv4 出口 IP，更不会改变路由。**

1. 准备一台 VPS，需要是 OpenGPT 支持的 161 个国家之一。因为你的网络在哪里，WARP 就会使用你所在地的 IP。比如香港就不行。

[Supported countries and territories](https://platform.openai.com/docs/supported-countries)

2. 使用以下命令安装 WARP。
```
bash <(curl -fsSL git.io/warp.sh) proxy
```

3. 配置 XrayR/V2Ray 的出站规则和路由。（以 XrayR 为例，XrayR/V2Ray 的使用本文略过）
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
简单解释一下，出站规则是指出站走 40000 端口的 SOCKS 代理。路由规则是指所有 IPv6 出站均走 SOCKS 代理。

4. 如果你只是想让 OpenAI 走 WARP 的 IPv6，可以这样写。
```json
# route.json
{
    "type": "field",
    "outboundTag": "socks5-warp",
    "domain": ["openai.com"]
}
```




