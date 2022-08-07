n = input().split(".")
if n[-1].startswith("0"):
    txt = n[-1][1:] + "." + n[0]
else:
    txt = n[-1] + "." + n[0]
print(txt)
