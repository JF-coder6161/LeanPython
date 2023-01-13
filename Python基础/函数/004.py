# ### 匿名函数
"""
python代码追求简洁高效
lambda表达式：用一句话来表达只有返回值的函数
语法
lambda 参数 : 返回值
"""


# (1) 有参lambda表达式
def func(num):
    return type(num)


res = func(10)
print(res)

# 改写
func = lambda num: type(num)
print(func)
print(func(100))


# (2) 无参lambda表达式
def func1():
    return "hello world"


func1()

# 改写
func2 = lambda: "Hello world"
print(func2)
print(func2())


# (3) 带有判断条件的lambda表达式

def func(num):
    if num % 2 == 0:
        return "偶数"
    else:
        return "奇数"


res = func(13)
print(res)

# 改写
num = 100
res = "偶数" if num % 2 == 0 else "奇数"
print(res)

# 改写
res = lambda num: "偶数" if num % 2 == 0 else "奇数"
print(res(13))
