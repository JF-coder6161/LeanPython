class ClassA:
    var1 = 100
    var2 = 0.01
    var3 = '两点水'
    
    def fun1():
        print('fun1')
    
    def fun2():
        print('fun2')
    
    def fun3():
        print('fun3')


print(ClassA.var1)
print(ClassA.var2)
print(ClassA.var3)


class ClassB:
    var1 = '两点水'
    
    @classmethod
    def fun1(cls, age):
        print('i am fun1' + cls.var1)
        print('age: ' + str(age))


'''
从内部来修改增加类的属性
'''


class ClassC:
    var1 = 'Jack'
    
    @classmethod
    def fun1(cls):
        print('var1 : ' + cls.var1)
        cls.var1 = input('input var1 value')
        print('change var1: ' + cls.var1)
        cls.var2 = input('add var2 input var2 value')
        print('add var2: ' + cls.var2)


'''
从外部来修改增加类的属性
'''


class ClassD:
    var = 'Ben'
    
    @classmethod
    def fun1(cls):
        print('ClassD var: ' + cls.var)


class ClassE(object):
    var = 'Jack'
    
    def fun1(self):
        print('var: ' + self.var)


'''
初始化函数
'''


class ClassF(object):
    name = 'Black'
    
    def __init__(self, name):
        self.name = name
        print('init 初始化' + self.name)
    
    def __del__(self):
        print('dell del')

if __name__ == '__main__':
    '''
    ClassA.fun1()
    ClassA.fun2()
    ClassA.fun3()
    ClassB.fun1(18)
    ClassC.fun1()
    
    ClassD.fun1()
    ClassD.var = 'Alice'
    ClassD.fun1()
    
    ClassD.var2 = input('ClassD add var2: ')
    print(ClassD.var2)

    '''
# 实例化
a = ClassE()
a.fun1()
print(a.var)

# 初始化函数，析构函数
b = ClassF('Alice')
del b

