start, end = map(int, input().split())

if end > start:
    print("O JOGO DUROU {} HORA(S)".format(end - start))
elif end < start:
    print("O JOGO DUROU {} HORA(S)".format(end + 24 - start))
else:
    print("O JOGO DUROU 24 HORA(S)")
