---
title: conda 用法
---

## 更新

更新conda:

    conda update conda

更新 anaconda:

    conda update anaconda

更新所有已安装模块:

    conda update --all

## 虚拟环境

创建虚拟环境:

    conda create --name envname
    conda create --name envname python=3.6 astroid babel

激活虚拟环境:

    source activate snowflakes

退出虚拟环境:

    source deactivate

列出所有虚拟环境:

    conda info --envs

删除虚拟环境:

    conda env remove --name xxxx

https://conda.io/docs/test-drive.html
