import random


def roulette_wheel_selection():
    x = random.random()
    if x < 0.8:
        return "Move forward"
    elif x < 0.9:
        return "Turn left"
    else:
        return "Turn right"


# Test the roulette wheel
for _ in range(10):
    print(roulette_wheel_selection())
