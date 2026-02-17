from romanify import arabic2roman, roman2arabic

arabic = int(input('Арабское число: '))
roman = input('Римское число: ')

try:
    roman = roman2arabic(roman)
except ValueError:
    raise

print('Сумма', arabic + roman, arabic2roman(arabic + roman), sep='\n')
print('Разность:', arabic - roman, arabic2roman(arabic - roman), sep='\n')
print('Произведение:', arabic * roman, arabic2roman(arabic * roman), sep='\n')
print('Частное:', arabic // roman, arabic2roman(arabic // roman), sep='\n')