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

