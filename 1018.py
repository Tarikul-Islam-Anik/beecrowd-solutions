notes = int(input())
hundred = notes // 100
fifty = (notes % 100) // 50
twenty = ((notes % 100) % 50) // 20
ten = (((notes % 100) % 50) % 20) // 10
five = ((((notes % 100) % 50) % 20) % 10) // 5
two = (((((notes % 100) % 50) % 20) % 10) % 5) // 2
one = (((((notes % 100) % 50) % 20) % 10) % 5) % 2

print(notes)
print(f"{hundred} nota(s) de R$ 100,00")
print(f"{fifty} nota(s) de R$ 50,00")
print(f"{twenty} nota(s) de R$ 20,00")
print(f"{ten} nota(s) de R$ 10,00")
print(f"{five} nota(s) de R$ 5,00")
print(f"{two} nota(s) de R$ 2,00")
print(f"{one} nota(s) de R$ 1,00")
