# Dictionaries
empty_dictionary = {}
print(empty_dictionary)
print(type(empty_dictionary))

dictionary_with_values = dict(a='a')
print(dictionary_with_values)

my_dictionary = {1: 'a', 2: 'b'}
print(my_dictionary)

list1 = [1, 2]
list2 = [1, 2, 3]
my_dictionary = {None: 'a', True: 'b'}
list1.append(2)

my_str = 'abc'
print(dir(my_str))
print(my_str.__hash__())
# print(list1.__hash__())
print((1, 3, True).__hash__())
print()

# mutable
new_dict = dict()
print(id(new_dict), new_dict)
new_dict.update({'a': 'b'})
print(id(new_dict), new_dict)

# Methods
keys = new_dict.keys()
print(type(keys), next(keys.__iter__()))
values = new_dict.values()
print(type(values), next(values.__iter__()))
items = new_dict.items()
print(type(items), next(items.__iter__()))
print()

# Unpack tuple
var1, var2, var3, *var4, var5 = (1, 2, 3, 4, 5, 6)
print(var1, var2, var3, var4, var5)
for x, y in [var4]:
    print(x, y)
print()

# Get method and []
print(new_dict.get('a'))
print(new_dict['a'])
print()

# Remove key
new_dict.pop('a')
print(new_dict)
print()

# Exercise
mag1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}
mag2 = {'mere': 11, 'pere': 15, 'prune': 6}
mag3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}
lista_de_magazine = {'mag1': mag1, 'mag2': mag2, 'mag3': mag3}
lista_de_cumparaturi = {'mere': 2, 'pere': 3, 'prune': 6}


def best_buy(shops, shopping_list):
    totals = {}
    result = None
    total_cost = None
    for product, number_of_items in shopping_list.items():
        for shop_name, shop_items in shops.items():
            cost = shop_items[product] * number_of_items
            print(f'In {shop_name} object {product} costs: ', cost)
            totals.update({shop_name: totals.get(shop_name, 0) + cost})
    print(totals)
    for shop, total_price in totals.items():
        if total_cost is None or total_cost > total_price:
            result = shop
            total_cost = total_price
    return result


print('Best shop to buy in is:', best_buy(lista_de_magazine, lista_de_cumparaturi))
print()


# Find prime number
def is_prime(number):
    for i in range(2, number//2 + 2):
        if not number % i:
            return False
    return True


print(is_prime(7))
print(is_prime(30))


def primes(limit):
    result = []
    for i in range(limit):
        if is_prime(i):
            result.append(i)
    return result


print(primes(150))
print()

# Set
my_set = set()
print(type(my_set), my_set)

my_set1 = {1, 2, 3, 4, 5, 5}
print(type(my_set1), my_set1)

my_set2 = {1, 3, 5}
my_set2.update({7})
print(my_set2)

print(my_set2.pop())

print(my_set2.difference(my_set1))
print(my_set1.difference(my_set2))
print(my_set2.intersection(my_set1))
print(my_set1.intersection(my_set2))
print(my_set1.symmetric_difference(my_set2))
print(my_set2.symmetric_difference(my_set1))
print(my_set1.union(my_set2))
print(my_set2.union(my_set1))
print()

# Exercise
test_data = [[1, 2, 3], [3, 3, 5], [8, 9, 4]]


def pinball_game_test(game_data, full_range = 10):
    range_values = set(range(1, full_range + 1))
    full_set = set()
    for match_game in game_data:
        full_set = full_set.union(match_game)
    return range_values.difference(full_set)


print(pinball_game_test(test_data))
