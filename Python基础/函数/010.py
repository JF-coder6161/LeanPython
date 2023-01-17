# ### 集合推导式

lst = [
    {"name": "张三", "money": 1900, "age": 19},
    {"name": "王五", "money": 1000000, "age": 50},
    {"name": "李四", "money": 5500, "age": 18},
    {"name": "赵二", "money": 20000, "age": 20}
]
setvar = set()
for i in lst:
    if 18 <= i["age"] <=21 and 5000 <= i["money"] <= 5500:
        res = "尊贵VIP卡老{}".format(i["name"][0])
    else:
        res = "抠脚大汉老{}".format(i["name"][0])
    # 把数据添加到集合中
    setvar.add(res)
print(setvar)

# 改写成集合推导式
setvar = {"尊贵VIP卡老{}".format(i["name"][0]) if 18 <= i["age"] <=21 and 5000 <= i["money"] <= 5500 else "抠脚大汉老{}".format(i["name"][0]) for i in lst }
print(setvar)



