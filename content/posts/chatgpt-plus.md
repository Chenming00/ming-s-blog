---
title: "I subscribed to ChatGPT Plus"
date: 2023-02-11T07:04:11+08:00
draft: false
tags: [ChatGPT, ChatGPT Plus, OpenAI]
---

## ChatGPT Plus 功能
- Available even when demand is high 即使在需求大的时候也可以使用
- Faster response speed 更快的反应速度
- Priority access to new features 优先获得新功能

## 订阅
### 正常方式
填写 [表格](https://docs.google.com/forms/d/e/1FAIpQLScee6ST3o-kZDjlw1ROfUNyjuRBwGdcoewxjCULNejbP5hdzQ/viewform) 并等待官方给你发送电子邮件获取资格。

### 漏洞
在中国时间的 2 月 10 日下午，看到群里有很多朋友说出现了 **Upgrade Plan** 的按钮，我立即登陆了我的帐号发现确实也有了，但是因为中国信用卡无法支付，导致开通失败。2 月 11 日我再次登录的时候发现已经消失了这个按钮。  

我翻看了我的 **Chrome 历史记录**，找到了一个 [pay.openai.com](https://pay.openai.com) 的链接，点进去发现还是熟悉的 **Stripe** 的界面。但是奇怪的事情是 **我无法填写地址信息**，但是没有地址信息无法提交。无奈之下，当然是按下 F12，找到填写地址的每一个 **input** 标签，把 **disable** 全部改为 **enable**，顺利地填写了信息。在我的好朋友 **Ming** 的帮助下，用他的美国卡支付，没有显示成功的界面，一直显示处理中，但是收到了订阅成功的邮件。回到 [chat.openai.com](https://chat.openai.com) 发现已经开通好了。

## 体验
Plus 版本有两个模式，分别是 **Default** 和 **Turbo**。  
![202302114W6T0j](https://r2.qwq.mx/blog/202302114W6T0j.png)

根据描述和实际体验，**Turbo** 模式显然要快很多，回复速度比免费版有了很大的提升，很少有遇到崩溃的情况。当然英文提问会比中文回复速度快很多。  

## IP 的问题
### 无法访问
ChatGPT 封锁了很多机房的 IP，因为 ChatGPT 使用的是 [Cloudflare](https://cloudflare.com) 的服务，我猜测是使用了 **Country** 匹配，也就是说只有在指定国家可用，目前是 161 个国家。除此之外，应该还加入了 **Threat Score** 和 **Known Bots** 的判断。意味着你的 IP 要想顺利访问，需要具备两个条件，IP 属于来自 161 个国家之一，并且你的 IP 危险分数足够低。  

### 我的方案
在 2022 年 3 月 28 日，我在 RIPE 申请到了 ASN，也就意味着我可以持有 IPv4 和 IPv6，我目前持有两个/48 的 IPv6。我目前的 IPv6 分别来自 **台湾** 和 **英国**，都在 161 个国家之内，危险分数都是 0。我建立了 BGP Session，完全可以使用自己的 IP 来访问 OpenAI 的服务。  
![20230211Dlnlje](https://r2.qwq.mx/blog/20230211Dlnlje.png)
```
Prefixes:
2401:95c0:f001::/48
2a0f:9400:6907::/48
```

### 检测是否可用
为了验证当前IP是否能够正常使用OpenAI服务，我用Shell写了一个检测脚本——[OpenAI-Checker](https://github.com/missuo/OpenAI-Checker)。使用方法也非常简单，仅需要在任何Linux/macOS上执行以下命令。
```shell
bash <(curl -Ls https://cpp.li/openai)
```
检测结果示例：
```
> bash <(curl -Ls https://cpp.li/openai)
OpenAI Access Checker. Made by Vincent
https://github.com/missuo/OpenAI-Checker
-------------------------------------
[IPv4]
Your IPv4: 205.185.1.1 - FranTech Solutions
Your IP supports access to OpenAI. Region: US
-------------------------------------
[IPv6]
Your IPv6: 2401: 95c0: f001:: 1 - Vincent Yang
Your IP supports access to OpenAI. Region: TW
-------------------------------------
```
## 总结
ChatGPT Plus的订阅价格为20美元/月，其实我觉得还可以，毕竟它能让你的体验更好，它能帮助你做很多事。只是中国大陆用户需要解决网络、绑定手机和支付问题，这一下子提高了使用门槛。
