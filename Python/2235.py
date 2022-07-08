n1, n2, n3 = map(int, input().split())

if n1 - n2 == 0:
    print("S")
elif n1 - n3 == 0:
    print("S")
elif n2 - n3 == 0:
    print("S")
elif (n1 + n2) - n3 == 0:
    print("S")
elif (n1 + n3) - n2 == 0:
    print("S")
elif (n2 + n3) - n1 == 0:
    print("S")
else:
    print("N")
