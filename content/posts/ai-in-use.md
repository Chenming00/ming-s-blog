---
title: "我在用的 AI 工具：2024 年的一份使用记录"
date: 2024-04-20T08:25:21-04:00
draft: false
tags: [AI, LLM, Tools]
summary: "整理截至 2024 年 4 月的 AI 订阅、API、聚合平台与个人项目，以及当时的使用习惯。"
---

> 本文记录截至 **2024 年 4 月 20 日**的使用情况。模型、额度、定价及项目维护状态均保留当时的背景。

从 2023 年 2 月开始尝试 ChatGPT，到写下这篇文章时，已经过去了一年多。

我一直喜欢试新工具。以前 iOS 一出 Beta 就想升级，哪怕碰到 Bug，也愿意顺手提交反馈。生成式 AI 兴起后，也是同样的心情：先用起来，看看它能帮我做什么。

一年多下来，订阅、API 和自己折腾的项目攒了不少，是时候整理一份使用记录了。

## 从能用上，到找到适合的工具

最早使用这些平台时，手机号验证、网络和支付都需要花时间处理。最初的订阅，是好朋友 **Ming** 用 BoA 信用卡帮忙支付的。

后来到了美国，有了当地银行卡，体验这些服务方便了许多，也逐渐形成了自己的工具组合。截至原文写作时，我使用中的账号还没有遇到封禁。

## 日常最常用的三个平台

| 平台 | 当时的订阅 | 大致使用占比 | 主要用途 |
| --- | --- | --- | --- |
| ChatGPT | Plus、Team | 50% | 写代码、生成文本 |
| Claude | Pro | 40% | 写代码 |
| Perplexity | Pro | 10% | 检索信息、搜索 |

我的主要使用场景还是写代码。最初几乎完全依赖 ChatGPT，后来逐渐把一部分编程任务交给 Claude Opus。在当时的个人体验中，我更喜欢 Opus 处理这类任务的表现。

Perplexity 是后来加入的，主要用来查资料。当时记录的每日 600 次额度，对我的使用量来说已经足够。

## API：翻译常用，其余备用

| 服务 | 当时使用的模型 | 用途 |
| --- | --- | --- |
| OpenAI | GPT-3.5-Turbo | Bob 翻译 |
| Cohere | Command R+ | Bob 翻译 |
| Azure | GPT-4 | 备用 |
| Claude | Opus | 备用 |
| Bedrock | Haiku、Sonnet | 备用 |

订阅平台承担日常对话和编程，API 则更多用在翻译插件和自己的小项目里。

## 部署过的第三方项目

- **[Lobe Chat](https://github.com/lobehub/lobe-chat)**：界面好看，也方便在不同模型之间切换。我会把部署好的入口分享给朋友。
- **[Next Chat](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)**：当时已经逐渐减少使用，只保留了一个 GPT-3.5-Turbo 部署供朋友体验。
- **[one-api](https://github.com/songquanpeng/one-api)**：用来聚合多个服务的 API，统一接口和分发 Key。当时我也在使用价格约为官方一半的 API Key，具体费用属于那一阶段的记录。

## 我折腾的几个项目

### Bob 翻译插件

- **[bob-plugin-cohere](https://github.com/missuo/bob-plugin-cohere)**：在 Bob 中调用 Cohere Command R+，是我当时最常用的翻译方案。
- **[bob-plugin-copilot](https://github.com/missuo/bob-plugin-copilot)**：通过模拟 GitHub Copilot 请求，在 Bob 中调用 GPT-4 翻译；截至 2024 年 4 月已停止维护。

### API 适配与代理

- **[cohere2openai](https://github.com/missuo/cohere2openai)**：把 Cohere API 转成 OpenAI 兼容接口，方便接入已有应用。
- **[claude2openai](https://github.com/missuo/claude2openai)**：为 Claude API 提供 OpenAI 兼容接口。
- **[ClaudeProxy](https://github.com/missuo/ClaudeProxy)**：集中转发 Claude API 请求，让上游请求来自同一个出口 IP。
- **[FreeGPT35](https://github.com/missuo/FreeGPT35)**：基于当时免登录使用 ChatGPT 的方式提供 GPT-3.5-Turbo API，当时就存在随时失效的可能。

如果遇到项目问题，可以在对应 GitHub 仓库提交 Issue。我会在有空时处理，也欢迎留下新的需求。

## 当时的使用经验

那段时间，我主要通过美国住宅网络访问服务，也试过商业网络。当时约有 10 位朋友共同使用账号，持续半年多没有遇到封禁。这是彼时这些账号的实际情况，服务规则与其他账号的使用结果还需要分别看待。

Cohere 当时提供的 Trial Key，也是我体验 Command R+ 的入口之一。

回头看，这一年最大的变化，是从只用一个平台，慢慢变成按任务选工具：编程、翻译和检索各有常用的选择。把它们记下来，既方便自己回顾，也给同样爱折腾工具的人留一点参考。

---

> 写作说明：本文由 **GPT** 根据原始内容整理、润色并撰写。
