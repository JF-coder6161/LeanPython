# 传递任意数量的实参
# 形参名*toppings中的星号让Python创建一个名为toppings的空元组
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
    
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# 结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


