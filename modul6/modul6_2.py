class Car:
    __key = 123510
    _engine = 1.8

    def __init__(self, color):
        self.attribute = color
        self.__key = 78910
        self._engine = 2

    def start_car(self):
        self.__engine_code = 521
        print("Car started")


class Animal(object):
    def __init__(self, species):
        self.species = species

    def hunt(self, prey):
        print("Does nothing")


class Wolf(Animal):
    bark = True

    def __init__(self, species):
        super().__init__(species)
        self.attribute = 'wild'

    def hunt(self):
        print("hunting")
        # raise NotImplemented

    def method_1(self):
        pass


class Coyote(Animal):
    bark = True

    def __init__(self, species):
        super().__init__(species)
        self.attribute = 'wild'

    def hunt(self):
        print("hunting more")
        # raise NotImplemented

    def method_1(self):
        pass

    def has_more_teeth(self):
        print("Adding teeth")


class Dog(Wolf, Coyote, Animal, Car):
    def __init__(self, species):
        super().__init__(species)
        self.attribute = 'domestic'

    def hunt(self):
        print("can't do that")

    def method_2(self):
        pass


dog = Dog("dog")
print('dog barks: ', dog.bark)
dog.method_2()
dog.method_1()
dog.hunt()
print(dog.attribute)
dog.has_more_teeth()
dog.start_car()


class Suv(Car):
    def __init__(self, color, size):
        super(Suv, self).__init__(color)
        self.size = size
        self._Car__key = 456123
        self._engine = 3

    def all_wheel_drive(self):
        print("All wheel drive active")


suv = Suv("green", 12)
print(suv._Car__key)
print(suv._engine)
suv.start_car()
print(suv._Car__engine_code)
suv._Car__engine_code = 20
print(suv._Car__engine_code)
