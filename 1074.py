loop = int(input())

for i in range(loop):
    n = int(input())
    if n == 0:
        print("NULL")
    elif n % 2 == 0 and n > 0:
        print("EVEN POSITIVE")
    elif n % 2 == 0 and n < 0:
        print("EVEN NEGATIVE")
    elif n % 2 == 1 and n > 0:
        print("ODD POSITIVE")
    elif n % 2 == 1 and n < 0:
        print("ODD NEGATIVE")
