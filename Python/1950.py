x = input()


if x.startswith("-"):
    x = float(x)
    print("{:.4E}".format(x))
else:
    x = float(x)
    print("+{:.4E}".format(x))
