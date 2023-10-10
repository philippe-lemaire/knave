from random import randint


def roll(dice):
    dice = dice.lower()
    if dice[0].isdigit():
        n, size = dice.split("d")
        n = int(n)
        size = int(size)
    elif dice[0] == "d":
        size = int(dice[1:])
        n = 1
    result = 0
    for _ in range(n):
        result += randint(1, size)
    return result
