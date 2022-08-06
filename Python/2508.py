def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    if len(str(sum)) > 1:
        return digit_sum(sum)
    else:
        return sum


pythagorean_table = {
    "AJS": 1,
    "BKT": 2,
    "CLU": 3,
    "DMV": 4,
    "ENW": 5,
    "FOX": 6,
    "GPY": 7,
    "HQZ": 8,
    "IR": 9,
}

while True:
    try:
        name = input()
        s = 0
        for i in name:
            for j in pythagorean_table:
                if i.upper() in j:
                    s += pythagorean_table[j]
        print(digit_sum(s))
    except EOFError:
        break
