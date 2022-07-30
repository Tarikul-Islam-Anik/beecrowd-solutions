while True:
    try:
        degree = int(input())
        degree %= 360
        if degree >= 0 and degree < 90:
            print("Bom Dia!!")
        elif degree >= 90 and degree < 180:
            print("Boa Tarde!!")
        elif degree >= 180 and degree < 270:
            print("Boa Noite!!")
        elif degree >= 270 and degree < 360:
            print("De Madrugada!!")
    except EOFError:
        break
