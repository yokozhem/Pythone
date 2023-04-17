# Задача 6: Вы пользуетесь общественным транспортом? 
#Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

ticket_number=int(input("Введите шестизначное число для проверки: "))
n1 = int(ticket_number//100000)
n2 = int(ticket_number/10000%10)
n3 = int(ticket_number/1000%10)
n4 = int(ticket_number/100%10)
n5 = int(ticket_number/10%10)
n6 = int(ticket_number%10)

sum1 = n6+n5+n4
sum2 = n3+n2+n1
if sum1 == sum2:
    print("У вас счастливый билет.Поздравляем!!!")
else:
    print("Увы, но нет, повезет в другой раз")


# Второй вариант
# number = input("Введите номер билета: ")

# first_sum = int(number[0]) + int(number[1]) + int(number[2])
# second_sum = int(number[3]) + int(number[4]) + int(number[5])

# if first_sum == second_sum:
#     print("yes")
# else:
#     print("no")

# Третий вариант решения задачи

# number = input("Введите номер билета: ")

# # Проверяем, что введен корректный шестизначный номер
# if len(number) != 6 or not number.isdigit():
#     print("Некорректный номер билета")
# else:
#     # Суммируем первые и последние три цифры номера
#     first_sum = sum(int(x) for x in number[:3])
#     second_sum = sum(int(x) for x in number[3:])

#     # Проверяем, равны ли суммы
#     if first_sum == second_sum:
#         print("Билет счастливый!")
#     else:
#         print("Билет несчастливый :(")