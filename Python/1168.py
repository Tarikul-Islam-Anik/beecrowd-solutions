leds = {
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6,
}

for i in range(int(input())):
    n = input()
    print(sum(leds[x] for x in n), "leds")
