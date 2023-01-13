# ### 互相嵌套的函数

"""
互相嵌套的两个函数outer和inner
分别为外函数和内函数
"""

def outer():
    def inner():
        print("我是inner函数")
        
# 内部函数可以直接在函数外部调用么？
# inner() 不可以
# 调用外部函数后，内部函数可以在函数外部调用么？
# outer()
# inner() 不行 因为inner是局部变量，只能作用在函数outer内部，无法作用在全局空间
# 内部函数可以在函数内部调用么？
def outer():
    def inner():
        print("我是inner函数")
    inner()
# 可以
# 内部函数在函数内部调用时，是否有先后顺序
# 必须先定义在调用;error

# 注意点，在其他语言中，允许直接调用函数，在定义函数，因为其他语言存在预加载机制，在代码执行前，
# 提前把函数加载到内存，然后在执行脚本，而python是解释型语言，执行一句编译一句，不存在预加载机制
# 所以只能先定义在调用

"""
寻找变量的调用顺序采用LEGB原则(即就近原则)
B -- Builtion(Python): Python内置模块的命名空间      (内建作用域)
G -- Global(module): 函数外部所在的命名空间           (全局作用域)
E -- Enclosing function locals; 外部嵌套函数的作用域  (嵌套作用域)
L -- Local(function): 当前函数内的作用域              (局部作用域)
依据就近原则,从下往上 从里向外 依次寻找
"""

print(print)

"""
nonlocal 符合LEGB原则，就近找变量原则
通过nonlocal用来修改当前作用域上一层空间的变量
如果上一层没有该数据，继续向上寻找，
直到再也找不到了，直接报错
"""

def outer():
    def inner():
        a = 200
        def smaller():
            nonlocal a
            a = 100
            print(a,"53")
        smaller()
        print(a,"50")
    inner()
outer()

"""
a = 200  # 此处为全局变量 nonlocal无法找到，报错
def outer():
    def inner():
    
        def smaller():
            nonlocal a
            a = 100
            print(a,"53")
        smaller()
        print(a,"50")
    inner()
outer()

"""
