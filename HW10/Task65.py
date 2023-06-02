# Задача №65. Решение в группах
# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограмм

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/pelmeshka/Documents/Обучение/Python/HomeWork/HW10/penguins.csv')
print(df.head())
print(df.columns)
# print(df.describe())

# ● Использовать 2-3 точечных графика

# sns.scatterplot(data = df, x = 'species' , y ='island')
# sns.scatterplot(data = df, x = 'bill_length_mm' , y ='species')

# точечный график по оттенкам
# sns.scatterplot(data = df, x = 'bill_length_mm' , y ='bill_depth_mm', hue = 'bill_length_mm', size = 'bill_length_mm', sizes = (2,100))
# sns.scatterplot(data = df, x = 'bill_length_mm' , y ='flipper_length_mm', hue = 'flipper_length_mm', size = 'flipper_length_mm  ', sizes = (2,100))


#  ● Использовать PairGrid с типом графика на ваш выбор
# cols = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)


# ● Изобразить Heatmap
penguins = sns.load_dataset("penguins")

numeric_columns = penguins.select_dtypes(include=[float, int]).columns
sns.heatmap(data=penguins[numeric_columns].corr())

# ● Использовать 2-3 гистограмм

plt.show(block=True)
