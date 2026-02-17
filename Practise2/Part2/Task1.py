cinemaList = [
    {
        'cinemaName': 'Аватар',
        'actorList': ['Сэм Уортингтон', 'Зои Салдана', 'Стивен Лэнг'],
        'sessionList': ['13:30', '15:40', '19:00', '22:05'],
        'ticketPrice': 600,
        'rating': 8.0
    },
    {
        'cinemaName': '28 лет спустя',
        'actorList': ['Элфи Уильямс', 'Аарон Тейлор-Джонсон', 'Джоди Комер'],
        'sessionList': ['12:00', '14:20', '16:50', '20:10'],
        'ticketPrice': 400,
        'rating': 6.1
    },
    {
        'cinemaName': 'Супермен',
        'actorList': ['Дэвид Коренсвет', 'Рэйчел Броснахэн', 'Николас Холт'],
        'sessionList': ['12:45', '14:00', '19:20', '21:30'],
        'ticketPrice': 500,
        'rating': 6.7
    },
    {
        'cinemaName': 'Матрица',
        'actorList': ['Киану Ривз', 'Лоуренс Фишбёрн', 'Кэрри-Энн Мосс'],
        'sessionList': ['10:15', '15:30', '21:00'],
        'ticketPrice': 350,
        'rating': 7.8
    }
]

for cinema in cinemaList:
    print(cinemaList.index(cinema))
    print(f'Название: {cinema.get("cinemaName")}')
    print(f'Актёры: {cinema.get("actorList")}')
    print(f'Сеансы: {cinema.get("sessionList")}')
    print(f'Цена билета: {cinema.get("ticketPrice")}')
    print(f'Рейтинг: {cinema.get("rating")}')