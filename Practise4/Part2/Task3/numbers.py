import math


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def isPrime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def inverse(n: float) -> float:
    if n == 0:
        raise ValueError('There is no inverse number for 0')
    return 1 / n

def sqrt(n: float) -> float:
    if n < 0:
        raise ValueError('The square root of a negative number is undefined in real numbers.')
    return math.sqrt(n)