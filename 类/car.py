class Car():
    
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


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(34)
my_new_car.read_odometer()
my_new_car.update_odometer(22)

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_used_car.odometer_reading = 1
my_used_car.read_odometer()