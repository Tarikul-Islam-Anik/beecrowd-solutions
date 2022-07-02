task = input()

matrix = []
for i in range(12):
    rows = []
    for i in range(12):
        rows.append(float(input()))
    matrix.append(rows)

s = 0
count = 0
start_idx = 1
end_idx = 11

for i in range(5):
    for j in range(start_idx, end_idx):
        s += matrix[i][j]
        count += 1
    start_idx += 1
    end_idx -= 1

if task == "S":
    print(f"{s:.1f}")
elif task == "M":
    print(f"{s/count:.1f}")
