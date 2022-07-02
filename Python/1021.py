notes = float(input())
hundred = notes // 100
fifty = (notes % 100) // 50
twenty = ((notes % 100) % 50) // 20
ten = (((notes % 100) % 50) % 20) // 10
five = ((((notes % 100) % 50) % 20) % 10) // 5
two = (((((notes % 100) % 50) % 20) % 10) % 5) // 2


one = (((((notes % 100) % 50) % 20) % 10) % 5) % 2
half = ((one - 1) * 100) // 50
quarter = (((one - 1) * 100) % 50) // 25
dime = ((((one - 1) * 100) % 50) % 25) // 10
nickel = (((((one - 1) * 100) % 50) % 25) % 10) // 5
penny = (((((one - 1) * 100) % 50) % 25) % 10) % 5

print("NOTAS:")
print(f"{int(hundred)} nota(s) de R$ 100.00")
print(f"{int(fifty)} nota(s) de R$ 50.00")
print(f"{int(twenty)} nota(s) de R$ 20.00")
print(f"{int(ten)} nota(s) de R$ 10.00")
print(f"{int(five)} nota(s) de R$ 5.00")
print(f"{int(two)} nota(s) de R$ 2.00")
print("MOEDAS:")
if half > 0:
    print(f"{int(one)} moeda(s) de R$ 1.00")
    print(f"{int(half)} moeda(s) de R$ 0.50")
    print(f"{int(quarter)} moeda(s) de R$ 0.25")
    print(f"{int(dime)} moeda(s) de R$ 0.10")
    print(f"{int(nickel)} moeda(s) de R$ 0.05")
    print(f"{int(penny)} moeda(s) de R$ 0.01")
else:
    print(f"{0} moeda(s) de R$ 1.00")
    print(f"{0} moeda(s) de R$ 0.25")
    print(f"{0} moeda(s) de R$ 0.50")
    print(f"{0} moeda(s) de R$ 0.10")
    print(f"{0} moeda(s) de R$ 0.05")
    print(f"{0} moeda(s) de R$ 0.01")
