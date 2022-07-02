point_a = [float(i) for i in input().split(" ")]
point_b = [float(i) for i in input().split(" ")]
distance = ((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2) ** 0.5
print("{:.4f}".format(distance))
