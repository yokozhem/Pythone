# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума

def find_indexes(lst, minimum, maximum):
    indexes = []
    for i in range(len(lst)):
        if minimum <= lst[i] <= maximum:
            indexes.append(i)
    return indexes

lst = [2, 5, 8, 3, 9, 1, 7, 4, 6]
minimum = 3
maximum = 7
indexes = find_indexes(lst, minimum, maximum)
print(indexes)  # [1, 3, 6, 7]
