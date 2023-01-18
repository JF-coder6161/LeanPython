# ### 递归函数
# 递归函数：自己调用自己的函数

def digui(n):
    print(n,"<===开头===>")
    if n > 0:
        digui(n - 1)
    print(n,"<=========>")

digui(5)
