salary = float(input())

if salary <= 400.00:
    new_salary = salary * 1.15
    percentage = 15
elif 400.01 <= salary <= 800.00:
    new_salary = salary * 1.12
    percentage = 12
elif 800.01 <= salary <= 1200.00:
    new_salary = salary * 1.10
    percentage = 10
elif 1200.01 <= salary <= 2000.00:
    new_salary = salary * 1.07
    percentage = 7
else:
    new_salary = salary * 1.04
    percentage = 4

readjusted_salary = new_salary - salary

print("Novo salario: {:.2f}".format(new_salary))
print("Reajuste ganho: {:.2f}".format(readjusted_salary))
print("Em percentual: {} %".format(percentage))
