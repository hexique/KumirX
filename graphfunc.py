# graphfunc
from graph import *
from math import inf, sqrt
import random
import hashlib

whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

# def memory(func):
#     cache = {}

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key = str(*args)
#         if key not in cache:
#             cache[key] = func(*args, **kwargs)
#         return cache[key]
#     return wrapper

def isprime(num):
    if str(num)[-1] in '024568': return False
    for i in range(2, num):
        if num % i == 0: return False
    return True

def prime(id):
    count, number = 0, 0
    while count <= id:
        number += 1
        if isprime(number): 
            count += 1
            continue
    return number

def fibonacci(id):
    nums = [1, 1]
    current = 1
    for i in range(id):
       current = nums[-1] + nums[-2]
       nums.append(current)
    return current

def collatz(n):
    result = [n]
    while n != 1 and n != 0:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        result.append(n)
    return result

def divisiors(n):
    result = [1]
    for i in range(2, n+1):
        if n % i == 0:
            result.append(i)
    return result

def nextprime(n):
    n = int(n)
    while True:
        if isprime(n):
            return n
        n += 1

def prevprime(n):
    n = int(n)
    while True:
        if isprime(n):
            return n
        elif n == 0:
            return 0
        n -= 1

def average(list):
    return sum(list) / len(list)

def cond(condition: bool, func):
    if condition:
        return func
    else:
        return inf

def strToInt(str: str) -> int:
    result = ''
    for i in str:
        if i in digits:
            result += i
    while result.startswith('0'):
        result = result[1:]
    if result == '':
        return 0
    return int(result)

def randomStr(length: int, symbols: str) -> int:
    return ''.join([random.choice(symbols) for i in range(length)])

def returnsError(func) -> bool:
    try:
        return func
    except:
        return inf

def esqrt(num):
    if num >= 0:
        return sqrt(num)
    else:
        return inf

def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def logf(func):
    print(func)
    return 0

if __name__ == '__main__':
    print(sha256('123'))
