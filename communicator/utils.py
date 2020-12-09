def function(my_string, key):
    list1 = []
    for i in my_string:
        list1.append(chr(ord(i).__xor__(key)))
    return ''.join(list1)