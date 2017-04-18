---
title: Python的安装与使用
---

## 安装 anaconda

1.  下载:  <https://www.continuum.io/downloads>
2.  安装:

        $ bash ./Anaconda3-4.3.1-Linux-x86_64.sh

3.  重启终端

## 修改镜像源以加速

### anaconda 镜像

添加清华 Anaconda 源以加快模块的下载速度

    $ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    $ conda config --set show_channel_urls yes

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

## 安装模块

可以通过 conda 进行安装的模块列表： <https://docs.continuum.io/anaconda/pkg-docs>

优先使用 conda 安装模块:

    conda install numpy

若 conda 找不到则使用 pip 安装模块:

    pip install numpy

pip 支持从 github 上直接安装最新版源码:

    pip install git+https://github.com/seisman/HinetPy.git

若 pip 找不到，则下载源码，手动编译:

    python setup.py install
