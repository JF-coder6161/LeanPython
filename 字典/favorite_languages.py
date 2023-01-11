# 由类似对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(
    "Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# 遍历字典中的所有键

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + " ! "
              )

if 'erin' not in favorite_languages.keys():
    print("Erin , please take our poll !")

# 按顺序遍历字典中的所有键

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 遍历字典中的所有值
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# 去重
print("----- Let's distinct -----")
for language in set(favorite_languages.values()):
    print(language.title())

# 字典中存储列表

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name,favorite_language in favorite_languages.items():
    
    if len(favorite_language) == 1:
        print("\n" + name.title() + "'s favorite languages are:" + favorite_language[0])
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in favorite_language:
            print("\t" + language.title())
            
