---
title: 'Remove National Anti-Fraud Center on MIUI'
date: 2023-02-04 00:01:04
tags: [MIUI, Anti-Fraud]
---

## Uninstall Directly(Recommended)
> ROOT is not required, but it may be reinstalled after updating the system.
1. Connect your phone to your computer and turn on `ADB` debugging.

2. Install `ADB` CLI tools on your computer.
```
# macOS
brew install android-platform-tools
or
https://dl.google.com/android/repository/platform-tools-latest-darwin.zip

# Windows
https://dl.google.com/android/repository/platform-tools-latest-windows.zip
```
3. Execute the following code.
```
adb shell pm list package | grep com.miui.guardprovider
adb uninstall --user 0 com.miui.guardprovider
adb shell pm list users

# if you find other users on your phone, please execute the following command.
adb uninstall --user [USERID] com.miui.guardprovider
```
![20230204UJZpcM](https://static.nisekoo.com/blog/20230204UJZpcM.png)

## Install Magisk Module
> ROOT is required, but updating the system works just as well.

[MinaMichita/AntiAntiDefraud/](https://github.com/MinaMichita/AntiAntiDefraud/)