# ### OS.PATH 路径模块
import os
import time

pathvar = r'D:\work\PycharmProjects\LeanPython\Python基础\函数\001.py'
# basename()    返回文件名部分
res = os.path.basename(pathvar)
print(res)
# dirname()     返回路径部分
res = os.path.dirname(pathvar)
print(res)
# split()       将路径分割成单独的文件部分和路径部分，组合成一个元组
tuple1 = os.path.split(pathvar)
print(tuple1)
# join()    将多个路径和文件组成新的路径，可以自动通过不同的系统加不同的斜杠 linux / win \
path1 = r'E:\\' # \\ 是单斜杠的意思
path2 = 'a'
path3 = 'b'
newpath = os.path.join(path1,path2,path3)
print(newpath)
# splitext()    将路径分割为后缀和其他部分
res = os.path.splitext(pathvar)
print(res)
# getsize()     获取文件的大小 (不能计算文件夹大小)
res = os.path.getsize(pathvar)
print(res)

# isdir()   检测路径是否是一个文件夹
# isfile()  检测路径是否是一个文件
# islink() 检测路径是否是一个链接 (快捷方式)



# getctime()    [windows]文件的创建时间,[linux]权限的改动时间，(返回时间戳)
# getmtime()    获取文件最后一次修改时间(返回时间戳)
# getatime()    获取文件最后一次访问时间(返回时间戳)

# exists()  检测指定的路径是否存在
res = os.path.exists(pathvar)
print(res)
# isabs()   检测指定的路径是否是绝对路径
res = os.path.isabs('.')
print(res)
# abspath() 将相对路径转化为绝对路径
res = os.path.abspath('.')
print(res)