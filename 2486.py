import os
os.system("cls")

alimentos = {'suco de laranja': 120, 
            'morango fresco': 85, 
            'mamao': 85, 
            'goiaba vermelha': 70, 
            'manga': 56, 
            'laranja': 50, 
            'brocolis': 34}

def vitaminaC(N, nome):
    quantC = alimentos[nome] 
    return (N*quantC)
    
def consumo_recomendado(ingestao):
    if ingestao >=110 and ingestao<=130:
        return print(f'{ingestao} mg')
    
    if ingestao > 130:
        return print(f'Menos {ingestao - 130} mg')
    
    if ingestao < 110:
        return print(f'Mais {110 - ingestao} mg')


def main():
    valorT = int(input())

    while valorT != 0:
        ingestao_total = 0
        
        for i in range(valorT):
            alimento = input().split(" ", 1)
            ingestao_total += vitaminaC(int(alimento[0]), alimento[1])

        consumo_recomendado(ingestao_total)

        valorT = int(input())

        

if __name__ == "__main__":
    main()
