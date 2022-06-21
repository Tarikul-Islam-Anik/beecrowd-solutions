n = int(input())

nums = list(map(int, input().split()))

print("Menor valor:", min(nums))
print("Posicao:", nums.index(min(nums)))
