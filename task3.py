def powers_of_two(n):
    powers = []
    k = 0
    power = 1

    while power <= n:
        powers.append(power)
        k += 1
        power = 2 ** k

    return powers

number = int(input("Введите число N: "))

result = powers_of_two(number)

print("Целые степени двойки, не превосходящие", number, ":")
for num in result:
    print(num)