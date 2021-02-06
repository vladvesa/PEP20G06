""" Homework 6 - needs to be presented before exam day
A car factory requires a class for an iterable object that can be used to keep track of car serial and lot numbers
produced in a certain day. A instance variable called "day" will record the date, in any format/value you prefer.
Lot number and serial number had values of 0 and 0 respectively for the first car produced.
Serial number is incremented with each car produced, lot number is incremented every 20 cars produced.
Each instance of the class will get constructor arguments the starting serial and number of cars produced for that day.
Your instance will need to calculate the lot numbers and serials produced in that specific day.
ex: Instance has start serial 30 and number of cars produced is 30 meaning resulting in serial numbers produced that day
are: 30, 31 ..59, 60 and lot numbers produced that day are 1, 2, 3 (serial 60 is part of lot 3)
Cars with odd serial number are right side driving cars and the cars with even serial number are left side driving cars.
Your instance will have methods for returning serial numbers for right side driving cars and left side driving cars.
Iterating the object will return the lot numbers produced that day
1) Implementation:
    a) Correct implementation of iterable object. 10P
    b) Correct implementation of iterator object. 10P
    c) Correct implementation of methods returning right and left side driving cars. 20P
2) Execution:
    a) Create object from class defined above using start serial 111 and number of cars produced 91. 10P
    b) Print all left hand and right hand serials for the object above: 10P
    c) Iterate the object created above and write the lot numbers on new lines in a file. 20P
3) Document:
   a) Add type hints for all arguments 5P
   a) Add module documentation 5P
   b) Add document all classes 5P
   c) Add document all methods 5P

   Creating the car factory classes using a class for iterator and a class for object
"""
from datetime import date


class CarIterator:
    """Iterator class for CarFactory class"""
    def __init__(self, lot):
        self.lot = lot

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lot) == 0:
            raise StopIteration
        return self.lot.pop(0)


class CarFactory:
    """ Class for cars definition """
    def __init__(self, starting_serial: int, cars: int):
        self.serial_list = []
        self.lot_list = []
        self.serial_list.append(starting_serial)
        self.day = date.today()
        self.starting_lot = starting_serial//20
        for i in range(1, cars + 1):
            self.serial_list.append(starting_serial + i)
        for j in range(1, cars + 2, 20):
            self.starting_lot += 1
            self.lot_list.append(self.starting_lot)

    def __iter__(self):
        return CarIterator(self.lot_list)

    def __next__(self):
        pass

    def right_side_drive(self) -> list:
        """
        Method that gets odd serial numbers and assigns them to right side driven cars list
        :return: list of right side driven cars
        """
        right_drive_list = []
        for i in self.serial_list:
            if i % 2 != 0:
                right_drive_list.append(i)
        return right_drive_list

    def left_side_drive(self) -> list:
        """
        Method that gets even serial numbers and assigns them to left side driven cars list
        :return: list of left side driven cars
        """
        left_drive_list = []
        for i in self.serial_list:
            if i % 2 == 0:
                left_drive_list.append(i)
        return left_drive_list


cars_built = CarFactory(111, 91)
print(cars_built.serial_list)
print(cars_built.lot_list)
right_drive = cars_built.right_side_drive()
left_drive = cars_built.left_side_drive()
print("Right side drive:", right_drive)
print("Left side drive:", left_drive)

with open("car_lot.txt", "x") as file:
    for lot_nr in cars_built:
        file.write(str(lot_nr) + "\n")
