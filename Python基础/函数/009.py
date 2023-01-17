# ### 推导式

"""
推导式种类三种：
    [val for val in Iterable] 列表推导式
    {val for val in Iterable} 集合推导式
    {a:b for a,b in Iterable} 字典推导式
"""
# 1. 单循环推导式
lst = []
for i in range(1, 101):
    lst.append(i)
# 改写
lst = [i for i in range(1, 5)]
print(lst)

# 2. 带有判断条件的单循环推导式
lst = [i for i in range(1, 5) if i % 2 == 0]
print(lst)
# 3. 多循环推导式
lst1 = ['jack', 'Alice', 'John']
lst2 = ['Peter', 'Ben', 'Smith']
lst_new = []
for i in lst1:
    for j in lst2:
        res = i + "fr" + j
        lst_new.append(res)
print(lst_new)

# 改写
lst = [i + "fr" + j for i in lst1 for j in lst2]
print(lst)

# 4. 带有判断的多循环推导式
lst1 = ['jack', 'Alice', 'John']
lst2 = ['Peter', 'Ben', 'Smith']
lst_new = []
for i in lst1:
    for j in lst2:
        if lst1.index(i) == lst2.index(j):
            res = i + "fr" + j
            lst_new.append(res)
print(lst_new)

# 改写
lst1 = ['jack', 'Alice', 'John']
lst2 = ['Peter', 'Ben', 'Smith']
lst_new = [i + "fr" + j for i in lst1 for j in lst2 if
           lst1.index(i) == lst2.index(j)]
print(lst_new)
