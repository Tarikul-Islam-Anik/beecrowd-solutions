idx = int(input())
task = input()

matrix = []
for i in range(12):
    rows = []
    for i in range(12):
        rows.append(float(input()))
    matrix.append(rows)


if task == "S":
    print(sum(matrix[idx]))
elif task == "M":
    print(f"{sum(matrix[idx])/12:.1f}")
