# ### 数学模块
import math
from collections.abc import Iterable,Iterator
# ceil() 向上取整
res = math.ceil(3.9)
print(res)

# floor() 向下取整
res = math.floor(3.9)
print(res)

# pow() 计算一个数值的N次方(结果为浮点数)

# sqrt() 开平方运算(结果浮点数)
res = math.sqrt(3)
print(res)
# fabs() 计算一个数值的绝对值(结果浮点数)
res = math.fabs(-12)
print(res)

# modf() 将一个数值拆分为整数和小数两个部分组成元组
res = math.modf(3.14)
print(isinstance(res, tuple))
res = iter(res)
for item in res:
    print(item) # 0.14000000000000012 3.0
    
# copysign() 将参数第二个数值的正负号拷贝给第一个 (结果浮点数)
res = math.copysign(1,-2)
print(res)

# fsum() 将一个容器数据中的数据进行求和运算 (结果浮点数)

lst = [1,2]
res = math.fsum(lst)
print(res)