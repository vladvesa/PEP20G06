# Functions
def my_print(value):
    print(type(value))
    print(value)


my_print('hello world')
print()


# Multiple arguments
def my_print(value, value2, value3):
    print(type(value))
    print(value, value2, value3)


my_print('hello world', 'x', 'y')
print()


def my_print(*args, end='\n'):
    print(type(args))
    print(type(end))
    print(*args, end=end)


my_print('hello world', 'x', 'y', end='$\n')
print()


def my_print(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(*args, **kwargs)


my_print('hello world', 'x', 'y', end='$\n', sep='_')
print()


# def print_string():
#     my_string = input()
#     print(my_string)
#
#
# print_string()
# print()


# Return
def add_numbers(nr1, nr2):
    result = nr1 + nr2
    print(result)


add_numbers(1, 2)
print()


def add_numbers(nr1, nr2):
    result = nr1 + nr2
    return result


sum = add_numbers(1, 2)
print(sum)
print()


def power(nr1, nr2):
    return nr1 ** nr2


nr_pow = power(2, 3)
print(nr_pow)
print()

# Function object
print(add_numbers)
print(add_numbers.__call__(1, 2))
print()

for i in range(3):
    def add_numbers(nr1, nr2):
        result = nr1 + nr2
        return result
    print(add_numbers)
print()


# Nested functions
number2 = 10


def outside(number):
    def inside():
        return number + number2
    return inside


var1 = outside(10)
print(type(var1))
print(var1())
number2 = 11
print(var1())
print()


def func1(*args):
    list1 = []
    for i in args:
        def infunc():
            print(i)
        list1.append(infunc)
    return list1


var1 = func1('a', 'b', 'c')
print(var1)
print()

# Lists
empty_list = []
print(empty_list)
empty_list = list()
print(dir(empty_list))
var1 = 3

print(id(empty_list))
empty_list.append(1)
print(empty_list)
empty_list.append(True)
print(empty_list)
print(id(empty_list))
empty_list.append(var1)
print(empty_list)
print(id(empty_list))
var1 = 4
print(empty_list)
print(id(empty_list))
print()

my_list_outside = []
my_list_outside.append(1)
my_list_inside = []
my_list_outside.append(my_list_inside)
my_list_inside.append(2)
print(my_list_outside)
my_list_inside.append(3)
print(my_list_outside)
print()

# tuple
empty_tuple = ()
one_object_tuple = (1, )
two_object_tuple = (1, 'a')
no_brackets_tuple = 1, 'a', True
print(type(no_brackets_tuple))
print(no_brackets_tuple)
new_two_object_tuple = (1, 'a')
new_two_object_tuple += None,
print(new_two_object_tuple)
print(id(two_object_tuple), id(new_two_object_tuple))
print()


def function(my_string, key):
    list1 = []
    for i in my_string:
        list1.append(chr(ord(i).__xor__(key)))
    return ''.join(list1)


encrypted = function('Hello world', 129)
print(encrypted)
decrypted = function(encrypted, 129)
print(decrypted)
print()

# Bitwise operations
result = 3 and -1  # classical
print(result)
result = 3 & -1  # bit
print(result)

print(-1 ^ 3)
print((-1).__xor__(3))
