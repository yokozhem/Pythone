# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

df = pd.read_csv('/Users/pelmeshka/Documents/Обучение/Python/HomeWork/HW9/california_housing_train.csv')

df1 = df.loc[df.population < df.population.quantile(.30)] 
print(df1.households.max())