# ### filter 数据过滤

"""
filter(func,iterable)
功能：
    用来过滤的，如果func函数中返回True，会将这个值保留到迭代器中，
    如果func函数中返回False，则将丢弃此值
参数：
    func：自定义函数
    iterable:具有可迭代性的数据(迭代器，容器类型数据，可迭代对象)
返回值：
    返回处理后的迭代器
"""

lst = [1, 4, 3, 2, 5,6]
def func(i):
    return i % 2 == 0
it = filter(func, lst)
res = list(it)
print(res)

