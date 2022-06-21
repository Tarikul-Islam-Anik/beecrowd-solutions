loop = int(input())

for i in range(loop):
    a, b, c = map(float, input().split(" "))
    a, b, c = a * 2, b * 3, c * 5
    print(f"{(a+b+c)/10:.1f}")
