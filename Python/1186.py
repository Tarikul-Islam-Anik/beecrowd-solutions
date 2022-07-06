task = input()

matrix = []
for i in range(12):
    rows = []
    for i in range(12):
        rows.append(float(input()))
    matrix.append(rows)

s = 0
count = 0
idx = 11

for i in range(1, 12):
    for j in range(idx, 12):
        s += matrix[i][j]
        count += 1
    idx -= 1

if task == "S":
    print(s)
elif task == "M":
    print(f"{s/count:.1f}")
