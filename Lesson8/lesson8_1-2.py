import time


class Auto:
    def __init__(self, brand: str, age: int, mark: str):
        self.brand = brand
        self.age = age
        self.mark = mark

    color = None
    weight = None

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1


# a=Auto(brand='BMW',age=3,mark='M5')
# print(a.brand)
#
# print(a.mark)
# print(a.age)
# a.birthday()
# print(a.age)
# a.move()
# a.stop()
# print(a.color)
# a.color='red'
# print(a.color)

class Truck(Auto):
    def __init__(self, max_load: int, brand: str, age: int, mark: str):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self, ):
        print('Attention')
        super(Truck, self).move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_speed: int, brand: str, age: int, mark: str):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super(Car, self).move()
        print(f'max speed is {self.max_speed}')


car1 = Car(max_speed=90, brand='lada', age=40, mark='1')
car2 = Car(max_speed=250, brand='mercedes', age=10, mark='220')
truck1 = Truck(max_load=30, brand='scania', age=20, mark='1')
truck2 = Truck(max_load=40,brand='volvo', age=10,mark='tx90')

print(car1.age)
print(car1.mark)
print(car1.max_speed)
print(car1.brand)
car1.move()

print(car2.age)
print(car2.mark)
print(car2.max_speed)
print(car2.brand)
car2.move()

print(truck1.age)
print(truck1.mark)
print(truck1.max_load)
print(truck1.brand)
truck1.move()
truck1.load()

print(truck2.age)
print(truck2.mark)
print(truck2.max_load)
print(truck2.brand)
truck2.move()
truck2.load()
