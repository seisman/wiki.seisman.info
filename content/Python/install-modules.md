---
title: 安装模块
weight: 2
---

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

## 升级模块

升级conda安装的模块:

    conda update --all
