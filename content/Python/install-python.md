---
title: 安装Python
weight: 1
---

## 安装 anaconda

1.  下载: https://mirrors.ustc.edu.cn/anaconda/archive/Anaconda3-5.0.1-Linux-x86_64.sh
2.  安装:

        $ bash ./Anaconda3-5.0.1-Linux-x86_64.sh

3.  重启终端

## 修改镜像源以加速

### anaconda 镜像

添加中科大 Anaconda 源以加快模块的下载速度:

    $ conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
    $ conda config --set show_channel_urls yes

这两个命令会修改文件 `~/.condarc` 。

### 添加 pip 镜像

编辑 `~/.pip/pip.conf` 文件（如果没有则创建之），将 `index-url` 开头的一行修改为下面一行：

    [global]
    index-url = https://pypi.mirrors.ustc.edu.cn/simple

## 更新 anaconda 预安装的模块

```bash
conda update conda
conda update anaconda
conda update --all
```
