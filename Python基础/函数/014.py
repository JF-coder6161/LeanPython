# 生成器函数
"""
yield关键字 类似于 return
共同点在于：执行到这句话都会把值返回回去
不同点在于：yield每次返回时，会记住上一次离开时执行的位置，下次在调用生成器，会从上次执行的位置
        往下走而return直接终止函数，每次重头调用
yield 6 和 yield(6) 2种写法都可以 yield 6 更像 return 6 的写法 推荐使用
"""


# （1）基本定义 ： 生成器函数
def gen():
    print("one")
    yield 1
    print("two")
    yield 2
    print("three")
    yield 3


# 初始化生成器函数，返回生成器对象 g
g = gen()

# 调用生成器
res = next(g)
print(res)

res = next(g)
print(res)

res = next(g)
print(res)


# (2) 优化代码
def mygen():
    for i in range(1, 101):
        yield "{}号球星".format(i)


g = mygen()
for i in range(3):
    res = next(g)
    print(res)

# (3)send收发数据
"""
send 可以 类比成 next
send 既可以调用数据，还可以发送数据
yield 既可以返回数据，还可以接收数据
"""


def mygen():
    print("start ...")
    
    res = yield 111
    print(res, "内部")
    
    res = yield 222
    print(res, "内部")
    
    res = yield 333
    print(res, "内部")
    
    print("end ...")


# 初始化生成器函数，返回生成器对象
g = mygen()
# 默认第一次发送数据时候，必须是None，因为此刻刚刚开始执行，还没有运行到yield，所以没人接收
# 只能发None
res = g.send(None)
print(res)  # 111
# 在第二此时，因为已经存有了上一次yield 执行的代码状态，所以可以发送了
res = g.send(1)
print(res)  #
res = g.send("发过去456")
print(res)


# res = g.send("发过去789") # error StopIteration
# print(res)

# (4) yield from 将第一个可迭代对象变成一个迭代器返回

def mygen():
    # yield [1, 2, 3]
    yield from [1, 2, 3]


g = mygen()
print(next(g))
print(next(g))
print(next(g))


# ###
def mygen(n):
    a = 0
    b = 1
    
    i = 0
    while i < n:
        # print(b)
        yield b  # 可以控制打印次数
        a, b = b, a + b
        i += 1


g = mygen(10)
for i in range(3):
    print(next(g))
