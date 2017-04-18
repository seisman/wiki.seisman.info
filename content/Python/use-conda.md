---
title: conda 用法
---

## 虚拟环境

创建虚拟环境:

    conda create --name myenvname

激活虚拟环境:

    source activate snowflakes

退出虚拟环境:

    source deactivate

创建其他版本的虚拟环境:

    conda create --name bunnies python=3 astroid babel

列出所有虚拟环境:

    conda info --envs

删除虚拟环境:

    conda remove --name xxx --all
    conda env remove --name xxxx

https://conda.io/docs/test-drive.html
