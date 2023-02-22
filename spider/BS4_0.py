import re
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 解析html_doc 获取BeautifulSoup对象
#soup = BeautifulSoup(html_doc,'html.parser')

# 四种对象
# 一、查找tag对象
soup = BeautifulSoup(html_doc,'html.parser')
print(soup.head,type(soup.head))
print(soup.title,type(soup.title))
print(soup.a,type(soup.a))
print(soup.p.b)

# 二.查找对象的签名和属性
print(soup.a.name) # a
print(soup.p.b.name) # b
print(soup.a['href']) # http://example.com/elsie
print(soup.a.attrs) # {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}

# 三.
'''
HTML4定义了一系列可以包含多个值的属性，在HTML5中移除了一些，却增加更多
最常见的多值的属性是class (一个tag可以有多个CSS的class).
还有一些属性 rel , rev , accept-charset , headers , accesskey
在Beautiful Soup中多值属性的返回类型是list

'''

print(soup.a['class'],type(soup.a['class'])) #['sister'] <class 'list'>

# 四、tag的属性可以被添加,删除或修改(tag的属性操作方法与字典一样)
# soup.a["class"] = ["sister c1"]
# del soup.a["id"]
# print(soup)

# 五. 获取标签对象的文本内容
print(soup.p.string) # The Dormouse's story
print(soup.p.strings) # <generator object Tag._all_strings at 0x0000024AF4C16350>
for i in soup.strings:
    print(i)
# 如果tag包含了多个子节点，tag就无法确定 .string方法应该调用哪个子节点的内容，.string的输出
# 结果是None，如果只有一个子节点那么就输出该子节点的文本，比如下面的这种结构
tag = soup.findAll("p")[1]
print(tag.string) # None
print(tag.strings) # <generator object Tag._all_strings at 0x000001D296053F90>

# text and string
print(soup.p.string)
print(soup.p.text) # 取到p下所有的文本内容，text属性更常用，并且它可以直接过滤掉注释
print(tag.text)

markup = "<b><!--Hey, buddy.Want to buy a used parser--></b>"
soup = BeautifulSoup(markup,'html.parser')
comment = soup.b.string
print(comment) # Hey, buddy.Want to buy a used parser
print(type(comment)) # <class 'bs4.element.Comment'>

