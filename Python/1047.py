h1, m1, h2, m2 = list(map(int, input().split()))
if h2 > h1 or (h2 == h1 and m2 > m1):
    hour_difference = h2 - h1
else:
    hour_difference = (h2 - h1) + 24
if m2 < m1:
    hour_difference -= 1
    minute_difference = (m2 - m1) + 60
else:
    minute_difference = m2 - m1

print("O JOGO DUROU ", hour_difference, " HORA(S) E ", minute_difference, " MINUTO(S)", end="\n")
