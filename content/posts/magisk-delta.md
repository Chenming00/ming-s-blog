---
title: "Switch from Magisk to Magisk Delta"
date: 2023-07-12T19:49:05+08:00
draft: false
tags: [Magisk, Magisk Delta, ROOT, Android]
---

## Magisk
**Magisk** 是目前常用的 Android ROOT 工具，总体来说没什么太大的问题。但是部分 App 会检测到 ROOT 之后无法正常运行，常见的是一些银行类 App，例如云闪付等。除此之外，例如微信、支付宝这类 App 的指纹支付无法开启，麦当劳中国 App 闪退。

目前的解决方案就是使用 [Shamiko](https://github.com/LSPosed/LSPosed.github.io/releases) 来隐藏 ROOT。

## Magisk Delta
**Magisk Delta** 就是为了解决这个问题，可以完全地隐藏 ROOT。

## 如何升级
1. 安装 Magisk Delta App，修补 **boot.img**。
[Download APK](https://cdn.jsdelivr.net/gh/huskydg/magisk-files@301b1865c7d47bbed1e375541987aee0cd1b753d/app-release.apk)

2. 使用 **Fastboot** 刷入修补之后的 **boot.img**。
```shell
fastboot flash boot_a boot_patched.img
fastboot flash boot_b boot_patched.img
fastboot reboot
```

3. 开机之后，卸载 **Magisk App**，打开新的 **Magisk Delta App**，开启 **MagiskHide** 和 **Enforce SuList**。（注意开机之后不需要重新导入模块，理论上会自动识别之前安装的所有模块，包括**LSP**）
![20230712ZBVeDI](https://static.nisekoo.com/blog/20230712ZBVeDI.jpg)

![20230712xkDIyI](https://static.nisekoo.com/blog/20230712xkDIyI.jpg)