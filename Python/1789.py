while True:
    try:
        n = input()
        speed = max(list(map(int, input().split())))
        if speed < 10:
            print(1)
        elif 10 <= speed < 20:
            print(2)
        elif 20 <= speed:
            print(3)

    except EOFError:
        break
