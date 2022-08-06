for i in range(int(input())):
    s1, s2 = input().split()
    s3 = ""
    remaining = ""
    if len(s1) > len(s2):
        size = len(s2)
        remaining = s1[size:]
    else:
        size = len(s1)
        remaining = s2[size:]
    for j in range(size):
        s3 += s1[j]
        s3 += s2[j]
    s3 += remaining
    print(s3)
