# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def recursive_power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return recursive_power(a * a, b // 2)
    else:
        return a * recursive_power(a * a, (b - 1) // 2)

a = int(input("Какое число возводим в степень: "))
b = int(input("В какую степень возводим: "))

result = recursive_power(a, b)

print(f"{a} в степени {b} равно {result}")