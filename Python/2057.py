times = list(map(int, input().split()))

print((24 + sum(times)) % 24) if sum(times) < 0 else print(sum(times) % 24)
