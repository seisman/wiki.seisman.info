---
title: obspy
---

## 安装obspy

    $ conda config --add channels conda-forge
    $ conda create --name py3
    $ source activate py3
    $ conda install obspy
    $ conda update obspy

仅读取一部分SAC文件，实现类似 SAC 中 cut 命令的功能：

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from obspy import read
from obspy.io.sac.util import get_sac_reftime

st = Stream()
for file in sorted(glob.glob("*.SAC")):
    tr = read(file)[0]
    reftime = get_sac_reftime(tr.stats.sac)

    starttime = reftime + tr.stats.sac.t0 - 10
    endtime = reftime + tr.stats.sac.t0 + 10

    st += tr.slice(starttime, endtime)
```
