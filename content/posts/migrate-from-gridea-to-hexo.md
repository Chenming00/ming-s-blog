---
title: Migrate from Gridea to Hexo
date: 2023-01-05 04:47:07
tags: [Gridea, Hexo]
---

> 由于 Gridea 的作者几乎已经放弃了 `Gridea客户端` 的更新和维护，直到现在还没有支持 Apple ARM。作者主要把重心放在了收费的网页版上。恰好我在 Gridea 上使用的主题，也有移植到 Hexo 上，于是就决定迁移。

## 迁移过程
### 部署新博客样式
因为是同一个主题，我用的是 [Pure](https://github.com/renbaoshuo/hexo-theme-pure)，之前改过一遍这个主题，所以现在第二次改还是比较熟悉的。主要是去除掉一些本身我觉得不需要的功能，把显示语言改成英文，最后再加上一些我比较喜欢的内容。总共耗时了 1-2 小时。Hexo 的好处也相当明显，之后写博客，只需要使用像 Obsidian、VSCode 或者 MWeb 这类 Markdown 编辑器即可，非常方便，不需要依赖特定的博客系统客户端。除此之外，Hexo 会生成纯静态的文件，可以部署到 GitHub Pages 上，或者你可以直接上传到网站的目录。


### 迁移文章
复制所有的 `.md` 文件放入新博客的 `_posts` 下即可。唯一需要变动的，可能是 `Post` 的几个属性。

### 评论系统
老的博客，Gridea 使用的是 `Disqus`，虽然 Hexo 也一样支持，但是似乎 `Disqus` 在中国大陆会出现加载失败的情况，所以这次索性放弃了之前的所有评论，采用了 GitHub 的 `Gitalk`。对于开发者来说，体验还是非常棒的。