# Print in base2
print(0b0100)

# Print in base8
print(0o17)
print(0o24)

# Print in base16
print(0x11)

# Exponents
print(5e10)

# Arithmetic Operations
number1 = 3
number2 = 4
number3 = -3

print('Division 3/4: ', number1 / number2)
print('Floor division 3//4: ', number1 // number2)
print('Remainder 3%4: ', number1 % number2)
print('Zero: ', number1 + number3)

print('3 to the power of 4: ', number1 ** number2)

a = 3
b = 4
c = 5
result = (-b - pow(pow(b, 2) - 4 * a * c, 1 / 2)) / (2 * a)
print('Quadratic formula result: ', result)

print('Type of -3: ', type(-3))
print('Type of 0.75: ', type(0.75))
print('Type of result: ', type(result))

# String:
string1 = 'Hello world'
string1 = "Hello world"
string1 = '''Hello world'''
string1 = """Hello world"""
string5 = u'Hello\nworld'
print(string1)
string5 = r'Hello\nworld'
print(string1)
string5 = f'Hello world: {string1}'
print(string1)

# String slices
result = string5[4]
print('Fourth char: ', result)
result = string5[-3]
print('Third char from right: ', result)
result = string5[4:7]
print('Fourth to seventh char: ', result)
result = string5[4:9:2]
print('Fourth to nineth char: ', result)
result = string5[-2:-6:-1]
print(result)
result = string5[3:-1]
print('Third to next to last char: ', result)

# Dot notation for strings:
print('string actions: ', dir(string1))
print(string1.lower())
print(string1.capitalize())
print(string1.upper())
string1 = string1 + ' {}'
print(string1.format('test'))

print(string1.find('ll'))
print(string1.center(20, '#'))
print(string1.replace(string1[1], 'Y'))

# Dot notation for int:
print('Sum: ', number1.__add__(number2))
print((3).__add__(4))
print('Multiplication: ', number1.__mul__(number2))
print('Division: ', number1.__truediv__(number2))
print('Power: ', number1.__pow__(number2))

# Input fcn
# print('Your name is:', input('Enter name: '))
# my_name = input('Enter last name: ')
# print('Your last name is:', my_name)

# number1 = input('first number: ')
# number2 = input('second number: ')
# print('Sum =', number1 + number2)
#
# # Casting
# number1 = int(number1)
# number2 = int(number2)
# print(number1 + number2)
#
# number1 = 2
# number2 = 3
# print('Tip number 1 pre-conv:', type(number1))
# number1 = str(number1)
# print('Tip number1:', type(number1))
# number2 = str(number2)
# print('Sum:', number1+number2)
#
# # Exercises
# sideAB = input('Enter side AB: ')
# sideBC = input('Enter side BC: ')
# area = (int(sideAB) * int(sideBC))/2
# print('Area is:', area)

# Bool
true1 = True
print(id(true1))
true2 = True
print(id(true2))

# Binary operations
# And operation
result = True and True
print('Response type:', type(result), result)
# Or operation
result = False or False
print('Response type:', type(result), result)
# Xor operation
print(dir(True))
print('True xor False:', True.__xor__(False))

# Unary operations
# Not operation
result = not True
print('Not True is:', result)
print('Not result is:', not result)

# Order of operation
print((not True) or True)
print(not (True or True))
print('Correct:', not True or True)

print(True or (not True))
print('Correct:', True or not True)

# and
print((not False) and (not False))
print(not not(False and False))
print('Correct: ', not False and not False)

# Homework
print(True and True or False and False)
print()

# Cast
print('String bool:', str(True))
print('Integer bool True:', int(True))
print('Integer bool False:', int(False))
print('String "false" to bool:', bool('false'))
print('String "" to bool:', bool(''))
print('Int "100" to bool:', bool(100))
print('Int "0" to bool:', bool(0))
print()

# Length of object
print('length of "text"', len('text'))
print('length of ""', len(''))
print()

# Bool operations
# Add bool objects
print('True + True + True =', True + True + True)
print('True - True - True =', True - True - True)
print()

# None object
none = None
print('id:', id(none), id(None))
print(dir(None))
print()

# Applications
string1 = 'Text to scramble'
print('Initial string:', string1)

# Rearrange odd letters
# string1 = string1[0::2]+string1[1::2]
# print('Rearranged string:', string1)
#
# string1 = string1[::-1]
# print('Rearranged string:', string1)

# string1 = string1[0::3] + string1[1::3] + string1[2::3]
# print('Rearranged string:', string1)

string1 = string1[-1::-2] + string1[-2::-2]
print('Rearranged string:', string1)
print()

string1 = "^"
print(string1.center(8, "_"))
print()

string1 = "---"
string2 = "| |"
print(string1.center(7, "_"))
print(string2.center(7, "_"))
print(string1.center(7, "_"))

# if statement
# Comparison
print('Result of comp 1 with 1:', 1 == 1)
print('Result of comp 1 < 1:', 1 < 1)
print('Result of comp 2 > 1:', 2 > 1)
print('Result of comp 2 >= 1:', 2 >= 1)
print('Result of comp 2 != 1:', 2 != 1)
print()

# my_number = int(input("Give number: "))
# if my_number < 3:
#     print(f'Number {my_number} smaller than 3')
# elif my_number > 5:
#     print(f'Number {my_number} greater than 5')
# else:
#     print(f'Number {my_number} is good')
print()

for my_var in 'My text':
    print(my_var)

print()
my_new_text = ''
for my_var in 'Text to scramble':
    my_new_text = my_var + my_new_text

print(my_new_text)
print(my_new_text[::-1])
