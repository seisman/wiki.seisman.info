---
title: 网络相关
---

从 pypi 获取模块的版本号:

```python
>>> import requests
>>> r = requests.get("https://pypi.python.org/pypi/HinetPy/json")
>>> r.json()['info']['version']
'0.3.3'
```
