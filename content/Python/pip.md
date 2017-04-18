---
title: pip
---

升级所有已安装的模块:

    pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

