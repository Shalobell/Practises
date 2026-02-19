import re
import pandas as pd
from collections import Counter

with open('file.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()


text = ''.join(lines).lower()
words = re.findall(r'\b[а-яё]{2,}\b', text)


word_counts = Counter(words)
top10 = word_counts.most_common(10)

df = pd.DataFrame(top10, columns=['Слово', 'Частота'])
print(df) # вывод датафрейма

df.to_csv('top10_words.csv', index=False, encoding='utf-8-sig')
df.to_excel('top10_words.xlsx', index=False)