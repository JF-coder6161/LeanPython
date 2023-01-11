filename = 'pi_digits.txt'
with open(filename) as file_object:
    
    # 读取整个文件
    # contents = file_object.read()
    # print(contents.rstrip())
    
    # 逐行读取
    # for line in file_object:
    #     print(line.rstrip())
    
    # 创建一个包含文件各行内容的列表
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())