def fibonacci(n):
    prev_num = 0
    next_num = 1
    result = []
    for i in range(n):
        result.append(prev_num)
        temp = prev_num
        prev_num = next_num
        next_num = temp + next_num
    return result


print(*fibonacci(int(input())))
