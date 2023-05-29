---
title: "Rime on Mac Tutorial"
date: 2023-05-29T19:57:54+08:00
draft: false
tags: [Rime, Squirrel]
---
> 之前有用过 Mac 原生输入法、搜狗输入法。原生输入法缺点就是词库太烂了，很多时候打出来的侯选词都不是我想要的。而搜狗输入法的词库是无可挑剔的，毕竟是联网的词库，但是会有一定的隐私安全。直到我在 Twitter 看到 [luolei](https://twitter.com/luoleiorg) 用上了 Rime。

我第一次接触 Rime 估计过去了快一年了，第一次配置简直是噩梦，因为 Rime 可以自定义的东西太多了，几乎你能想到的一切都可以自定义，这就导致了你要弄明白每一个设置的参数是干什么用的。配置完之后，使用的体验也不算太好，很多时候都出现不了我想要的侯选词，不过随着个人词库的训练，会变得越来越“智能”。老实说，放在以前我不会向你推荐 Rime，我相信很多朋友刚设置完没几天就换回 **搜狗** 了。直到 **[雾凇拼音](https://github.com/iDvel/rime-ice)** 的出现。**雾凇拼音** 的好处我就不多赘述了，直接来说说使用方法吧！

### 1. 安装 Rime (Squirrel)
```bash
brew install --cask squirrel
```

### 2. 安装 东风破 (plum)
```bash
cd ~/Library/Rime
git clone --depth=1 https://github.com/rime/plum
```

### 3. 安装 雾凇拼音
```bash
cd plum
bash rime-install iDvel/rime-ice:others/recipes/full
```
到这里安装部分基本上已经是完成了。你已经可以开始使用了。下面的部分是一些优化和高阶玩法的部分。

### 使用 微信输入法 Mac 的主题
修改 `squirrel.custom.yaml` 文件。
```yaml
# squirrel.custom.yaml
patch:
  # 通知栏显示方式以及 ascii_mode 应用，与外观无关
  show_notifications_via_notification_center: true

  # 以下软件默认英文模式
  app_options:
    com.svend.uPic:
      ascii_mode: true

# 如果想要修改皮肤，直接更改 color_scheme 的值即可
  style:
    color_scheme: wechat_light
    color_scheme_dark: wechat_dark

  preset_color_schemes:
    wechat_light:
      name: 微信键盘浅色
      horizontal: true                          # true横排，false竖排
      back_color: 0xFFFFFF                      # 候选条背景色
      border_height: 0                          # 窗口上下高度，大于圆角半径才生效
      border_width: 8                           # 窗口左右宽度，大于圆角半径才生效
      candidate_format: '%c %@ '                # 用 1/6 em 空格 U+2005 来控制编号 %c 和候选词 %@ 前后的空间
      comment_text_color: 0x999999              # 拼音等提示文字颜色
      corner_radius: 5                          # 窗口圆角
      hilited_corner_radius: 5                  # 高亮圆角
      font_face: PingFangSC                     # 候选词字体
      font_point: 16                            # 候选字大小
      hilited_candidate_back_color: 0x75B100    # 第一候选项背景色
      hilited_candidate_text_color: 0xFFFFFF    # 第一候选项文字颜色
      label_font_point: 12                      # 候选编号大小
      text_color: 0x424242                      # 拼音行文字颜色
      inline_preedit: true                      # 拼音位于： 候选框 false | 行内 true
    wechat_dark:
      name: 微信键盘深色
      horizontal: true                          # true横排，false竖排
      back_color: 0x2e2925                      # 候选条背景色
      border_height: 0                          # 窗口上下高度，大于圆角半径才生效
      border_width: 8                           # 窗口左右宽度，大于圆角半径才生效
      candidate_format: '%c %@ '                # 用 1/6 em 空格 U+2005 来控制编号 %c 和候选词 %@ 前后的空间
      comment_text_color: 0x999999              # 拼音等提示文字颜色
      corner_radius: 5                          # 窗口圆角
      hilited_corner_radius: 5                  # 高亮圆角
      font_face: PingFangSC                     # 候选词字体
      font_point: 16                            # 候选字大小
      hilited_candidate_back_color: 0x75B100    # 第一候选项背景色
      hilited_candidate_text_color: 0xFFFFFF    # 第一候选项文字颜色
      label_font_point: 12                      # 候选编号大小
      text_color: 0x424242                      # 拼音行文字颜色
      label_color: 0x999999                     # 预选栏编号颜色
      candidate_text_color: 0xe9e9ea            # 预选项文字颜色
      inline_preedit: true                      # 拼音位于： 候选框 false | 行内 true
```

### 更新和同步词库
我这边采用的备份方案是 **Dropbox**，别的也都类似，可以实现多台设备之间词库互相同步。修改 `installation.yaml` 文件。
```yaml
# installation.yaml
distribution_code_name: Squirrel
distribution_name: "鼠鬚管"
distribution_version: 0.16.2
install_time: "Mon May  8 15:13:26 2023"
installation_id: "mac-mini"
sync_dir: "/Users/vincent/Library/CloudStorage/Dropbox/Rime/"
rime_version: 1.8.5
```
更新词库脚本，你可以配置 Mac 计划任务，每天或者每隔几个小时自动执行。
```bash
#!/bin/bash
cd ~/Library/Rime/plum

echo "Updating rime..."
bash rime-install iDvel/rime-ice:others/recipes/full

sleep 3

echo "Syncing rime..."
/Library/Input\ Methods/Squirrel.app/Contents/MacOS/Squirrel --sync

echo "Deploying rime..."
/Library/Input\ Methods/Squirrel.app/Contents/MacOS/Squirrel --reload
```

别的一些非常具体的设置，我在这里就不介绍了，[雾凇拼音官方介绍](https://dvel.me/posts/rime-ice/) 写的非常详细，可以仔细阅读。
