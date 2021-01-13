# classes

class CarFactory:
    model = 'VW'
    counter = 0

    def __init__(self, colour):
        print('Building car')
        self.colour = colour

    def __le__(self, second_car):
        print('First object:', self)
        print('Second object:', second_car)
        return id(self) <= id(second_car)


print('Class attribute:', CarFactory.model)

car1 = CarFactory('green')
print(car1.colour)
print('Instance var:', car1.model)
car2 = CarFactory('blue')
print(car1.colour)
print('Instance var', car2.model)
print()
# print('Car 1 is:', car1)
# print('Car 2 is:', car2)
# print(dir(car1))
# print()
# # print(car1 < car2)
# print(car1.__le__(car2))
# print(car2.__le__(car1))

# mutable class attributes


class A:
    mutable_object = []

    def change_attr(self, value):
        self.mutable_object.append(value)


a = A()
print(a.mutable_object)
a.change_attr(1)
print(a.mutable_object)
print()
b = A()
print(b.mutable_object)
b.change_attr(2)
print(b.mutable_object)
print()
print(a.mutable_object)

# track how many cars are built


class Factory:
    __counter = [0]

    def __init__(self):
        print()
        self.__counter.append(self.__counter.pop(0) + 1)


first_car = Factory()
second_car = Factory()
print(Factory._Factory__counter)
print()


class A:
    __attr0 = 'really hide'
    _attr1 = 'hide'
    attr2 = 'do not hide'


a = A()
print(a._A__attr0)
print(a._attr1)
print(a.attr2)
