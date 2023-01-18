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
dic = {"name":"Alice","age":18,"sex":"女"}
# ensure_ascii 是否显示中文 sort_keys 是否排序
res = json.dumps(dic,ensure_ascii=False,sort_keys=True)
print(res,type(res))

# json loads
dic = json.loads(res)
print(dic,type(dic))

# json dump
with open('lianxi.json',mode="w",encoding="utf-8") as fp:
    json.dump(dic,fp,ensure_ascii=False)
    
# json load
with open('lianxi.json',mode='r',encoding='utf-8') as fp:
    res = json.load(fp)
    print(res,type(res))
    
"""
json 与 dump的区别
"""