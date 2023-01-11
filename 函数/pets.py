# 位置实参
def describe_pet(animal_type,pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster','harry')

# 关键字实参

describe_pet(pet_name='harry',animal_type='hamster')

# 默认值
# 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。

def describe_pet1(pet_name,animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet1("harry")

