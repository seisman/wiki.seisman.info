---
title: Git 笔记
---

## 学习资源

1. [Pro Git 中文版](https://git-scm.com/book/zh/v2)

## 配置 Git

Git 配置文件为 `~/.gitconfig`。

### 首次配置

首次使用需要进行配置：

```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

### 其他配置

```
git config --global core.editor vim
git config --global merge.tool meld
```

## git 入门

初始化新仓库:

    git init

跟踪文件并提交:

    git add *.c
    git add README.md
    git ci -m 'initial version'

Clone已有仓库:

    git clone https://github.com/libgit2/libgit2 mylibgit
    git clone git@github.com:seisman/HinetPy.git

修改最后一次提交的信息:

    git commit --amend

向最后一次提交添加更多内容:

    git commit -m 'initial commit'
    git add forgotten_file
    git commit --amend

取消暂存的文件:

    git reset HEAD xxx.md

撤销对文件的修改:

    git checkout -- xxx.md

重命名本地分支:

    git branch -m <newname>
    git branch -m <oldname> <newname>

### 远程

推送到远程分支:

    git push origin master

查看远程仓库:

    git remote show origin

重命名远程仓库:

    git remote rename pb paul

删除远程仓库:

    git remote rm paul

### 标签

打标签:

    git tag 1.2.3

推送标签到远程:

    git push origin 1.2.3
    git push --tags

## git 高阶


1.  远程已删除分支，但在本地依然存在，欲清理之:

        git remote prune origin

2.  指定子模块追踪某个特定的分支

        # add submodule to track master branch
        git submodule add -b master [URL to Git repo]

        # update your submodule
        git submodule update --remote
