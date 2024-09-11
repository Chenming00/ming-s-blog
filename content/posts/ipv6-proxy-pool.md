---
title: "IPv6 Proxy Pool Configuration"
date: 2024-09-11T12:47:09-04:00
draft: false
tags: [IPv6, Proxy, ASN]
---

## 写在前面

感谢 [zu1k](https://github.com/zu1k) 在两年前就已经踩好了坑，因此在我配置的过程中相对比较顺利。本文是基于 [https://zu1k.com/posts/tutorials/http-proxy-ipv6-pool/](https://zu1k.com/posts/tutorials/http-proxy-ipv6-pool/) 的教程进行配置的，在此基础上广播自己的 IPv6 地址。

## BIRD 相关的配置

```conf
# /etc/bird/bird.conf
protocol static {
  ipv6;
  route 2a06:a005:1c40::/44 reject;
  route 2a06:a005:1c40::/64 via fe80::5cb0:94ff:fe8e:5f24%ens18;
}
```

当然你可以直接把 ` 2a06:a005:1c40::/64` 改成 `2a06:a005:1c40::/44` ，这样你就可以获得更多的 IPv6 地址，可用的 IPv6 数量为 `2^84` 个。

## 网卡配置

```
# /etc/network/interfaces
auto lo
iface lo inet loopback
iface lo inet6 static
    address 2a06:a005:1c40::/64
    up ip route add local 2a06:a005:1c40::/64 dev lo
```

这里有个很坑的地方，我一开始尝试将 /64 添加到 `lo` 上，但是发现似乎无法通过任何 IP 出站。后来查了一下，似乎必须是 /128。 于是我就干了一件很蠢的事情。我用 Python 写了一个脚本，把整个 /120 的所有 IPv6 地址手动添加到了 `lo` 上。

```
iface lo inet6 static
    address 2a06:a005:1c40::0/128
iface lo inet6 static
    address 2a06:a005:1c40::1/128
iface lo inet6 static
    address 2a06:a005:1c40::2/128
...
iface lo inet6 static
    address 2a06:a005:1c40::ffff/128
```

当然，这样的配置可以工作，但是显然我不可能将整个 /64 全部以这样的方式添加。在 [Reddit](https://www.reddit.com/r/ipv6/comments/dp88q0/so_what_is_best_practice_for_loopback_128_or_64/) 找到了答案。

```
ip route add local 2a06:a005:1c40::/64 dev lo
```

我仅需要执行以上命令添加路由即可。当然为了方便，在上面对 `/etc/network/interfaces` 的配置中，我添加了 `up` 命令在 `lo` 网卡启动时自动添加路由。

当我以为一切准确就绪的时候，似乎又遇到了麻烦，我尝试使用 

```
curl --interface 2406:a005:1c40::1 ipv6.ip.sb
```

访问外网，发现无论如何都无法访问。

```bash
sysctl net.ipv6.ip_nonlocal_bind=1
```

需要使用 `sysctl net.ipv6.ip_nonlocal_bind=1` 命令来允许非本地绑定。为了让它永久生效，需要修改 `/etc/sysctl.conf` 文件。

```bash
nano /etc/sysctl.conf
net.ipv6.ip_nonlocal_bind=1
```

然后执行 `sysctl -p` 命令使配置生效。

完成以上步骤之后，使用 `curl --interface 2a06:a005:1c40::1 ipv6.ip.sb` 测试是否能够访问外网。

## 创建 HTTP 代理池

我用到的是 [zu1k](https://github.com/zu1k) 的 [zu1k/http-proxy-ipv6-pool](https://github.com/zu1k/http-proxy-ipv6-pool) 。由于 zu1k 提供的是 DEMO，并没有编译，因此需要自己完成编译。

我自己配置了一下 Actions，编译了 `http-proxy-ipv6-pool` ，并把编译好的文件上传到了 [missuo/http-proxy-ipv6-pool/releases](https://github.com/missuo/http-proxy-ipv6-pool/releases) 。

请注意，如果你使用 [v1.0.0](https://github.com/missuo/http-proxy-ipv6-pool/releases/tag/v1.0.0) 版本，则是原版。如果你使用 [v1.0.1](https://github.com/missuo/http-proxy-ipv6-pool/releases/tag/v1.0.1) 版本，则是修改了部分代码，支持了 HTTP 代理的 Authentication 功能。你可以使用以下命令在启动时设置 `Username` 和 `Password` 。

```bash
./http-proxy-ipv6-pool -u your_username -p your_password -b 0.0.0.0:51080 -i 2a06:a005:1c40::/64
```

## 测试

测试你的 IPv6 代理池是否可以工作。

```bash
curl --proxy http://your_username:your_password@your_ip:51080 http://ipv6.ip.sb
```

顺利的话，你应该会得到以下结果。

![20240911V6b5br](https://r2.qwq.mx/blog/20240911V6b5br.png)

```json
{
  "ip": "2a06:a005:1c40::1",
  "city": "Toronto",
  "region": "Ontario",
  "country": "CA",
  "loc": "43.7064,-79.3986",
  "org": "AS206729 Vincent Yang",
  "postal": "M5A",
  "timezone": "America/Toronto",
  "readme": "https://ipinfo.io/missingauth"
}
```

![20240911iTO991](https://r2.qwq.mx/blog/20240911iTO991.png)

通过 [IPInfo](https://ipinfo.io/2a06:a005:1c40::1) 可见，IP 完全是原生的，来自加拿大多伦多。

```json
{
    "ip":"2a06:a005:1c40::1",
    "score":"0",
    "risk":"low"
}
```

通过 [Scamalytics](https://scamalytics.com/ip/2a06%253Aa005%253A1c40%253A%253A1) 可见，IP 的风险分数为 `0` ，风险等级为 `low` 。

## 说明

- 由于我使用的是自己广播的 IPv6 地址，因此无需进行 ndppd 相关的配置。