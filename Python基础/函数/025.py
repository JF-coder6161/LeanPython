# ###时间模块
"""
localtime <=> mktime <=> ctime
时间元组       时间戳       时间字符串

"""
import time

# time() 获取本地时间戳
res = time.time()
print(res)

# localtime() 通过[时间戳]获取[时间元组] (默认当前时间)
res = time.localtime()
print(res)

# 特别指定时间戳，返回时间元组
res = time.localtime(1675043058)

# mktime() 通过【时间元组】获取【时间戳】 （参数是时间元组）
tt1 = (2022,12,21,12,21,21,0,0,0)
res = time.mktime(tt1)
print(res)

# ctime() 通过【时间戳】 获取 【时间字符串】 (默认当前时间)
res = time.ctime(res)
print(res)