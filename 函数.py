"""
函数
"""


def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
        return result


if __name__ == '__main__':
    """函数的参数"""
from random import randint


def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


"""
可变参数
"""
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))


"""
避免命名冲突
用模块管理函数

from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()

或则

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()
"""

"""
需要说明的是，如果我们导入的模块除了定义函数之外还有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，
if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"。

eg module3.py
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
    
test.py
import module3
xxxx
"""