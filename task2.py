def find_numbers(s, p):
    for x in range(1, 1001):
        y = s - x
        if x * y == p:
            return x, y

sum_hint = int(input("Введите сумму чисел: "))
product_hint = int(input("Введите произведение чисел: "))

result = find_numbers(sum_hint, product_hint)

if result:
    print(f"Задуманные числа Петей: {result[0]} и {result[1]}")
else:
    print("Не удалось найти числа, соответствующие подсказкам.")