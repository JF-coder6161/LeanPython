# sorted
"""
sorted (iterable,reverse=False,key=函数)
功能：对数据进行排序
参数：
    iterable：   具有可迭代性的数据（迭代器，容器类型数据，可迭代对象）
    reverse：    是否反转 默认为False 代表正序，改成True 为倒序
    key:    指定函数，内置或自定义函数
返回值：
    返回排序后的数据
"""
lst = [-100, 24, 99, 21]
print(sorted(lst))
print(sorted(lst, reverse=True))

# 对于sorted来说，所有的Iterable种类的数据都能排序
# 集合
setvar = {90, -100, 78, 222}
res = sorted(setvar)
print(res)  # [-100, 78, 90, 222]
print(type(res))
# 字典 （默认排序的是键）
dic = {"a": 1, "b": 3, "c": 2}
res = sorted(dic)
print(res)  # ['a', 'b', 'c']
print(type(res))
# 元组
tup = (3, 2, 4, 6, 1)
res = sorted(tup)
print(res)

"""
sort:   针对列表(针对的是原列表进行排序，没有返回值)
sorted: 针对任意可迭代的数据类型（返回排序后的结果，类型为列表）
"""

# 按照内置方法排序 eg:abs
lst = [-1, -4, 3, 2]
res = sorted(lst, key=abs)
print(res)  # [-1, 2, 3, -4]

# 按照余数的大小排序
lst = [19, 22, 34, 63]


def func(i):
    return i % 10

res = sorted(lst, key=func)
print(res)
