for i in range(int(input())):
    year = int(input())
    if year > 2015:
        print(year - 2014, "A.C.")
    elif year < 2015:
        print(2015 - year, "D.C.")
    else:
        print("1 A.C.")
