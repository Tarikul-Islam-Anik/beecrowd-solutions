nums = []
for i in range(20):
    nums.append(int(input()))

for i in range(-1, -21, -1):
    print(f"N[{abs(i+1)}] = {nums[i]}")
