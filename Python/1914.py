for i in range(int(input())):
    p1, o1, p2, o2 = input().split()
    s = sum(map(int, input().split()))
    if o1.startswith("P"):
        if s % 2 == 0:
            print(p1)
        else:
            print(p2)
    else:
        if s % 2 == 0:
            print(p2)
        else:
            print(p1)
