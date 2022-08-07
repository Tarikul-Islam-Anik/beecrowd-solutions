while True:
    try:
        msg = input()
        blinked_blub = int(input())
        indexes = list(map(int, input().split()))
        for i in indexes:
            print(msg[i - 1], end="")
        print()
    except EOFError:
        break
