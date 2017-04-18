---
title: Python标准库
---

## csv

假如CSV文件内容如下:

    #EventID | Time | Latitude | Longitude | Depth/km | Author | Catalog | Contributor | ContributorID | MagType | Magnitude | MagAuthor | EventLocationName
    9993759|2017-01-22T04:30:22|-6.2145|155.1442|135.0|pt,us,at|NEIC PDE|us|us10007uph,pt17022050,at00ok5z6p|mww|7.9|us|SOLOMON ISLANDS
    9993037|2017-01-19T23:04:21|-10.3433|161.318|36.0|pt,us,at|NEIC PDE|us|us10007u7n,at00ok1ura,pt17019050|mww|6.5|us|SOLOMON ISLANDS
    9953968|2017-01-10T06:13:47|4.4634|122.575|612.71|at,us|NEIC PDE|us|us10007s9c,at00ojjvz0|Mww|7.3|us|CELEBES SEA
    9951821|2017-01-03T21:52:30|-19.3542|176.058|12.0|at,us,pt|NEIC PDE|us|us10007pj6,at00oj84rf,pt17003051|Mww|6.9|us|SOUTH OF FIJI ISLANDS

可以用 ``csv.DictReader`` 读入该文件，但需要对key做特殊处理:

```python
with open("events.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    reader.fieldnames = [field.strip() for field in reader.fieldnames]
    for row in reader:
        print(row['Time'])
```


## multiprocessing

### Pool.starmap

`Pool.starmap` 用于在多进程中传入多个参数

```python
from multiprocessing import Pool

def func2run(c1, c2, v1, c3, v4):
    print(c1, c2, v1, c3, v4)

pool = Pool(processes=4)
c1, c2, c3, c4 = 1, 2, 3, 4
args = [(c1, c2, v, c3, c4) for v in range(1, 10)]
pool.starmap(func2run, args)
```

输出结果为

    1 2 1 3 4
    1 2 2 3 4
    1 2 3 3 4
    1 2 5 3 4
    1 2 4 3 4
    1 2 7 3 4
    1 2 6 3 4
    1 2 8 3 4
    1 2 9 3 4

注意， ``starmap`` 的返回值是顺序的。

### dummy & pool.ThreadPool

这两个模块可以用于执行多线程程序：

``` python
from  multiprocessing.dummy import Pool

with Pool(4) as p:
    p.map(f, args)
```

``` python
from  multiprocessing.pool import ThreadPool

with ThreadPool(4) as p:
    p.map(f, args)
```
