titulo = "Cadastros"
print(len(titulo) * "=")
print(titulo)
print(len(titulo) * "=")
i = 1
while True:
    try:
        quantidade = int(input("Digite a quantidade de cliente que você deseja fazer cadastro: "))
        break     
    except ValueError as e:
        print("Digite apenas valores numericos", e)
        continue
while i <= quantidade:
    nome = input(f"Digite o nome do {i}º cliente: ")
    while True:
        try:
            idade = int(input(f"Digite a idade do {i}º cliente: "))
            break
        except ValueError:
            print("Digite apenas valores numericos")
            continue
    email = input(f"Digite o email do {i}º cliente: ")
    print(f"Nome: {nome.capitalize()}\nIdade: {idade}\nEmail: {email}")
    i+=1