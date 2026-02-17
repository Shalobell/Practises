start = int(input('Начало диапазона: '))
k = int(input('Последняя цифра: '))
s = int(input('Кратны числу: '))

count = 0

while count != 10:
    if start % 10 == k and start % s == 0:
        print(start)
        count += 1
    start += 1