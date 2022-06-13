h1, m1, h2, m2 = map(int, input().split())

if h2 > h1:
    if m2 > m1:
        print(f"O JOGO DUROU {h2-h1} HORA(S) E {m2-m1} MINUTO(S)")
    else:
        print(f"O JOGO DUROU {h2-h1-1} HORA(S) E {60+m2-m1} MINUTO(S)")
elif h2 == h1:
    if m2 > m1:
        print(f"O JOGO DUROU {h2-h1} HORA(S) E {m2-m1} MINUTO(S)")
    elif m2 == m1:
        print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        print(f"O JOGO DUROU 23 HORA(S) E {60-m1+m2} MINUTO(S)")
