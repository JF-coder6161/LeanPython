if __name__ == '__main__':
    a = int(input("a = "))
    b = int(input("b = "))
    print('%d + %d = %d' % (a, b, a + b))
    print('%d - %d = %d' % (a, b, a - b))
    print('%d * %d = %d' % (a, b, a * b))
    print('%d / %d = %f' % (a, b, a / b))
    print('%d // %d = %d' % (a, b, a // b))
    print('%d %% %d = %d' % (a, b, a % b))
    print('%d ** %d = %d' % (a, b, a ** b))

"""
逻辑运算符
not 逻辑取反 相当于java ！
"""

flag = not (1 != 2)
print('flag5 = ', flag)

"""
将华氏温度转换为摄氏温度
"""

f = float(input('请输入华氏温度： '))
c = (f - 32) / 1.8
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

"""
输入年份判断是不是闰年
"""
year = int(input('请输入年份： '))
# 如果代码太长写成一行不便于阅读，可以使用 \ 对代码进行折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
          year % 400 == 0
print(is_leap)

"""
分支结构
if
elif
else
"""

"""
for-in 循环
range(101):产生0到100范围的整数，需要注意的是取不到101
range(1,101)：产生1到100范围的整数，相当于前面是闭区间后面是开区间
range(1,101,2): 2为步长，产生1~100的奇数
range(100,0,-2): 产生100~1的偶数，-2是步长
"""

sum = 0
for x in range(101):
    sum += x
    print(sum)

"""
while
"""

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入： '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜')
        break
    print('你总共猜了%d次' % counter)
    if counter >7:
        print('IQ lower')

