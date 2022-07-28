p, n = map(int, input().split())

h = list(map(int, input().split()))

for i in range(n - 1):
    if abs(h[i] - h[i + 1]) <= p:
        continue
    else:
        print("GAME OVER")
        break
else:
    print("YOU WIN")
