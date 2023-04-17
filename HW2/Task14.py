# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число N: "))

for i in range(n):
    power_of_2 = 2 ** i
    if power_of_2 > n:
        break
    print(power_of_2, end=' ')