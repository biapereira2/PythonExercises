teste = int(input())


for i in range(teste):
    valorTotal = 0 
    linhas = int(input())
    matriz = [[]]

    for l in range(linhas):
        letras = input()

        for index in range(len(letras)):
            valorTotal+= ord(letras[index])-65 + l + index

    print(valorTotal)
