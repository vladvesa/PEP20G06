def crypt_decrypt(my_string, key):
    result = []
    for i in my_string:
        result.append(chr(ord(i).__xor__(key)))
    return ''.join(result)


def is_prime(number):
    for i in range(2, number // 2 + 2):
        if not number % i:
            return False
    return True


def generate_primes(limit):
    result = []
    for i in range(limit):
        if is_prime(i):
            result.append(i)
    return result
