def isLeap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysInMonth(month, year):
    if month == 2:
        return 29 if isLeap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def previousDate(day, month, year):
    if day > 31:
        return 'invalid day'
    elif month > 12:
        return 'invalid month'
    elif day > 1:
        return str(day - 1) + '.' + str(month) + '.' + str(year)
    else:
        if month == 1:
            return str(31) + '.' + str(12) + '.' + year - 1
        else:
            prevMonth = month - 1
            prevDays = daysInMonth(prevMonth, year)
            return str(prevDays) + '.' + str(prevMonth) + '.' + str(year)

def nextDate(day, month, year):
    if day > 31:
        return 'invalid day'
    elif month > 12:
        return 'invalid month'

    daysCurrent = daysInMonth(month, year)

    if day < daysCurrent:
        return str(day + 1) + '.' + str(month) + '.' + str(year)
    else:
        if month == 12:
            return str(1) + '.' + str(1) + '.' + str(year + 1)
        else:
            return str(1) + '.' + str(month + 1) + '.' + str(year)

print(previousDate(1, 12, 2017))
print(nextDate(1, 12, 2017))
print(previousDate(1, 3, 2016))
print(nextDate(28, 2, 2016))

print(previousDate(41, 3, 2016))
