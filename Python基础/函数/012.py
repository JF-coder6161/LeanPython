# ### Zip
"""
zip(iterable,......)
    功能：将多个iterable中的值，一个一个拿出来配对组成元组放入迭代器中
    iterable：可迭代的数据(常用：迭代器，容器类型数据，可迭代对象range)
返回：迭代器
注意：只把具有相同索引的元素进行配对，少一个自动舍弃
"""
from collections.abc import Iterable

lst1 = {"Peter", "Ben", "Smith"}
lst2 = {"John", "Alice", "Bob"}
it = zip(lst1, lst2)
print(isinstance(it, Iterable))
for i in it:
    print(i)  # 索引有点凌乱 返回不及预期
