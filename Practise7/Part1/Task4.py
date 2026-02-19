import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('high_pollution.csv', sep=';', encoding='utf-8')

print('Загружено строк: ', len(df))

dfVolga = df.loc[(df['river_basin'] == 'р. Волга') & (df['indicator'] == 'Нитрит-ионы') & (df['period'] == '2008-01-31')]

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

print(dfVolga['value_max'])


# 1. Горизонтальная столбчатая диаграмма

subject = dfVolga['subject'].to_list()
value_max = dfVolga['value_max'].to_list()
# colors = plt.cm.viridis(np.linspace(0, 1, len(subject)))

axes[0, 0].bar(subject, value_max)
axes[0, 0].set_xlabel('Регион', fontsize=8)
axes[0, 0].set_ylabel('Загрязнение', fontsize=8)
axes[0, 0].set_title('1. Горизонтальная столбчатая диаграмма\nМаксимальное загрязнение р. Волга по регионам за 31 января 2008', fontsize=8)
axes[0, 0].grid(axis='x', alpha=0.3)


# 2. Первый линейный график (Московская обл)
dfMoscowVolga = df.loc[(df['river_basin'] == 'р. Волга') & (df['indicator'] == 'Нитрит-ионы') & (df['subject'] == 'Московская область')]

period = [item for _, item in zip(range(6), dfMoscowVolga['period'].to_list())]
value_max = [item for _, item in zip(range(6), dfMoscowVolga['value_max'].to_list())]

axes[0, 1].plot(period, value_max, marker='o', linewidth=2,
                color='blue', markersize=8)

axes[0, 1].set_xlabel('Период', fontsize=8)
axes[0, 1].set_ylabel('Максимальный уровень загрязнения', fontsize=8)
axes[0, 1].set_title('2. Линейный график\nЗагрязнение р. Волга в Московской обл.', fontsize=8)
axes[0, 1].grid(True, alpha=0.3)

# 3. Второй линейный график (Нижегородская область)

dfVologdaVolga = df.loc[(df['river_basin'] == 'р. Волга') & (df['indicator'] == 'Нитрит-ионы') & (df['subject'] == 'Вологодская область')]

period = [item for _, item in zip(range(6), dfVologdaVolga['period'].to_list())]
value_max = [item for _, item in zip(range(6), dfVologdaVolga['value_max'].to_list())]

axes[1, 0].plot(period, value_max, marker='o', linewidth=2,
                color='blue', markersize=8)

axes[1, 0].set_xlabel('Период', fontsize=8)
axes[1, 0].set_ylabel('Максимальный уровень загрязнения', fontsize=8)
axes[1, 0].set_title('2. Линейный график\nЗагрязнение р. Волга в Московской обл.', fontsize=8)
axes[1, 0].grid(True, alpha=0.3)


# 4. Диаграмма рассеивания

sample_df = df.loc[(df['river_basin'] == 'р. Волга') & (df['indicator'] == 'Нитрит-ионы') & (df['subject'] == 'Московская область')]
scatter = axes[1, 1].scatter(sample_df['cnt_cases'].to_list(), sample_df['value_max'].to_list(),
                             alpha=0.6, c=sample_df['value_max'], cmap='plasma', s=50)

axes[1, 1].set_xlabel('Количество случаев загрязнения', fontsize=8)
axes[1, 1].set_ylabel('Максимальный уровень загрязнения', fontsize=8)
axes[1, 1].set_title('4. Диаграмма рассеивания\nСвязь между уровнем загрязнения р. Волга и количеством зафиксированных случаев загрязнения', fontsize=8)
plt.colorbar(scatter, ax=axes[1, 1], label='Уровень загрязнения')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('waterPollution.png', dpi=300, bbox_inches='tight')
plt.show()