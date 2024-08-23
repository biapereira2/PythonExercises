cha = int(input())
certos = 0
resposta = (input().split())

if cha>=1 and cha<=4:
    for i in resposta:
        if int(i)==cha:
            certos+=1

print(certos)