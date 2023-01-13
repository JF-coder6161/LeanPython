# 迭代器
"""
迭代器：能被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator,迭代器是对象)
概念：
    迭代器指的是迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的，
    单纯的重复不是迭代
特征：
    并不依赖索引，而通过next指针(内存地址寻址)迭代所有数据,一次只取一个值
    而不是一股脑的把所有数据放进内存，大大节省空间
"""

# 1 可迭代对象
setvar = {"Jack", "Alice", "Linux"}
for i in setvar:
    print(i)

lst = dir(setvar)
print(lst)

# '__iter__' 具有可迭代性

res = '__iter__' in lst
print(res)  # True

# 2 迭代器
"""
for 循环在遍历数据的时候，要先把可迭代性数据变成迭代器，通过地址寻址的方式，获取每一个数据，不
依赖索引
如果是迭代器，一定是可迭代对象
如果是可迭代对象，不一定是迭代器
可迭代对象 =》 迭代器 是从数据不能直接被调用，到数据可被直接调用的过程 [有序无序的数据都可以迭代]
"""

# 1.如何定义迭代器
it = iter(setvar)
# 2 如何判断迭代器
lst = dir(it)
print(lst)  # __iter__ __next__
res = "__iter__" in lst and "__next__" in lst
print(res)  # True
# 3.如何遍历迭代器
# 特点：一次只取一个值，而且一条路走到黑不回头
# 方法一
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
# res = next(it)
# print(res) # StopIteration

# 方法二
print("-----------------------------")
for i in it:
    print(i)  # 方法一已经迭代过  导致 方法二取不到数据

# 4 如何重置迭代器
it = iter(setvar)
for i in it:
    print(i)

# 判断迭代器
from collections import Iterable, Iterator

# Iterator 迭代器
# Iterable 可迭代对象

res = isinstance(setvar, Iterable)
print(res)
res = isinstance(it,Iterator)
print(res)

# 小练习
r = range(10)
res = isinstance(r, Iterable)
print(res)
res = isinstance(r,Iterator)
print(res)

lst = iter(r)
# 获取迭代器中的数据 方法一：