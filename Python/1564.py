while True:
    try:
        if int(input()) == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break
