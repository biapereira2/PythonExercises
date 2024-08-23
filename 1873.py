testes = int(input())
dicionario = {
    'papel': ['pedra', 'spock'], 
    'tesoura': ['papel','lagarto'], 
    'pedra': ['lagarto','tesoura'], 
    'lagarto': ['spock','papel'],
    'spock': ['tesoura', 'pedra']
}

for i in range(testes):
    isRajeshWinner = False

    escolha=input().split()
    if escolha[0] == escolha[1]:
        print("empate")
    else:
        rajesh = dicionario[escolha[0]]

        sheldon = dicionario[escolha[1]]

        for r in rajesh:
            if r == escolha[1]:
                isRajeshWinner = True

        if isRajeshWinner:
            print('rajesh')

        else:
            print('sheldon')