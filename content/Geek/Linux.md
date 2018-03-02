---
title: Linux 笔记
---

## 有用的命令

递归删除当前目录下的空文件夹:

    find . -type d -empty -delete

删除当前目录下大小为零的文件:

    find . -size 0 -delete

同步但不删除:

    rsync -av 2012* user@hostip:/data --progressr

将中文编码修改为UTF-8编码:

    enca -L zh_CN -x UTF-8 infile

将文件内容复制到剪贴板:

    xclip -sel clip < xxx.txt

开机自动启动 ssh 服务:

    chkconfig sshd on

查看一个二进制文件在执行时加载了哪些动态库:

    ldd /bin/ls

## Linux 学习资源

1. [Linux 工具快速教程](http://linuxtools-rst.readthedocs.io/zh_CN/latest/)

## Linux 相关资源

1. [Ubuntu 软件包查询](http://packages.ubuntu.com/)
2. [Linux 软件包查询](https://pkgs.org/)

## Linux下的效率工具

1. [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
2. [auto-jump](https://github.com/wting/autojump)
3. [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
4. [ack](https://beyondgrep.com/)
