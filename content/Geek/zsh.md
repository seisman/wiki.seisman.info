---
title: zsh
---

## 安装 zsh

    yum install zsh

## 安装 oh-my-zsh

安装方式见 [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)

## zsh 插件

- 插件列表（按字母排序） https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins
- 插件列表（按分类排序） https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins-Overview
- 外部插件： https://github.com/robbyrussell/oh-my-zsh/wiki/External-plugins

刚安装完成的 oh-my-zsh 启动时间大概时0.1秒，使用过多的插件会大大增加启动时间。
可以使用如下命令测试 zsh 的启动速度:

    for i in $(seq 1 10); do /usr/bin/time zsh -i -c exit; done

在 `~/.zshrc` 的 `plugins=()` 中加入要启用的插件名即可启用相应插件，比如:

    plugins=(extract pip)

下面列举出非常有用且不影响zsh启动速度的插件。

### autojump

其实跟 zsh 没啥关系，autojump 实现了目录快速跳转。autojump 提供了命令 `j`

跳转到目录名包含 `foo` 的文件夹:

    j foo

打开某个文件夹:

    jo music

### extract

用一个命令解压几乎所有压缩格式:

    x ABC.zip
    x ABC.tar.gz
    x ABC.tgz
    ...

### pip

该插件提供了pip自动补全功能和几个辅助函数:

- `zsh-pip-cache-packages`
- `zsh-pip-clear-cache`
- `zsh-pip-clean-packages`

用法：

1. 启用该插件
2. 终端执行 `zsh-pip-cache-packages` ，等待缓存完成，约需要两分钟
3. 开始使用

   - `pip <TAB>` 会自动补全 pip 所支持的命令
   - `pip install Hi<TAB>` 会自动补全以 `Hi` 开头的 Python 模块

### colored-man-pages

为 man page 加上颜色，更加易于查看 man page。

### sudo

按下两次 Esc 键则自动在命令开头加上 `sudo`

### 一些命令补全插件

除了上面提到的插件之后，还有一些可以加入的补全插件：

- `autopep8`
- `git-extras`

## zsh 主题

- 自带主题： https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
- 外部主题： https://github.com/robbyrussell/oh-my-zsh/wiki/External-themes

## 相关资源

- awesome-zsh-plugins: https://github.com/unixorn/awesome-zsh-plugins
- oh-my-zsh cheatsheet: https://github.com/robbyrussell/oh-my-zsh/wiki/Cheatsheet
