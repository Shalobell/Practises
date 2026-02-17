def getRoot(a, b, c):
    if not a:
        return 'Error!'
    d = b ** 2 - 4*a*c
    if d < 0:
        return 'Rational squares do not exist!'
    elif d == 0:
        return round(-b / (2*a), 1)
    x1 = round((-b + d ** 0.5) / (2*a), 1)
    x2 = round((-b - d ** 0.5) / (2*a), 1)
    return x1, x2

a = int(input())
b = int(input())
c = int(input())

print(getRoot(a, b, c))