# ### 生成器
"""
# 元组推导式的返回值是一个生成器对象，简称生成器，生成器本质就是迭代器
# 迭代器与生成器区别：
    迭代器本身是系统内置的.重写不了，而生成器是用户自定义的，可以重写迭代逻辑
# 生成器可以用两种方式创建：
    1.生成器表达式(里面是推导式，外面用圆括号)
    2.生成器函数 （用def定义，里面含有yield）
都会创建一个生成器
生成器是特殊的迭代器，可以自定义内部的迭代逻辑
"""
from collections.abc import Iterable , Iterator
# 1.创建生成器表达式
gen = (i for i in range(10))
print(gen) # <generator object <genexpr> at 0x00000287483630B0>
print(isinstance(gen,Iterator)) # True

# 调用生成器
for i in gen:
    print(i)
