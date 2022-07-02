count = option = 0
avg = 0.00
while True:
    x = float(input())
    if x > 10 or x < 0:
        print("nota invalida")
    else:
        count += 1
        avg += x
        if count == 2:
            print("media = %.2f" % (avg / 2))
            while True:
                print("novo calculo (1-sim 2-nao)")
                option = int(input())
                if option == 1:
                    count = option = 0
                    avg = 0.00
                    break
                elif option == 2:
                    break
    if option == 2:
        break
