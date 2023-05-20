---
title: "Automatically update Homebrew versions using Action"
date: 2023-03-04T02:42:51+08:00
draft: false
tags: [Homebrew, Casks, Formula]
---

Homebrew 可以说是 Mac 上必装的命令行工具之一。它真的太好用太方便的。但是你在维护一个 Homebrew Tap 的时候，如果你的程序有新的 Release 发布时，需要在对应的 `.rb` 文件中修改版本号以及对应的二进制文件的 sha256，这显然会有些繁琐，或者说不太优雅。

我习惯使用 GitHub Action 去交叉编译各种 Release，重要的是 Action 可以帮助我自动发布。其实在每一次 Action 发布之后，可以添加一个 Step，去更新 Casks 或者 Formula 的 `.rb`。为了方便，你可以创建一个 `.sh` 文件来做这件事。

## 部分代码（以 DeepL X 为例）
#### 更新版本号
```bash
Get the latest version of Deeplx
last_version=$(curl -Ls "https://api.github.com/repos/OwO-Network/DeepLX/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/' | sed 's/v//g')

# Update the version number in the formula
sed -i "s/version \".*/version \"${last_version}\"/g" Formula/deeplx.rb
```

#### 更新 sha256
```bash
 # Download the new binaries
wget -O deeplx_darwin_amd64 https://github.com/OwO-Network/DeepLX/releases/download/v${last_version}/deeplx_darwin_amd64
wget -O deeplx_darwin_arm64 https://github.com/OwO-Network/DeepLX/releases/download/v${last_version}/deeplx_darwin_arm64

# Calculate the SHA256 hash for the new binaries
amd64_sha256=$(sha256sum deeplx_darwin_amd64 | cut -d ' ' -f 1)
arm64_sha256=$(sha256sum deeplx_darwin_arm64 | cut -d ' ' -f 1)

# Update the SHA256 hashes in the formula
sed -i "8s/.*/    sha256 \"${arm64_sha256}\"/" Formula/deeplx.rb
sed -i "11s/.*/    sha256 \"${amd64_sha256}\"/" Formula/deeplx.rb

# Delete the new binaries
rm -f deeplx_darwin*
```

在Action发布到Release之后，触发这个shell文件就可以啦。这样的话，当你有新的Release发布的时候，无需去维护Homebrew Tap。用户可以直接获取到最新的版本。

