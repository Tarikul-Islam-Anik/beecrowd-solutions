name = input()
salary = float(input())
sales = float(input())

total = salary + (sales * 0.15) if sales > 0 else salary

print("TOTAL = R$ {:.2f}".format(total))
