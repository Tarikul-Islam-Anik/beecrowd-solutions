inter = gremio = empates = 0

while True:
    i, g = map(int, input().split())

    if i > g:
        inter += 1
    elif i < g:
        gremio += 1
    else:
        empates += 1

    print("Novo grenal (1-sim 2-nao)")
    n = int(input())
    if n == 2:
        break

print((inter + gremio + empates), "grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empates}")

if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
