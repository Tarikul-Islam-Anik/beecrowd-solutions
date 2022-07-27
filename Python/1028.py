def stack(f1, f2):
    return f1 if not f2 else stack(f2, f1 % f2)


for i in range(int(input())):
    f1, f2 = map(int, input().split())
    print(stack(f1, f2))
