# exceptions
from time import sleep

var = 2

try:
    sleep(0)
    result2 = 2 / var
    if var == 0:
        result1 = 2 / '0'
except ZeroDivisionError:
    print('Bad division')
except TypeError:
    print('Bad operand type')
except Exception:
    print('Something is wrong')
else:
    print('This will only execute if no exception is caught')
finally:
    print('This will always be executed')
print()


# function to divide input number to 2


def check_if_not_0(nr=0):
    if nr == 0:
        raise ValueError('Number is 0')
    print('Value is not 0')


def div(divider=2):
    var1 = input("Give number: ")
    if divider == 0:
        raise AttributeError('Divider is 0')
    elif divider % 2 != 0:
        raise AttributeError('Divider is odd', 'Wrong value')
    else:
        try:
            return int(var1) / divider
        except ValueError:
            print('Wrong var type')


try:
    print(div(1))
except AttributeError as e:
    print('Try again')
    if e.args[0] == 'Divider is 0' and e.args[1] == 'Wrong value':
        print(e.args[0])
    elif e.args[0] == 'Divider is odd':
        print(e)
