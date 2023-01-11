alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 使用字典
# 在Python中，字典是一系列键—值对。每个键都与一个值相关联，你可以使用键来访问与之
# 相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对
# 象用作字典中的值。

# 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 添加键-值对
alien_0 = {'color': 'green', 'points': 5}
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

# 创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 修改字典中的值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'red'
print("The alien is " + alien_0['color'] + ".")

# 删除键-值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

