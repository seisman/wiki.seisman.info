---
title: Hugo
---

[Hugo](https://gohugo.io)，是目前我看到的最好的静态网站生成器。

优点：

1.  安装简单，只需要下载一个单独的二进制文件即可，完全没有任何依赖
2.  面向任何类型的网站，不局限于博客

## 安装

[直接下载](https://github.com/spf13/hugo/releases)

唯一的外部依赖（可选）：

    pip install Pygments

## 命令

常用命令:

    hugo
    hugo help
    hugo list
    hugo server
    hugo undraft

`hugo new`:

    hugo new site <SITENAME>
    hugo new theme <THEMENAME>
    hugo new <SECTIONNAME>/<FILENAME>.<FORMAT>


## 使用

1.  `.IsNode` 所有的 list 都是 Node
2.  `.IsPage` 所有由文件生成的页面都是 Page
