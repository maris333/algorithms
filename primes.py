"""
Zad 1.
Napisz funkcję, która przyjmie liczbę całkowitą n i zwróci pierwsze n liczb pierwszych.
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


"""
Zad 2.  
Napisz funkcję, która przyjmie dodatnią liczbę całkowitą N i zwraca True jeżeli jest liczbą 
pierwszą lub false, jeżeli nie jest 
"""


def is_prime2(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True
