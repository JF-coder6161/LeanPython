"""
所谓字符串，就是由零个或者多个字符组成的有限序列，
在Python程序中，如果我们把单个多多个字符用单引号或双引号包围起来，就可以表示一个字符串

在\后面还可以跟一个八进制或者十六进制数来表示字符，例如\141和\x61都代表小写字母a，前者是八进制的表示法，后者是十六进制的表示法。
也可以在\后面跟Unicode字符编码来表示字符。
"""
import sys

if __name__ == '__main__':
    s1 = '\'hello, world!\''
    s2 = '\n\\hello, world!\\\n'
    print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

# 不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')  # 输出 \'hello, world!\' \n\\hello, world!\\\n
print('\n')

"""
列表
"""
list1 = [1, 2, 3]

for index in range(0, len(list1)):
    print(index)
    print(list[index])

f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
print(sys.getsizeof(f))

x = [(x ** 2 for x in range(1, 3))]
print(sys.getsizeof(x))
y = (x ** 2 for x in range(1, 3))
print(sys.getsizeof(y))
# for val in f:
#     print(val)

"""
元组
Python中的元组与列表类似也是一种容器数据类型，可以用一个变量（对象）来存储多个数据，不同之处在于元组的元素不能修改
"""
t = ('xx', 38, True)

for var in t:
    print(var)

person = list(t)
print(person)

"""
集合
集合不允许有重复元素
"""
# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 向集合添加元素和从集合删除元素。
set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)

"""
字典
可变容器模型,可以存储任意类型对象
字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开
dict()
"""

scores = {'jack': 13, 'Alice': 14, 'Tom': 15}

item1 = dict(one=1, two=2, three=3, four=4)  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(item1)

for key in item1:
    print(f'key = {key} , value = {item1[key]}')

# 字典推导式
items2 = {n: n * 2  for n in range(1, 10)}
print(items2)



