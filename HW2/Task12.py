# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input("Назовите сумму загаданных чисел: "))
P = int(input("Назовите произведедние загадданых чисел: "))

for x in range(1, 1001):
    for y in range(1, 1001):
        if x + y == S and x * y == P:
            print(f"Задуманные числа: {x} и {y}")
            break
    else:
        continue
    break