for i in range(int(input())):
    txt = input().split()
    print(" ".join(sorted(txt, key=len, reverse=True)))
