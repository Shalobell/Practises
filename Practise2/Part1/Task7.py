me = {
    "first_name": "Grigory",
    "last_name": "Litvinov",
    "middle_name": "Sergeevich",
    "position": "Developer",
    "age": 23,
    "salary": "300$",
    True: False
}

print(str(me.get('last_name') + " " + me.get('first_name')))
me['position'] = 'Performance artist'
del me[True]
print(me)