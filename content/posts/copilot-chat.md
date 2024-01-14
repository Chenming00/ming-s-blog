---
title: "Use Copilot for free unlimited use of GPT-4 API"
date: 2024-01-14T09:31:34-05:00
draft: false
tags: [GPT-4, Copilot, ChatGPT]
---

> Copilot 是 GitHub 提供的一项 AI 代码补全的工具，不久之前增加了 Chat 的功能。正是因为支持了 Chat 功能，所以可以把 Copilot Chat 的 API 转换为 OpenAI 官方的 API。重要的是，还支持 GPT-4，虽然不是最新版本的 GPT-4 模型，但是基本也够用。

## 准备工作
- GitHub 帐号 （有 Copilot 权限的，我用的是 GitHub Student Pack）
- 海外 VPS （确保能访问 Copilot Chat API）

## 部署
在开始之前，先获取你的 Copilot Token。

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/aaamoon/copilot-gpt4-service/master/shells/get_copilot_token.sh)"
```

接下来主要使用的是 [aaamoon/copilot-gpt4-service](https://github.com/aaamoon/copilot-gpt4-service)，GitHub 目前的版本还没有合并我的 PR，所以在部署之后，每次请求都应该携带在上一步获取的 **Copilot Token**。我改进之后的版本是当你在环境变量或者配置文件中填写了 Copilot Token，则无需在每次请求时携带，会优先使用环境变量或者配置文件提供的 Token。

```bash
mkdir copilot-gpt4-service && cd copilot-gpt4-service
wget -O compose.yaml https://raw.githubusercontent.com/missuo/copilot-gpt4-service/dev/docker-compose.yml
nano compose.yaml # 修改成你自己的 COPILOT_TOKEN
docker compose up -d
```

部署完成后即可在任何支持 OpenAI API 的 App 中填写你的 API Endpoint，如果 API Key 不能留空的话可以随便写。

## 注意事项
- 如果你使用了我改进的版本部署，请注意你的 API 是完全开放的，不要泄露你的 API
- 建议不要使用 GitHub 大号的 Token，否则可能会封号，我是直接买了一个帐号，花费 40CNY
