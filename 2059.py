import os
os.system("cls")

def soma(n1, n2, par, roubo, acusou):

    n1 = int(n1)
    n2 = int(n2)
    par = int(par)
    roubo = int(roubo)
    acusou = int(acusou)

    soma = n1+n2

    if roubo == 1 and acusou == 0:
        return("Jogador 1 ganha!")
    
    if roubo == 1 and acusou == 1:
        return("Jogador 2 ganha!")
    
    if roubo == 0 and acusou == 1:
        return("Jogador 1 ganha!")
    
    if roubo == 0 and acusou == 0:
        
        if par == 1 and soma%2 == 0:
            return("Jogador 1 ganha!")
        
        if par == 0 and soma%2 != 0:
            return("Jogador 1 ganha!")
        
        if par == 0 and soma%2 == 0:
            return("Jogador 2 ganha!")
        
        if par == 1 and soma%2 != 0:
            return("Jogador 2 ganha!")
    
def main():
    valores = input().split()

    p = valores[0]
    j1 = valores[1]
    j2 = valores[2]
    r = valores[3]
    a = valores[4]

    print(soma(j1, j2, p, r, a))

if __name__ == "__main__":
    main()