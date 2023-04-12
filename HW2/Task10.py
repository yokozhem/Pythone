# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random

n_coins = int(input("Сколько моент лежит на столе: "))
coins = []
for i in range(n_coins): 
    coin = random.randint(0, 1)
    coins.append(coin)
print(coins)
count = 0

for i in coins:
    if i == 0:
        count+=1

other_side = n_coins - count
if other_side >= count:
    print(f'Вам нужно перевенуть {count} монет')
else:
    print(f'Вам нужно перевенуть {other_side} монет')
    


