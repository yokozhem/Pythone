# 61.
# Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value


import pandas as pd

df = pd.read_csv('/Users/pelmeshka/Documents/Обучение/Python/HomeWork/HW9/california_housing_train.csv')

# Определить какое максимальное и минимальное
# значение median_house_value

print(df['median_house_value'].min()) # находим максимальное и минимальное значение
print(df['median_house_value'].max())
#print(df.loc[:, 'median_house_value'].max()) # альтернивная возможность нахождения мин и макс


# Показать максимальное median_house_value, где
# median_income = 3.1250


print(df[df['median_income'] == 3.1250]['median_house_value'].max())

#Узнать какая максимальная population в зоне
# минимального значения median_house_value

df1 = df.loc[df.median_house_value < df.median_house_value.quantile(.25)] # используем квантиль(процентиль) для установления границы отбора
print(df1.population.max())
print(df1)

#print(df['population'].max(), df['median_house_value'].min())
