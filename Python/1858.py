dummy_input = input()

lst = list(map(int, input().split()))

print(lst.index(min(lst)) + 1)
