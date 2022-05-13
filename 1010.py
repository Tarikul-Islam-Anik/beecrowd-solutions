product_1 = input().split(" ")[1:]
product_2 = input().split(" ")[1:]
total = (int(product_1[0]) * float(product_1[1])) + (
    int(product_2[0]) * float(product_2[1])
)
print("VALOR A PAGAR: R$ {:.2f}".format(total))
