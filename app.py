def caracter(frase) -> str:
    letras = 0
    espaco = 0
    digito = 0
    for i in frase:
        if i.isalpha():
            letras += 1
        elif i == " ":
            espaco += 1
        elif i.isdigit():
            digito += 1
    print(f"Sua frase tem {len(frase)} caracteres, tem {letras} letras, tem {digito} digitos e tem {espaco} espaços vazios")
f = input("Digite uma frase:\n")
caracter(f)