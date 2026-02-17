def isWindowFit(height, width, diameter):
    return diameter <= height - 1 and diameter <= width - 1


a = int(input('Высота форточки: '))
b = int(input('Ширина форточки: '))
d = int(input('Диаметр головы Васи: '))

print(isWindowFit(a, b, d))