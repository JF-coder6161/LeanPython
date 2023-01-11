# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# 字符串查找
str = "Chairman"

# 未查找到(返回-1)
str.find("a")
# 右侧查找
str.rfind("ir")

# 返回找字符的索引（如果找不到抛错）
str.index("i")

# 从右侧查找
str.rindex("ir")

# 计数
str.count('i', 1, 2)

# split 切分
str1 = "my name is Tom"
str1.split(" ")
print(str1.split(' ', 2))

# 移除前缀
str1.removeprefix("my")
# 移除后缀
str1.removesuffix("om")

# 替换
print(str1.replace("my", "My"))

# 特殊方法
# encode(字符编码相关)

name = ["Monkey", "Celina", "Black"]

# join
print("-".join(name))

# maketrans 生成密码本
source = "abcdefghi"
output = "012345678"
password_table = str.maketrans(source, output)
msg = "hello baby"
print(msg.translate(password_table))

import string

print(string.ascii_letters)
print(string.printable)

source2 = string.printable
output2 = string.printable[::-1]

password_table2 = str.maketrans(source2, output2)
msg = "Hello baby, I miss you so much , want to see you ,but afraid the female tiger find out .."
encrypt_msg = msg.translate(password_table2)



