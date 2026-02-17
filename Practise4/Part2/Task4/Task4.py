from vector import *

v1 = Vector([2, 4])
v2 = Vector([0, 1])      # единичный вектор по оси Y

print('v1 =', v1.components)
print('v2 =', v2.components)

print('Длина v1:', v1.length())
print('Длина v2:', v2.length())

v3 = v1 * 4
print('v1 * 4 =', v3.components)

v4 = 5 * v2
print('5 * v2 =', v4.components)

dot = v1.scalarProduct(v2)
print('v1 · v2 =', dot)

angle_rad = v1.angleWith(v2)
angle_deg = v1.angleWith(v2, degrees=True)

print(f'Угол в радианах: {angle_rad:.4f}')
print(f'Угол в градусах: {angle_deg:.2f}')