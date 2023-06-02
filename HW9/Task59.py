# 59. 
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000


import pandas as pd

df = pd.read_csv('/Users/pelmeshka/Documents/Обучение/Python/HomeWork/HW9/california_housing_train.csv')

print(df.isnull()) # выводит пустые значения
print(df.isnull().sum()) # суммирует пустые значения

print(df[df['median_income'] < 2][['median_house_value',]]) # Показать median_house_value где median_income < 2

print(df.describe()) # описание столбцов
print(df[['longitude', 'latitude']]) # выводит информацию только конкретных столбцов
print(df.iloc[:, 0:2]) # выводит информацию только конкретных столбцов

print(df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)])
# print(df[(df.housing_median_age < 20) & (df.median_house_value > 70000)])или можно прописать так


