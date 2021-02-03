# We want to create class for an object that behaves like a triangle, that has flexible sides and angles.
# Because of approximations in python the triangle will get distorted after some of the changes so this is not a
# perfect model

# 30P
#  - class constructor can receives 3 arguments for angles (with default value of 60) and 3 arguments for sides (with
# default value of 1)
# class variables for sides will be called A, B, C
# class variables for angles will be called AB, BC, CA (indicating sides)

# 30P
# - class implements method to modify_angle:
#   - modify_angle method takes two argument:
#       - "angle" and can be one of 3 string values 'AB', 'BC', 'CA'
#       - "degrees" that can be a positive or negative and represents the amount by which the angle will be modified
# If as a result of the change any of the angles will be outside interval (0, 180) then method should raise an exception
# When an angle is modified you will need to recalculate the opposing side which can be done using the following
# example: angle AB is changed then C = (A**2 + B**2 - 2*A*B*cos(AB))**(1/2)
# Because angles in a triangle must sum up to 180 degrees unmodified angles need to be recalculated after we have
# recalculated the opposite side using the following example:
# angle AB is changed then BC = arccos((B**2+ C**2 - A**2) / (2*B*C)), CA = arccos((C**2+ A**2 - B**2) / (2*C*A)),


# 30P
# - class implements method to modify_side:
#   - modify_side method takes two argument:
#       - "side" and can be one of 3 string values 'A', 'B', 'C'
#       - "meters" that can be a positive or negative and represents the amount by which the side will be modified
# If as a result of the change sum of the unmodified sides is less then or equal to the changed side then method should
# throw an exception
# If as a result of the change side will be less then or equal to 0 then method should raise a different exception
# When a side is modified by some value all other sides need to be modified by the fraction of the change to maintain
# the same triangle angles. For example if A increase by +1 then B = ((A+1)/A)*B and C = ((A+1)/A)*C

from math import cos, acos, degrees


class Triangle:
    A = B = C = 1
    AB = BC = CA = 60

    def __init__(self, a=1, b=1, c=1, ab=60, bc=60, ca=60):
        self.A = a
        self.B = b
        self.C = c
        self.AB = ab
        self.BC = bc
        self.CA = ca

    def modify_angle(self, angle, degrees_to_add):
        if angle == "AB":
            self.AB += degrees_to_add
            self.C = (self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * cos(self.AB)) ** (1 / 2)
            self.BC = degrees(acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C)))
            self.CA = degrees(acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A)))
        elif angle == "BC":
            self.BC += degrees_to_add
            self.A = (self.B ** 2 + self.C ** 2 - 2 * self.B * self.C * cos(self.BC)) ** (1 / 2)
            self.AB = degrees(acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B)))
            self.CA = degrees(acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A)))
        elif angle == "CA":
            self.CA += degrees_to_add
            self.B = (self.C ** 2 + self.A ** 2 - 2 * self.C * self.A * cos(self.CA)) ** (1 / 2)
            self.AB = degrees(acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B)))
            self.BC = degrees(acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C)))
        if not (0 <= self.AB <= 180 or 0 <= self.BC <= 180 or 0 <= self.CA <= 180):
            raise ValueError("Angle out of range")

    def modify_side(self, side, meters):
        if side == "A":
            self.A += meters
            self.B = ((self.A + meters) / self.A) * self.B
            self.C = ((self.A + meters) / self.A) * self.C
            if self.B + self.C <= self.A:
                raise AttributeError("Modified side A too small")
        elif side == "B":
            self.B += meters
            self.A = ((self.B + meters) / self.B) * self.A
            self.C = ((self.B + meters) / self.B) * self.C
            if self.A + self.C <= self.B:
                raise AttributeError("Modified side B too small")
        elif side == "C":
            self.C += meters
            self.A = ((self.C + meters) / self.C) * self.A
            self.B = ((self.C + meters) / self.C) * self.B
            if self.A + self.B <= self.C:
                raise AttributeError("Modified side C too small")
        if self.A <= 0 or self.B <= 0 or self.C <= 0:
            raise ValueError("Side equal to 0")


# 10P
# Create an object from your class with default constructor values and modify angle AB by +30 degrees and side A by +1.5
triangle = Triangle()
triangle.modify_angle("AB", 30)
print("Angles: \n", "AB =", triangle.AB, "\n", "BC =", triangle.BC, "\n", "CA =", triangle.CA)
triangle2 = Triangle()
triangle2.modify_side("A", 1.5)
print("Sides:\n", "A =", triangle2.A, "\n", "B =", triangle2.B, "\n", "C =", triangle2.C)

