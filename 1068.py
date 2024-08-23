import os
os.system("cls")

def parenteses(expressao):

    cont_abre = 0 
    cont_fecha = 0 

    for quant in expressao:
        if quant == '(':
            cont_abre +=1

        elif quant == ')':
            if cont_abre <= cont_fecha:
                return print("incorrect")

            cont_fecha+=1


    if cont_fecha == cont_abre:
        return print("correct")
        
    else:
        return print("incorrect")


    

def main():
    while True:
        try:
            entrada = input()

            if entrada != ' ':
                parenteses(entrada)
        
        except EOFError:
            break

if __name__ == '__main__':
    main()
