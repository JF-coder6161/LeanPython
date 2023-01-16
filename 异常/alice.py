file_name = 'alice.txt'

try:
    with open(file_name) as file_object:
        line = file_object.read()
        print(line)
except FileNotFoundError:
    print("File not Found please check!")
else:
    print("found file success")