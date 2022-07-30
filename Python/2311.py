for i in range(int(input())):
    name = input()
    multi = float(input())
    scores = list(map(float, input().split()))
    scores.sort()
    print(name, f"{sum(scores[1:-1])*multi:.2f}")
