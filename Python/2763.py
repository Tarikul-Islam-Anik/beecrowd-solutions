while True:
    try:
        cpf = input().replace("-", ".").split(".")
        [print(i) for i in cpf]
    except EOFError:
        break
