---
title: "Upgrade ChatGPT Plus bypassing restrictions"
date: 2023-11-17T16:10:07-05:00
draft: false
tags: [ChatGPT, ChatGPT Plus]
---

> 在前段时间 ChatGPT 不再允许新用户订阅 ChatGPT Plus 方案，前几天我刷到了一个偷渡升级的方案，发在了我的 Twitter，但是没具体说如何执行这段代码，本篇文章主要就是介绍完整的操作流程。

### 登录帐号
直接访问 [https://chat.openai.com/api/auth/session](https://chat.openai.com/api/auth/session)，你可以在这里面找到一个 **accessToken** 的数据。复制 **accessToken** 的 Value。如果你是小白，不知道怎么找到的话，建议你复制到 [https://jsonformatter.org](https://jsonformatter.org) 后查看，或者安装 Chrome 插件 [JSON Viewer](https://chrome.google.com/webstore/detail/gbmdgpbipfallnflgajpaliibnhdgobh)。

![20231117dUCdKY](https://r2.qwq.mx/blog/20231117dUCdKY.png)

你应该完整的复制 **eyxxxx** 开头的字符串。

### 补全代码
粘贴到 {accessToken} 处，注意不要保留 {}。
```js
await fetch("https://chat.openai.com/backend-api/payments/checkout", {
    method: "POST",
    headers: {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Authorization": "Bearer {accessToken}"
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer' 
})
.then(response => response.text()) 
.then(result => console.log(result))
.catch(error => console.log('error', error));
```
### 执行代码
复制完整的代码，打开浏览器，确保这个浏览器已经登录过你的 ChatGPT 帐号，右击选择 **检查元素**，或者直接按下 **F12**，选择 `Console`，粘贴代码，按下回车。顺利的话会看到生成了一个链接。

![20231117sZDlvt](https://r2.qwq.mx/blog/20231117sZDlvt.png)

点击这个链接，你就会跳转到熟悉的界面。

![20231117ZJpsYv](https://r2.qwq.mx/blog/20231117ZJpsYv.png)

大胆的输入你的卡片信息即可成功订阅。

### 总结
ChatGPT 官方似乎没有完全关闭订阅通道，这个方案直到美国东部时间(EDT) 2023年11月17日 16:25 可行，想要订阅抓紧时间，不要错过机会了。