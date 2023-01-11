class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    # 通过方法修改属性的值
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    # 通过方法对属性的值进行递增
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("please increment gass")


class Battery:
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


# 定义子类时，必须在括号内指定父类的名称
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # 将实例用作属性
        self.battery = Battery()
    
    # 重写父类的方法
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")