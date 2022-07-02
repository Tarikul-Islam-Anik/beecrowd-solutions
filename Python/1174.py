nums = [float(input()) for _ in range(100)]

[print(f"A[{i}] = {float(v)}") for i, v in enumerate(nums) if v <= 10]
