# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum((a & b) << 1, a ^ b)

a, b = map(int, input("Введите числа: ").split())

result = sum(a, b)

print(result)
