while True:
    data = input()
    if data.startswith("0"):
        break
    else:
        a, b, c = map(int, data.split())
        if c == 100:
            print(int(__import__("math").sqrt(a * b)))
        else:
            print(int(__import__("math").sqrt((a * b) / (c / 100))))
