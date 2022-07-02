total_distance = 0

for i in range(int(input())):
    t, v = map(int, input().split())
    total_distance += t * v

print(total_distance)
