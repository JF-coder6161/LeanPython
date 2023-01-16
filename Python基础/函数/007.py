# ### reduce
"""
reduce(func,iterable)
功能：
    先把iterable里面的前两个数据拿到func函数当中进行运算，得到结果
    在把计算的结果和iterable中的第三个数据拿到func里面进行运算
    依次类推，直到iterable里面的所有数据都拿完为止，程序结束
参数：
    func    内置或自定义函数
    iterable    具有可迭代性的数据([迭代器],[容器类型的数据],[range对象])
返回值：
    计算的最后结果
"""
from functools import reduce

# [7,7,5,8] => 整数7758
# 7 * 10 + 7 = 77
# 77 * 10 + 5 = 775
# 775 * 10 + 8 = 7758
lst = [7, 7, 5, 8]


def func(x, y):
    return x * 10 + y


res = reduce(func, lst)
print(res)

# 7758 => [7,7,5,8]
lst = "7758"


def func1(i):
    dic = {}
    for item in range(10):
        dic[str(item)] = item
    return dic[i]


it = map(func1, lst)
lst = list(it)

res = reduce(lambda x, y: x * 10 + y, lst)
print(res)
