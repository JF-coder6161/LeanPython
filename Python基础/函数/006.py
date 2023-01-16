# ### 高阶函数 ： 参数是函数 map reduce sorted filter
# map
"""
map(func,iterable)
功能：
    把iterable里面所有数据 一一的放进到func这个函数中进行操作，通过迭代器来获取数据
参数：
    func    内置或自定义函数
    iterable 具有可迭代性的数据 ([迭代器],[容器类型的数据]，[range对象])
返回值：
    返回最后的迭代器
"""
from collections.abc import Iterable,Iterator
# lst = ["1","2","3","4","5","6"] => [1,2,3,4]
# 常规方法
lst = ["1","2","3","4","5","6"]
tmp_lst = []
for i in range(4):
    print(i)
    tmp_lst.append(int(lst[i]))
print(tmp_lst)

it = map(int,lst)
print(isinstance(it,Iterator))
for i in it:
    print(i)

# map 改写
lst = ["1","2","3"]
def func(i):
    print("迭代器触发~~~")
    res = int(i)
    return res * 4
it = map(func,lst)
print("<===============>")
for i in range(3):
    # 只有在调用迭代器的时候，才会执行map中func这个代码，否则不执行
    print(next(it))

# list 列表强转方法，全部一次性获取到
lst = list(it)
print(lst)

# 三. {97:'a',98:'b',99:'c'} => [97,98,99]
dic = {97:'a',98:'b',99:'c'}
# 翻转字典
tmp_dic = {}
for key,value in dic.items():
    tmp_dic[value] = key
print(tmp_dic)

lst = ['a','b','c']
lst_new = []
for i in lst:
    lst_new.append(tmp_dic[i])
print(lst_new)

# 改写 map
def func(it):
    dic = {97: 'a', 98: 'b', 99: 'c'}
    for key, value in dic.items():
        tmp_dic[value] = key
    return tmp_dic
it = map(func,lst)
res = list(it)






