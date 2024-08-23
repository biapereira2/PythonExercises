cod = ''
quantidade=int(input())

for i in range(quantidade):
    frase=input()
    for f in range(len(frase)):
        if frase[f]!=' ' and f==0:
            cod+=frase[f]
        elif frase[f-1]==' ' and frase[f]!=' ':
            cod+=frase[f]
    print(cod)
    cod = ''