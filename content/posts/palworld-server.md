---
title: "Palworld Dedicated Server Setup"
date: 2024-01-23T20:25:20-05:00
draft: false
tags: [Palworld]
---

> 今天朋友问我能不能用我家的服务器搭建一个 Palworld，我看了一下网上的教程，用 Linux 还挺麻烦。直到我找到了 GitHub 的 Docker 版本。

## 准备工作
- 性能还不错的 Linux 服务器 （我这边是家里的服务器）
- 安装了 Docker

## 启动 
```bash
mkdir palworld && cd palworld
nano compose.yaml
```

```
services:
   palworld:
      image: thijsvanloef/palworld-server-docker:latest
      restart: unless-stopped
      container_name: palworld-server
      ports:
        - 8211:8211/udp
        - 27015:27015/udp
      environment:
         - PUID=1000
         - PGID=1000
         - PORT=8211 # Optional but recommended
         - PLAYERS=16 # Optional but recommended
         - MULTITHREADING=true
         - RCON_ENABLED=true
         - RCON_PORT=25575
         - ADMIN_PASSWORD="adminPasswordHere"
         - COMMUNITY=false  # Enable this if you want your server to show up in the community servers tab, USE WITH SERVER_PASSWORD!
         # Enable the environment variables below if you have COMMUNITY=true
         # - SERVER_PASSWORD="worldofpals"
         # - SERVER_NAME="World of Pals"
      volumes:
         - ./palworld:/palworld/
```

复制粘贴上面的内容，可以修改一下 **ADMIN_PASSWORD**。

```bash
docker compose up -d
```

最后记得开放一下 8211 和 27015 端口，记得开启 UDP。

PS: 美国东部的朋友可以用我搭建的服务器。

## Reference
- [https://github.com/thijsvanloef/palworld-server-docker](https://github.com/thijsvanloef/palworld-server-docker)
- [https://github.com/jammsen/docker-palworld-dedicated-server](https://github.com/jammsen/docker-palworld-dedicated-server)
