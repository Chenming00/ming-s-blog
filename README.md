# 🚀 Ming's Blog

Welcome to Ming's personal blog. This site is built with [Hugo](https://gohugo.io/) and uses the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme. It is designed to be fast, minimalist, and responsive.

- **URL**: [https://blog.ming.fi](https://blog.ming.fi)
- **Framework**: Hugo (Extended)
- **Theme**: PaperMod

---

## 🛠 本地开发 (Local Development)

如果你想在本地预览博客或进行调试，请按照以下步骤操作：

### 1. 前置条件
- 安装 **Hugo (Extended version)**。
- 确保你的电脑已配置 **Git**。

### 2. 克隆项目
```bash
git clone --recursive https://github.com/Chenming00/ming-s-blog.git
cd ming-s-blog
```
*注意：由于使用了主题子模块，请务必带上 `--recursive` 参数。*

### 3. 运行本地服务器
在 VS Code 终端中运行：
```bash
hugo server -D
```
访问 `http://localhost:1313` 即可实时预览。`-D` 参数表示同时预览草稿（Drafts）。

---

## 📝 文章发布教程 (Publishing Tutorial)

本博客推荐使用 **VS Code + Cline (AI 助手)** 的高效协作模式。

### 第一步：创建新文章 🤖
你可以直接向 **Cline** 发送指令：
> "帮我创建一篇关于 [文章标题] 的新文章，标签包含 [标签1, 标签2]，内容是 [简要说明]。"

**Cline 会自动完成：**
1. 在 `content/posts/` 目录下创建对应的 `.md` 文件。
2. 自动生成 YAML 元数据（Frontmatter），如标题、日期和标签。

### 第二步：编辑内容 ✍️
在 VS Code 中打开新建的文件，编辑 Markdown 内容。
- **常用 Frontmatter 控制：**
  - `title`: 文章标题
  - `date`: 发布日期（自动生成，通常不需改动）
  - `tags`: 标签数组，例如 `[AI, Tools]`
  - `draft`: **重要！** 开发时设为 `true`，准备发布时改为 `false`。

### 第三步：本地预览 👁️
1. 打开 VS Code 终端。
2. 运行 `hugo server -D`。
3. 在浏览器查看效果。

### 第四步：同步到 GitHub (发布) 🚀
1. 确认文章的 `draft` 字段已设为 `false`。
2. 使用 VS Code 左侧的 **Source Control (源代码管理)** 面板：
   - **Stage** 你的改动。
   - 输入 **Commit Message** (例如: "feat: add new post about Yudan")。
   - 点击 **Sync Changes** (或者 `git push`)。

**部署自动化：**
一旦代码推送到 GitHub 的 `master` 分钟，GitHub Actions 会自动触发构建并部署到 `blog.ming.fi`。通常需要 1-2 分钟生效。

---

## 📂 目录结构
- `content/posts/`: 所有的博客文章。
- `content/about/`: “关于”页面。
- `static/`: 静态资源（图片、favicon、CNAME）。
- `themes/`: Hugo 主题。
- `config.yml`: 站点全局配置文件。

---

## 📬 联系我
- **GitHub**: [chenming00](https://github.com/chenming00)
- **Twitter**: [@Will_cm](https://twitter.com/Will_cm)
- **Email**: i@ming.fi
