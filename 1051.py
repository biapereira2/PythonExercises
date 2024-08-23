import os
os.system("cls")

def imposto_de_2k(renda):
    renda=renda-2000
    imposto=renda*0.08
    return imposto

def imposto_de_3k(renda):
    renda=renda-3000
    imposto=renda*0.18
    return imposto

def imposto_de_4_5k(renda):
    renda=renda-4500
    imposto=renda*0.28
    return imposto



def calculo_IR(renda):

    if renda>=0 and renda<=2000:
        return("Isento")

    elif renda>4500:
        imposto_total = imposto_de_4_5k(renda) + imposto_de_3k(4500) + imposto_de_2k(3000)
        
    elif renda>=3000.01 and renda<=4500:
        imposto_total = imposto_de_3k(renda) + imposto_de_2k(3000)

    elif renda>=2000.01 and renda<=3000:
        imposto_total = imposto_de_2k(renda)
    
    return imposto_total

def main():

    salario=float(input())

    if calculo_IR(salario) == "Isento":
        print(calculo_IR(salario))
    else:
        print(f"R$ {format(calculo_IR(salario), '.2f')}")

if __name__ == "__main__":
    main()