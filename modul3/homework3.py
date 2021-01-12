# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have there length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

def ordered_ints(list_of_objects: list):
    result = []
    for i in range(len(list_of_objects)):
        if type(list_of_objects[i]) == tuple:
            aux_str = ''.join(map(str, list_of_objects[i]))
            list_of_objects[i] = int('0' + aux_str)
    list_of_objects = list(map(int, list_of_objects))
    result = sorted(list_of_objects, reverse=True)
    return result


print(ordered_ints([1, True, '123', False, 6, ()]))


# 25P - (do not rush to resolve this)
# For recursive functions try reading the articles below if you find need more information
# https://realpython.com/python-thinking-recursively/
# https://www.python-course.eu/python3_recursive_functions.php
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2

def sum_of_square(n: int):
    square_sum = 0
    for i in range(1, n + 1):
        square_sum += i*i
    return square_sum


def sum_of_square_recursive(n: int):
    if n == 0:
        return 0
    else:
        return sum_of_square_recursive(n-1) + (n*n)


print(sum_of_square(10))
print(sum_of_square_recursive(10))


# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)*(2^2)*(3^2)

def factorial_of_squares(n: int):
    if n == 0:
        return 1
    else:
        return factorial_of_squares(n-1) * (n*n)


print(factorial_of_squares(5))


# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become  ("1234567A", "_ext_to_te_t")

def process_text(text: str):
    split_string = text.split(" ", 1)
    split_string[0] = split_string[0].upper()
    aux = split_string[1]
    for i in range(len(aux)):
        if aux[i].isupper() or aux[i].isnumeric() or aux[i].isspace():
            aux = aux.replace(aux[i], '_')
    # print(aux)
    split_string[1] = aux
    return tuple(split_string)


print(process_text('1234567a Text to te5t'))
