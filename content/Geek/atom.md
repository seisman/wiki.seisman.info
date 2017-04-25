---
title: atom 编辑器
---

atom 是 GitHub 官方推出的编辑器，具有开向即用、可扩展性强等特点。唯一的
缺点是启动速度偏慢，解决办法是长期打开一个编辑器窗口不关闭。

- 主页： https://atom.io/
- 插件： https://atom.io/packages
- 主题： https://atom.io/themes
- 文档： http://flight-manual.atom.io/

## 安装

1.  下载 https://atom.io/download/rpm
2.  安装:

        yum localinstall atom.x86_64.rpm

## 基础操作

命令|说明
---|---
`Ctrl+Shift+P` | 打开命令面板
`Ctrl+,` | 打开设置面板，由 `settings-view` 提供
`Ctrl+\` | 打开Tree view
`Alt+\` | focus在tree view
`Ctrl+W` | 关闭当前标签页
`Ctrl+O` | 打开文件
`Ctrl+S` | 保存文件
`Ctrl+Shift+S` | 另存为
`Ctrl+Alt+S` | 保存所有文件

## 插件列表

名称 | 说明
---|---
`sync-settings` | 用于同步/备份 atom 配置文件
`seti-icons` | 好看的文件图标
`pdf-view` | 在 atom 中预览 PDF
`atom-beautify`i | 代码格式化工具

### markdown

1. 禁用 atom 内置插件 `markdown-preview`
2. 安装 [markdown-preview-enhanced](https://github.com/shd101wyy/markdown-preview-enhanced)
