# Задача №63. Решение в группах
# 1. Изобразите отношение households к population с
# помощью точечного графика
# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
df = pd.read_csv('/Users/pelmeshka/Documents/Обучение/Python/HomeWork/HW10/california_housing_train.csv', names=columns, header=0)

#1
sns.scatterplot(data=df, x='households', y='population')

#2
sns.relplot(x = 'longitude', y = 'median_house_value', kind = 'line', data = df)
plt.show(block=True)

#3 
sns.histplot(data  = df, x = 'housing_median_age')

#4
sns.displot(df, x = 'median_house_value', hue = 'housing_median_age')

plt.show(block=True)