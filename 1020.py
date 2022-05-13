days = int(input())
years = days // 365
months = (days % 365) // 30
days = (days % 365) % 30
print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
