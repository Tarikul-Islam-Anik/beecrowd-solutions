idx = int(input())
task = input()

matrix = []
for i in range(12):
    rows = []
    for i in range(12):
        rows.append(float(input()))
    matrix.append(rows)


s = sum([i[idx] for i in matrix])

if task == "S":
    print(s)
elif task == "M":
    print(f"{s/12:.1f}")
