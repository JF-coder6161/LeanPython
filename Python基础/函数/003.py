# 闭包的特点
"""
在闭包情况下，内函数使用了外函数的局部变量
该局部变量与内函数发生了绑定，将延长该局部变量的生命周期
"""


def outer(num):
    def inner(val):
        return num + val
    
    return inner


func = outer(10)
print(func)

# func() <=> inner()
res = func(5)
print(res)
print(outer(5)(5))  # 保存num变量 延长num变量生命周期

# 闭包的意义
# 闭包可以优先使用外函数中的变量，并对闭包中的值起到了封装保护的作用。外部无法访问
num = 0


def count():
    global num
    num += 1
    print(num)


count()
count()
count()
num = 100  # 被攻击
count()
count()


def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
        return count
    inner()
    print(count,42)
    return inner

func = outer()
print(func())
print(func())
count = 100
print(func())

"""
总结：
    延长生命周期是特点
    封装保护成员是意义
"""

