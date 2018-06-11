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

根据 doi 获取 bibtex 或 json:
``` python
#!/usr/bin/env python
# source: https://gist.github.com/jrsmith3/5513926

import requests
url = "https://doi.org/10.1038/nature07109"

headers = {"accept": "application/x-bibtex"}
r = requests.get(url, headers=headers)
print(r.text)

headers = {"accept": "application/json"}
r = requests.get(url, headers=headers)
print(r.json())
```
