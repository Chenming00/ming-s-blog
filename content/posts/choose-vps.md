---
title: "How to choose a VPS with fast speed to Mainland China."
date: 2023-10-12T21:43:56-04:00
draft: false
tags: [VPS, Looking Glass]
---
> 从 2019 年开始陆陆续续用过的 VPS 商家超过可能有 200 家以上，~~尽管很多已经跑路了~~。其中因为玩这些 VPS 认识了很多朋友。这篇文章主要针对作为 Proxy Server，别的用途例如建站、存储和跑项目不考虑。

## 初步判断
- 选择支持 **PayPal** 支付的商家，如果存在多种支付方式，建议选择 PayPal 支付。主要是为了防止商家跑路，如果你买的是月付，其实 Alipay 这些付款方式也可以接受，毕竟月付一般情况下最多 10USD 左右。
- 足够的流量和带宽，一般情况下个人使用至少有 500G 以上的流量和 500M 以上的带宽才够用。
- IP 的解锁情况，最好可以解锁一些流媒体，但是这不是最重要的，后面我会讲到。
- IP 的路由情况，这是至关重要的，这会直接影响速度，具体的判断后面也会讲到。
- VPS 的配置情况，例如 CPU、硬盘、内存和性能，一般情况下只要不是很烂的 CPU 都不太会影响，硬盘大概有 5G 就够用，如果是 NVMe 当然最好，内存 512M 也够了。

## 路由判断
因为路由直接影响速度，因此我先讲讲这至关重要的一部分。路由只要分为去程和回程。去程也就是从你的 IP 到达 VPS，回程则是反过来。去程的测试知道 VPS 的 IP 就可以测试，而回程需要使用 VPS，如果有的商家提供 **Looking Glass** 也可以提前测试。

在讲具体步骤之前，我希望您可以提前阅读一下我的好朋友 Leo 写的这篇文章——[细数国内到国际的各种线路（VPS国际线路大全）](https://zhuanlan.zhihu.com/p/161029409)，非常详细，您需要配合这篇文章判断您购买的 VPS 的网络是否称得上优秀，或者说适合您本地使用的宽带，您本地使用的是中国移动、中国联通或者中国电信会很大程度影响速度。

### 去程判断
#### 使用 [IPIP.NET](https://tools.ipip.net/traceroute.php)
仅需要选择你当地的运营商的测试节点，输入目标的 IP，即可展示完整的路由。大部分情况下，应该还算是准确。当然，如果你希望获得更可靠的结果，请参考第二种方式。

#### 使用 [NextTrace](https://github.com/nxtrace/NTrace-core)
这是一款开源的路由追踪工具，当然在之前有一款叫作 **BestTrace**。BestTrace 的一些限制让用户会非常难受，因此在两年前我和我的好朋友 [Leo](https://leo.moe) 开始有了开发 [NextTrace](https://github.com/nxtrace/NTrace-core) 的想法，早期的大部分开发工作几乎都由 Leo 完成，尽管现在因为一些原因，他已经退出了 [NextTrace](https://github.com/nxtrace/NTrace-core) 的开发工作。当然我们也有一些新的想法，拭目以待吧！请允许我废话那么多。这款工具的简单用法如下：

```bash
brew install nexttrace
nexttrace -T [VPS_IP]
```

### 回程判断
在 VPS 上使用 **NextTrace** 查看到你家的路由。例如上海电信：
```bash
bash -c "$(curl http://nexttrace-io-leomoe-api-a0.shop/nt_install_v1.sh)"
nexttrace -T sh.189.cn
```

## 优化路由
玩法有很多，我只说一些简单的。使用支持 WebSocket 的 CDN，例如 Cloudflare、CloudFront 等等。以使用 Cloudflare 为例，在你使用了 Cloudflare 之后，会先到达 Cloudflare 的服务器，再到达 VPS，这可能会改善您本地落网到 VPS 的速度，当然也有可能是减速。高阶的玩法，可以自选 Cloudflare IP。

## 解锁流媒体
目前来看，最好的解锁流媒体的方式就是使用 Cloudflare Warp。可以使用这个非常优秀的 [安装脚本](https://github.com/P3TERX/warp.sh)。一般情况下，你可以只修改 IPv6 的出站 IP。

## 我使用的 VPS 的一些总结
> 我不会提供任何 AFF 链接，意味着您买哪一家我都不会获得任何收益。
- 不建议购买 RackNerd 和 CloudCone 这类非常廉价的 VPS，尽管很多人在推荐。我曾经用过一年的 RN，他绝对称不上优秀，唯一的优势可能就是便宜了。在廉价的商家里，我会觉得 BuyVM 会更胜一筹。
- BandwagonHost 是个非常不错的选择，当然非常非常的贵，怀念很多年前只要年付 19.99USD 的 CN2 GIA。他们家的 CN2 GIA 和 BBETC（联通用户） 都不错。
- GreenCloudVPS 我用的最久的商家之一，日本东京的 IIJ 线路非常不错。
- Linode 和 Vultr 这两家差不多，都是知名的大商家，在日本的机器最受欢迎，NTT 线路晚高峰非常慢。当然 Vultr 可以白嫖免费的 VPS，我在用西雅图的。
- DigitalOcean 也是一家大商家，移动用户可以值得一试新加坡地区。
- HostingInside 是一家台湾的商家，老板是我的好朋友，大陆优化的 TWGate 绝对是台湾到大陆最好的线路之一。