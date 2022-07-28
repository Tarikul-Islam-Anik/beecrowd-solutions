for i in range(3):
    n = 0
    while True:
        wink = input()
        if wink != "caw caw":
            n += int(wink.replace("-", "0").replace("*", "1"), 2)
        else:
            print(n)
            break
