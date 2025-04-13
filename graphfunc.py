# graphfunc
from graph import *
from functools import cache, wraps
from time import time

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


if __name__ == '__main__':
    start = time()
    print(10.995574287564276/2)
    print(time() - start)

