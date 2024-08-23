import os
os.system("cls")

def triangulos(a, b, c):
    if a >= (b + c):
        return print("NAO FORMA TRIANGULO")
    
    if (a * a) == ((b * b) + (c * c)):
        print("TRIANGULO RETANGULO")

    if (a * a) > ((b * b) + (c * c)):
        print("TRIANGULO OBTUSANGULO")

    if (a * a) < ((b * b) + (c * c)):
        print("TRIANGULO ACUTANGULO")

    if a == b and a == c:
        print("TRIANGULO EQUILATERO")

    if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        print("TRIANGULO ISOSCELES")

def main():
    valores = (input().split())
    valores = [float(x) for x in valores]

    valores.sort(reverse = True )

    valorA = valores[0]
    valorB = valores[1]
    valorC = valores[2]

    (triangulos(valorA, valorB, valorC))

if __name__ == "__main__":
    main()