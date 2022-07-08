for i in range(int(input(""))):
    a, b = input().split()
    if a == b:
        result = "De novo!"
    elif a == "pedra":
        if b == "tesoura" or b == "lagarto":
            result = a
        else:
            result = b
    elif a == "papel":
        if b == "pedra" or b == "Spock":
            result = a
        else:
            result = b
    elif a == "tesoura":
        if b == "lagarto" or b == "papel":
            result = a
        else:
            result = b
    elif a == "lagarto":
        if b == "Spock" or b == "papel":
            result = a
        else:
            result = b
    elif a == "Spock":
        if b == "tesoura" or b == "pedra":
            result = a
        else:
            result = b
    if result == a:
        result = "Bazinga!"
    elif result == b:
        result = "Raj trapaceou!"
    print(f"Caso #{i+1}: {result}")
