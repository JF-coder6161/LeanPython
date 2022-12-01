"""
列表特性
有序
有索引，可切片，可遍历

删除
names.clear 清空
names.pop 删除（默认删除最后一个元素,可指定位置索引)
names.remove 删除(从前开始删除)
del (全局)

改:
切片:(前闭后开 [x,x) )
list[0:5]
正切:
list[0:]
步长:(参数最后一位为步长)
list[0:8:2]
倒切:( [x,x) )
list[-4:-1]
反转:
list[::-1]

查
'A' in list
list.count("1") 有多少个“1”
list.index("a")

特殊
反转
list.reverse()
排序
list.sort()
合并
list.extend(xx)

copy
浅copy (注意列表嵌套)  a.copy
深copy
import copy
copy.deepcopy(a)

列表生成式
[f"staff-{i} for i in range(1,30)]
"""
if __name__ == '__main__':

    staff_list = [f"staff-{i}" for i in range(1, 30)]
    print(staff_list)
