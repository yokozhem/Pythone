# 57. 
# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

import pandas as pd

df = pd.read_csv('/Users/pelmeshka/Documents/Обучение/Python/HomeWork/HW9/california_housing_train.csv')

# print(df.head(10))
# #https://jupyter.org/

# print(df[df['housing_median_age'] < 20][['total_bedrooms','total_rooms']])

print(df.shape) #определяет размер таблицы: количество строк и количество столбцов
print(df.dtypes)# определяет тип данных столбцов