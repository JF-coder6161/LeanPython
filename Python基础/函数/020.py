# ### random 随机模块
import random

# random() 获取随机0-1之间的小数(左闭右开)
res = random.random()
print(res)

#randrange() 随机获取指定范围内的整数(包含开始值,不包含结束值，间隔值) 同range
# 一个参数 0 1 2
res = random.randrange(3)
# 两个参数 3 4 5
res = random.randrange(3,6)
# 三个参数
res = random.randrange(1,10,3) # 1 4 7

# randint() 随机产生指定范围内的随机整数
res = random.randint(1,3) # 1 2 3

# uniform() 获取指定范围内的随机小数(左闭右开)
res = random.uniform(2,4) # 2 <= x < 4
print(res)
res = random.uniform(4,2) # 2 < x <= 4

# choice() 随机获取序列中的值(多选一)
lst = [1,2,3,4]
res = random.choice(lst)
print(res)

# 自定义choice
def mychoice(lst):
    length = len(lst)
    num = random.randrange(length)
    return lst[num]

# 简写
func = lambda lst : lst[random.randrange(len(lst))]
print(func(lst))


# sample() 随机获取序列中的值(多选多) [返回列表]
lst = ['Alice','jack','ben','petter']
res = random.sample(lst,2)
print(res,type(res))

# shuffle() # 随机打乱序列中的值(直接打乱原序列)
random.shuffle(lst)
print(lst)

