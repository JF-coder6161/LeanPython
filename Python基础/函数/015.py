# ### 内置函数
"""
round 四舍五入 (n.5 n为偶数则舍去 n.5 n 为奇数，则进一)
bin 10进制转换成2进制
oct 10进制转换成8进制
hex 10进制转换成16进制
chr 将ASCII编码转换为字符
ord 将字符转换为ASCII码
eval 将字符串当作python代码执行 (可以获取到返回值)
exec 将字符串当作python代码执行(功能强大) (不能获取到返回值)
repr 不转义字符输出字符串
hash 转换成hash值
"""

# max min 高阶使用

lst = [
    (16, "Jack"),
    (19, "Alice"),
    (17, "Ben")
]


def func(n):
    print(n)
    return n[0]


res = max(lst, key=func)
res = min(lst, key=func)
print(res)

# pow 计算某个数值的x次方
res = pow(2, 3)
print(res)
res = pow(2, 3, 3)
print(res)

# eval
strvar = "print(123)"
res = eval(strvar)
print(res)  # None

# exec
strvar = "a = 1"
exec(strvar)
print(a)  # 1

strvar = """
for i in range(2):
    print(i)
"""
exec(strvar)

# repr 不转义字符输出字符串  相当于元字符串
res = repr("E:\py\nday")
print(res)

# hash 生成哈希值
"""相同数据，哈希值一致，用在文本校验或者密码校验环节"""
res1 = hash("abc")
res2 = hash("abc")
print(res1, res2)

# 集合 为什么集合放纯数字是固定不变的原因：因为hash出的值总是固定的,由hash算法决定
setvar = {1, 2, 3, 4}
print(setvar)
print(hash(1))
print(hash(2))
print(hash(3))
