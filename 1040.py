n1, n2, n3, n4 = map(float, input().split())

avg = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print("Media: {:.1f}".format(avg))
if avg >= 7:
    print("Aluno aprovado.")
elif avg >= 5:
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame: {:.1f}".format(n5))
    print("Aluno aprovado.")
    print("Media final: {:.1f}".format((avg + n5) / 2))
elif avg < 5:
    print("Aluno reprovado.")
