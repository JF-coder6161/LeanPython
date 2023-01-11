# 根据约定，在Python中，首字母大写的名称指的是类
class Dog():
    
    # 类中的函数称为方法
    # 形参self必不可少，还必须位于其他形参的前面。
    # 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    def __init__(self,name,age):
        # 可以通过实例访问的变量称为属性
        self.name = name;
        self.age = age;
        
    def sit(self):
        print(self.name.title() + "is now sitting")
    
    def roll_over(self):
        print(self.name.title() + "rolled over")
        
my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()