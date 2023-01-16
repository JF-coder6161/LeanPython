file_name = 'programming.txt'

with open(file_name,'w') as file_object:
    file_object.write("I love programming .\n")
    # 写入多行
    file_object.write("I love creating new games .\n")
    #  附加到文件

with open(file_name,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets. \n")
    file_object.write("I love creating apps that can run in a browser. \n")