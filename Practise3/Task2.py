def sumOfDigits(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sumOfDigits(n // 10)

def countDigits(n):
    if n < 10:
        return 1
    else:
        return 1 + countDigits(n // 10)

print(sumOfDigits(28))
print(countDigits(28))
print(sumOfDigits(280))
print(countDigits(280))