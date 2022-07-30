while True:
    try:
        v = float(input())
        d = float(input()) / 2
        print(f"ALTURA = {v/(3.14*d**2):.2f}")
        print(f"AREA = {3.14*d**2:.2f}")

    except EOFError:
        break
