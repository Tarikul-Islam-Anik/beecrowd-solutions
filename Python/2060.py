n = input()

nums = list(map(int, input().split()))

multiple_of_two = 0
multiple_of_three = 0
multiple_of_four = 0
multiple_of_five = 0

for i in nums:
    if i % 2 == 0:
        multiple_of_two += 1
    if i % 3 == 0:
        multiple_of_three += 1
    if i % 4 == 0:
        multiple_of_four += 1
    if i % 5 == 0:
        multiple_of_five += 1

print(multiple_of_two, "Multiplo(s) de 2")
print(multiple_of_three, "Multiplo(s) de 3")
print(multiple_of_four, "Multiplo(s) de 4")
print(multiple_of_five, "Multiplo(s) de 5")
