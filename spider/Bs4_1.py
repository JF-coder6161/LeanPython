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

soup = BeautifulSoup(html_doc, 'html.parser')

# 1.嵌套选择
print(soup.head.title.text)  # The Dormouse's story
print(soup.body.a.text)  # Elsie

# 2.子节点 子孙节点
print(soup.p.contents)  # 找寻P标签下所有子节点
print(
    soup.p.children)  # 得到一个迭代器，包含p下所有子节点 <list_iterator object at 0x000001B8AB7182E0>

for i, child in enumerate(soup.p.children, 1):
    print(i, child)
