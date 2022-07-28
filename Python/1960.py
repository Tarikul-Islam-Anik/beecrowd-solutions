def to_roman_numeral(n):
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    result = ""
    for i in range(len(ints)):
        count = int(n / ints[i])
        result += nums[i] * count
        n -= ints[i] * count
    return result


print(to_roman_numeral(int(input())))
