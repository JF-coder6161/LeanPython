# ### 字典推导式
### 1 enumerate
"""
enumerate(iterable,[start=0])
功能：枚举； 将索引号和iterable中的值，一个一个拿出来配对组成元组放入迭代器中
参数：
    iterable：可迭代性数据 （常用：迭代器，容器类型数据，可迭代对象range）
    start：可以选择开始的索引号(默认从0开始索引)
返回值：迭代器
"""
from collections.abc import Iterator

lst = ["铁拐李", "何仙姑", "蓝采和", "潘多拉"]
it = enumerate(lst, start=1)
print(isinstance(it, Iterator))  # True
for k, v in it:
    print(k, v)

# 借助enumerate转化推导式
dic = {k: v for k, v in enumerate(lst)}
print(dic, type(dic))

# 直接dict 强转
dic = dict(enumerate(lst))  # ?? 疑问为什么枚举可以当作入参
print(dic)

