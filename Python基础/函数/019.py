# ### json 序列化和反序列化
"""
所有的编程语言都能够识别的数据格式叫做json，是字符串
python可以转换成json格式数据 有如下类型：(int float bool str list tuple dict None)
# dumps 把任意对象序列化成一个str
# loads 把任意str反序列化成原来的数据
# dump 把对象序列化后写入到file-like object(即文件对象)
# load 把file-like object(即文件对象)中的内容拿出来，反序列化成原来数据
"""
import json

# json 的 dumps
dic = {"name": "Alice", "age": 18, "sex": "女"}
# ensure_ascii 是否显示中文 sort_keys 是否排序
res = json.dumps(dic, ensure_ascii=False, sort_keys=True)
print(res, type(res))

# json loads
dic = json.loads(res)
print(dic, type(dic))

# json dump
with open('lianxi.json', mode="w", encoding="utf-8") as fp:
    json.dump(dic, fp, ensure_ascii=False)

# json load
with open('lianxi.json', mode='r', encoding='utf-8') as fp:
    res = json.load(fp)
    print(res, type(res))

"""
json 与 pickle 的区别
"""
dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}

with open('json1.json', mode='w', encoding='utf-8') as fp:
    json.dump(dic1, fp)
    fp.write("\n")
    json.dump(dic1, fp)
    fp.write("\n")

# 语法上：不可以连续load反序列化数据 （load一次性把文件fp对象中的数据全部获取一下，
# 如果是多个字典无法解析）
# with open('json1.json',mode='r',encoding='utf-8') as fp:
# dic1 = json.load(fp)
# dic2 = json.load(fp)

with open('json1.json', mode='r', encoding='utf-8') as fp:
    for line in fp:
        # 循环2次，拿出一行反序列化一次，以此类推
        dic1 = json.loads(line)
        print(dic1, type(dic1))

# pickle
# 1. 语法上：是否可以连续dump序列化数据？
dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}

import pickle

with open('pickle1.pkl', mode='wb') as fp:
    pickle.dump(dic1, fp)
    pickle.dump(dic2, fp)

# 2. 语法上：是否可以连续load序列化数据？ 可以
# 因为字节流存储时，默认在追加一条数据后添加了结束符，通过结束符，找到一条条的内容
with open('pickle1.pkl', mode='rb') as fp:
    res1 = pickle.load(fp)
    res2 = pickle.load(fp)
    print(res1, type(res1), res2, type(res2))

# 获取所有文件中的数据
with open('pickle1.pkl', mode='rb') as fp:
    while True:
        res = pickle.load(fp)
        print(res,type(res))
        

