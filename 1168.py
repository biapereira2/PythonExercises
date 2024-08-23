testes=int(input())
dicionario = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
cont=0

if testes>=1 and testes<=2000:
    for i in range(testes):
        numero=str(input())
        for n in range(len(numero)):
            cont+=dicionario[numero[n]]
        print(f'{cont} leds')
        cont=0