---
title: "AI ​​I’m currently using"
date: 2024-04-20T08:25:21-04:00
draft: false
tags: [AI, LLM, Tools]
---

> 本文最后更新于 2024 年 4 月 20 日，未来可能会更新更多我在用的 AI 工具。

2023 年 2 月 ChatGPT 发布以来，已经过去一年多的时间了。作为一个科技爱好者，每一次的 iOS Beta 更新都会让我兴奋不已，我会在第一时间更新，即使有很多的 Bug，我也愿意作为那个上报 Bug 的人。而对于最近一年兴起的生成式 AI 也是如此，我从 2023 年 2 月开始，一直在使用各种类似的工具。我想一年过去了，我有必要分享一些我在用的工具，以及最近一年我自己写的相关的项目。

从 ChatGPT 的诞生到今天，想要使用这些平台都有一些门槛，最早的 ChatGPT 必须要验证手机号以及需要魔法以外，最让人头大的是支付方式，最初我的帐号的支付都是用的我好朋友 **Ming** 的 BoA 信用卡。然而没过多久我来到了美国，直到今天我有了很多美国银行的银行卡，然而这些平台几乎都诞生于美国，几乎所有的平台都支持给美国的用户使用。因此，我也就有机会体验所有新出的 AI 模型。值得一提的是，直到今天，我被封号率为 **0%**。

## 平台

| 平台 | 订阅 | 使用频率 | 使用场景 |
| --- | --- | --- | --- |
| ChatGPT | Plus & Team | 50% | 写代码/文本生成 |
| Claude | Pro | 40% | 写代码 |
| Perplexity | Pro | 10% | 检索信息/搜索引擎 |

我自己其实最多的场景还是写代码，之前就是单平台，完全依赖 ChatGPT，现在逐渐将这些场景交给 Claude Opus，个人觉得 Opus 比起 GPT-4 的表现更优秀。而 Perplexity 是我最近才开始使用的，主要是用来检索信息，它的优点就是使用次数可以很多，每天 600 次对我来说绰绰有余。

## API

| API | 模型 | 使用场景 |
| --- | --- | --- |
| OpenAI | GPT-3.5-Turbo | Bob 翻译 |
| Cohere | Command R+ | Bob 翻译 |
| Azure | GPT-4 | 备用 |
| Claude | Opus | 备用 |
| Bedrock | Haiku / Sonnet | 备用 |

## 第三方项目

- [Lobe Chat](https://github.com/lobehub/lobe-chat)：颜值很高的聚合 AI 平台，可以随意切换各种模型，方便我分享给国内的朋友使用。
- [Next Chat](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)：现在慢慢抛弃了，只部署了一个 GPT-3.5-Turbo，供朋友免费使用。
- [one-api](https://github.com/songquanpeng/one-api)：API 聚合平台，支持几乎所有的 API，还支持分发 API Key，方便共享给朋友使用，目前我在使用官方半价的 API Key，同时也支持将所有 API 转换成 OpenAI 的 API。

## 我的项目

- [bob-plugin-cohere](https://github.com/missuo/bob-plugin-cohere)：Cohere 的 Bob 翻译插件，可以在 Bob 上使用 Cohere 的 Command R+ 模型，这是我目前最常用的翻译模型了。
- [bob-plugin-copilot](https://github.com/missuo/bob-plugin-copilot)：利用模拟 GitHub Copilot 的请求，可以在 Bob 上使用 OpenAI 的 GPT-4 模型进行翻译，**目前已经不再维护**。
- [cohere2openai](https://github.com/missuo/cohere2openai)：将 Cohere 的 API 转换成兼容 OpenAI 的 API，方便在任何兼容 OpenAI 的应用中调用 Cohere 模型。
- [claude2openai](https://github.com/missuo/claude2openai)：将 Claude 的 API 转换成兼容 OpenAI 的 API，方便在任何兼容 OpenAI 的应用中调用 Claude 模型。
- [ClaudeProxy](https://github.com/missuo/ClaudeProxy)：Claude API 代理，让所有向 Claude API 发送的请求都来自一个 IP，避免被封号。
- [FreeGPT35](https://github.com/missuo/FreeGPT35)：利用免登录使用 ChatGPT 实现的免费 GPT-3.5-Turbo API，目前可能随时失效。

以上项目如果在使用过程中遇到任何问题，请在 GitHub 上提 issue，我会在空余时间尽快解决。如果你有别的觉得有必要的需求，也可以在评论区留言，我会考虑实现。

## 一些经验

建议不要使用美国以外的 IP 请求 Claude 的 API，否则很容易被封号。建议使用美国 Residential IP，实在没条件也可以使用 Business IP。实际测试下来 ChatGPT 和 Claude 帐号可以共享给很多人使用，并不会封号。目前我的帐号大概有 10 个朋友在用，都是来自美国家宽的 IP，已经持续超过半年的时间，没有任何问题。