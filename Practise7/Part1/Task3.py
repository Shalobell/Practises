import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Имя': ['Алексей', 'Анна', 'Григорий', 'Евгений', 'Антон'],
    'Возраст': [18, 20, 22, 30, 21],
    'Стипендия': [2000, 4000, 1500, 5000, 2000],
    'Курс': [3, 5, 2, 1, 4],
    'Средняя_оценка': [4.5, 4.8, 4.2, 4.9, 4.6]
}

df = pd.DataFrame(data)
print("Исходный DataFrame:")
print(df)

print("1. Название колонок:")
print(df.columns.tolist())

print("2. Индексация по столбцу 'Имя':")
print(df['Имя'])
print("Индексация по столбцу 'Стипендия':")
print(df['Стипендия'])

print("3. Применение метода loc:")
print("Первые 3 строки:")
print(df.loc[0:2])
print("Выборка по условию (Стипендия > 3000):")
print(df.loc[df['Стипендия'] > 3000])
print("Выборка конкретных строк и столбцов (loc[0:2, ['Имя', 'Стипендия']]):")
print(df.loc[0:2, ['Имя', 'Стипендия']])

df['НовыйСтолбец'] = df['Стипендия'] * 0.5
print("4. Добавлен новый столбец 'НовыйСтолбец':")
print(df)

print("5. Сравнение столбцов:")
comparison = df['Стипендия'] > df['Курс'] * 1000
print("Сравнение: Зарплата > Опыт_работы * 1000")
print(comparison)

comparison2 = df['Возраст'] >= 25
print("Сравнение: Возраст >= 25")
print(comparison2)

comparison3 = df['Стипендия'] > df['НовыйСтолбец'] * 10
print("Сравнение: Стипендия > НовыйСтолбец * 10")
print(comparison3)

data2 = {
    'Имя': ['Алексей', 'Иван'],
    'Возраст': [20, 19],
    'Стипендия': [1500, 4000],
    'Курс': [4, 5],
    'Средняя_оценка': [4.7, 4.5],
    'НовыйСтолбец': [3000, 8000]
}

df2 = pd.DataFrame(data2)

print("6. Объединение DataFrame:")
print("Второй DataFrame:")
print(df2)

df_vertical = pd.concat([df, df2], ignore_index=True)
print("Объединение по вертикали (concat):")
print(df_vertical)

data3 = {
    'Город': ['Москва', 'Новороссийск', 'СПб', 'Москва', 'Волгоград'],
    'Факультет': ['IT', 'Юриспурденция', 'IT', 'Физмат', 'Физмат']
}

df3 = pd.DataFrame(data3)
df_horizontal = pd.concat([df, df3], axis=1)
print("Объединение по горизонтали (concat axis=1):")
print(df_horizontal)

print("7. Метод describe (статистическое описание):")
print(df.describe())

print("8. Кумулятивная сумма:")
df['Кумулятивная_Стипендия'] = df['Стипендия'].cumsum()
print("Кумулятивная сумма по столбцу 'Стипендия':")
print(df[['Имя', 'Стипендия', 'Кумулятивная_Стипендия']])

df['Кумулятивный_курс'] = df['Курс'].cumsum()
print("Кумулятивная сумма по столбцу 'Курс':")
print(df[['Имя', 'Курс', 'Кумулятивный_курс']])
print()

print("9. Построение графиков:")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(df['Имя'], df['Стипендия'], color='skyblue')
plt.title('Стипендия по студентам')
plt.xlabel('Имя')
plt.ylabel('Стипендия')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.plot(df['Имя'], df['Кумулятивная_Стипендия'], marker='o', color='green')
plt.title('Кумулятивная сумма стипедии')
plt.xlabel('Имя')
plt.ylabel('Кумулятивная стипендия')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.savefig('dataframe_plot.png')
print("Графики сохранены в файл 'dataframe_plot.png'")
plt.show()

print("Финальный DataFrame:")
print(df)