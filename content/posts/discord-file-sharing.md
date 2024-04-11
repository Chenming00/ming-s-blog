---
title: "File Sharing via Discord Bot"
date: 2024-04-10T20:04:15-04:00
draft: false
tags: [Discord, Go, File Sharing]
---

用过 Discord 的朋友应该知道，在任何的 Server 里面发的图片，音频，视频以及别的任何文件，都会生成一个以 `https://cdn.discordapp.com/attachments/` 开头的链接。这个链接是可以直接访问的，但是不幸的是这个链接会在 24 小时后失效。但是只要每 24 小时获取一次最新的链接，应该就可以利用这一点来实现图床或者是文件共享的功能。

Discord 似乎个人账户是不存在 API 的，但是可以随意地创建 Bot，我们只要创建一个 Bot，然后把 Bot 添加到你自己私有的 Server 之后，给 Bot 赋予发送消息和媒体文件的权限，就可以通过 API 接收文件，然后再通过 Bot 发送文件到 Channel 里面。

这里我使用 Go 来实现这个功能，首先我们需要一个 Bot 的 Token，这个 Token 可以在 [Discord Developer Portal](https://discord.com/developers/applications) 里面创建一个 Bot 之后获取到。

在 [https://github.com/missuo/discord-image](https://github.com/missuo/discord-image) 的设计中，每次上传完文件（以图片为例），并不会直接返回 Discord 的链接，而是返回一个 `https://example.com/file/{message_id}` 的链接，`/file` 是一个 API，每次请求这个 API 都会去 Discord 获取最新的链接，然后返回给用户。这样就实现了链接用不失效的效果。

除此之外，由于 `cdn.discordapp.com` 在中国大陆已经被 GFW 封锁，但是关于这个问题，可以用简单的 Nginx Reverse Proxy 或者是 Cloudflare Worker 来解决。

比起我之前分享过的 Telegraph 来说，利用 Discord 支持单文件 25MB，而过去的 Telegraph 只支持 5MB，这样的话，我们就可以利用 Discord 来分享更大的文件。而且 Discord 支持的文件类型更加丰富，过去利用 Telegraph 上传之后是无法进行删除的操作的，而 Discord 可以直接在你的 Channel 直接删除文件。

但是也存在一些局限性，例如 Discord 某个 Server 的 Attachments 可能有最大容量的上限，这一点我还不确定。除此之外，如果你的 Bot 被封禁了，你再创建一个新的 Bot，你之前所有的链接都会失效，原因是新的 Bot 在进入 Server 之后，没办法看到历史的记录，也就没办法获取到之前上传的文件的 URL。

我不知道能存活多久，且用且珍惜吧。