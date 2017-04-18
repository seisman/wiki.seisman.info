---
title: 管理/同步配置文件
---

Linux/macOS 下各种软件都有自己的配置文件，通常是以 `.` 开头的隐藏文件，比如
`~/.zshrc`、`~/.vimrc` 等。这些文件统称为 dotfiles。

为了备份/同步这些配置文件，最简单的思路是将这些 dotfiles 移动到某个特定的目录，
然后制作指向原位置的软链接。但这些软链接管理起来却很麻烦。

[mackup](https://github.com/lra/mackup) 是专门用于管理/备份/同步 dotfiles 的工具。

## 安装

macOS 安装 mackup:

    brew install mackup

Linux 安装 mackup:

    pip install mackup

mackup v0.8.16 在Python3下似乎有bug，将 `site-packages/mackup/config.py` 的第225行:

    path = path.decode("utf-8")

修改为:

    path = str(path)

可以解决此问题。

## 用法

    mackup -h         显示用法
    mackup list       列出 mackup 官方支持的软件
    mackup backup     备份
    mackup restore    在新机器上恢复
    mackup uninstall  取消 mackup 的备份

## 备份原理

1. 读取配置文件 `~/.mackup.cfg`，确认哪些文件需要备份，以及要备份到哪些地方
2. 将需要备份的文件移动到备份目录下
3. 生成软链接

## 配置

### 全局配置文件

全局配置文件为 `~/.mackup.cfg`:

    #
    # mackup 配置文件
    #

    # 备份目的地
    [storage]
    # engine 可以取 dropbox|google_drive|icloud|copy|file_system
    # 设置为 file_system 表示将文件备份到某个指定目录下
    engine = file_system
    # 备份目录为 ~/Nutstore/dotfiles
    path = Nutstore
    directory = dotfiles

    # 只同步指定软件的配置文件
    [applications_to_sync]
    git          # 官方支持的软件
    mackup       # 自定义的软件，见下一节

    # 不同步指定软件的配置文件
    [applications_to_ignore]

    # 指定备份特定的文件(似乎无效)
    [configuration_files]

### 自定义配置文件

mackup 官方支持备份300多种软件的配置文件，但并不能满足需求，因而需要能够自定义。

所有自定义软件备份的配置文件都保存在 `~/.mackup` 目录下:

    mkdir ~/.mackup
    cd ~/.mackup

创建 `mackup.cfg` 文件，内容为:

    [application]
    name = Mackup

    [configuration_files]
    .mackup.cfg
    .mackup

然后将 `mackup` 加入到 `~/.mackup.cfg` 的 `applications_to_sync` 中，即可实现 mackup 配置自身的备份。

## mackup 官方支持软件列表

<https://github.com/lra/mackup/tree/master/mackup/applications>
