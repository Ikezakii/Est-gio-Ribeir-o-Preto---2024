palavra = str(input("Digite uma palavra: "))


for letra in palavra[: : -1]:
    print(letra,end="")
