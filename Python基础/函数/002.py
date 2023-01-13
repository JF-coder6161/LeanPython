# 闭包函数
"""
互相嵌套的两个函数，内函数使用了外函数的一个局部变量
外函数把内函数返回出来的过程叫做闭包，内函数是闭包函数
"""


def family():
    father = 'Jack'
    
    def father_hobby():
        print(f"{father}的爱好是打球")
    
    return father_hobby


func = family()  # func = father_hobby
func()  # func() = father_hobby() # Jack的爱好是打球 生命周期延长


# ###扩展版
def family1():
    sister = "Alice"
    father = "John"
    money = 1000
    
    def sister_hoppy():
        nonlocal money
        money -= 400
        print(f"{sister} like book buy book:{money}")
    
    def father_hoppy():
        nonlocal money
        money -= 550
        print(f"{father} like ball buy ball:{money}")
    
    def master():
        return [sister_hoppy, father_hoppy]
    
    return master


func = family1()  # func = master
print(func)
lst = func()
print(lst)
sister = lst[0]
father = lst[1]
sister()
father()
