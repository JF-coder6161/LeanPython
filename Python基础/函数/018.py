# ### pickle 序列化模块
"""
序列化: 把不能够直接存储的数据变成可存储的数据
反序列化: 把数据拿出来，恢复成原本的数据类型

pickle可以序列化所有的数据类型,可以变成字节流
"""

import pickle

lst = [1, 2, 3]

# dumps 把任意对象=序列化成一个bytes
res = pickle.dumps(lst)
print(res, type(res))  # <class 'bytes'>

# 把字节流存储到文件中
with open("seril.txt", mode="wb") as fp:
    fp.write(res)

# loads 把任意bytes反序列化成原来的数据
lst = pickle.loads(res)
print(lst)

# 提取文件中字节流，通过loads反序列化恢复原来数据类型
with open("seril.txt", mode='rb') as file1:
    b = file1.read()
    print(b)
    res = pickle.loads(b)
    print(res, type(res))

def func():
    print("123")


b = pickle.dumps(func)
print(b, type(b))  # <class 'list'>

res = pickle.loads(b)
print(res,
      type(res))  # <function func at 0x000001FC6497F040> <class 'function'>
res()

# 序列化，反序列化 迭代器
from collections.abc import Iterable, Iterator

it = iter(range(10))
print(next(it))  # 取一次数据 # 0
res = pickle.dumps(it)
it2 = pickle.loads(res)
print(next(it2))  # 1

# dump 把对象序列化后写入到file-like object (即文件对象)
lst = [1, 2]
with open("seril1.txt", mode="wb") as fp:
    # 把1st 直接写入到fp文件对象中
    pickle.dump(lst, fp)

# load 把file-like object(即文件对象)中的内容 反序列化成为原来数据
with open('seril1.txt', 'rb') as fp:
    # 直接从fp文件中获取数据 (获取数据 -》 反序列化)
    res = pickle.load(fp)
    print(res,type(res))

