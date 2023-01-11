# 导入整个模块
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# 导入特定的函数
from pizza import make_pizza

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

# 使用as 给函数指定别名
from pizza import make_pizza as mp
mp(16,'pepperoni')

# 使用as 给模块指定别名
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入模块中的所有函数
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

# 函数编写指南
# 给形参指定默认值时，等号两边不要有空格：
# def function_name(parameter_0, parameter_1='default value')
# 对于函数调用中的关键字实参，也应遵循这种约定：
# function_name(value_0, parameter_1='value')

