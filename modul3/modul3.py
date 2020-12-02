# For loop
# Iterable object
string1 = 'My str'
print(dir(string1))

# Next for iterable objects
print(type(string1.__iter__()))
print(dir(string1.__iter__()))
print()
iterator = string1.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

number1 = 1234
print(dir(number1))

my_int = 123
# for i in my_int:
#     print(i)

my_bool = True
print(dir(my_bool))
print()

for i in 'My text':
    print(i)
print("Done")
print()

# Compare string
nr = ord('a')
print(f"Number of a: {nr}")
nr = ord('b')
print(f"Number of b: {nr}")
print()

print('Check if a == b:', 'a' == 'b')
print('Check if a.__eq__(b):', 'a'.__eq__('b'))
print('Check if a < b:', 'a' < 'b')
print('Check if a < b:', 'a'.__lt__('b'))
print('Check if a <= b:', 'a' <= 'b')
print('Check if a <= b:', 'a'.__le__('a'))
print('Check if a > b:', 'a' > 'b')
print('Check if a > b:', 'a'.__gt__('a'))
print('Check if a >= b:', 'a' >= 'b')
print('Check if a >= b:', 'a'.__ge__('b'))
print()

# Exercise exit for on _
for i in "My_text":
    if i == "_":
        break
    print(i)
print()

# Exercise print 'yey' if _ not in text
var1 = ''
for i in "My_text":
    if i == "_":
        break
else:
    print('yay')

# Sum of all letters if ' ' does not appear
sum = 0
for i in 'My text':
    if i != " ":
        sum += ord(i)
    else:
        break
else:
    print(sum)

# Print last letter if text longer than 3
my_string = 'My text'
nr_char = 0
last_letter = ''
for i in my_string:
    nr += 1
    if nr > 3:
        last_letter = i
else:
    print(last_letter)
print()

# len fcn
print(len('my_text'))
print("my_text".__len__())
print()

text = "my_text"
if len(text) > 3:
    for i in text:
        pass
    print(i)

# Continue
# New text without spaces
text = 'my text'
new_text = ''
for i in text:
    if i == ' ':
        continue
    new_text += i
print(new_text)

# Add only letters >100
text = 'abxz'
new_text = ''
for i in text:
    if ord(i) <= 100:
        continue
    new_text += i
print(new_text)
print()

# While loop
a = 3
while a > 2:
    a -= 1
    print('True')

# read while value < 100
# my_bool = True
# while my_bool:
#     nr = int(input())
#     print(nr)
#     if nr > 100:
#         my_bool = False

# len(text) < 5 then add new characters
my_text = 'my_text'
new_text = ''
var2 = 0
while len(new_text) < 5:
    new_text += my_text[var2]
    var2 += 1
    print(new_text)

# Function range
range_obj = range(10)
print(type(range_obj))
range_iter = range_obj.__iter__()
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))

for i in range(3):
    print('in for:', i)

for i in range(2, 6, 2):
    print('in for with step 2:', i)

# Assignment operator
var1 = 1
print(var1)
var1 += 1
