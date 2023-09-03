import random

def count_min_flips(coins):
    heads = coins.count("H")
    tails = coins.count("T")
    
    return min(heads, tails)

def flip_coins(n):
    coins = ["H", "T"] * n 
    random.shuffle(coins)
    
    print("Исходное расположение монеток:", coins)
    
    min_flips = count_min_flips(coins)
    
    return min_flips

n = int(input("Введите количество монеток: "))
min_flips = flip_coins(n)
print("Минимальное количество переворотов:", min_flips)