def leitura(lista):
    i = 0

    while i < 10:

        x = int(input("Introduza um nº: "))

        lista.append(x)

        i += 1
    return lista


def maior_menor(lista):
    cnt = 0
    maior = " "
    menor = " "

    while cnt < 10:
        if menor == " ":
            menor = lista[cnt]

        if maior == " ":
            maior = lista[cnt]
        
        if menor > lista[cnt]:
            menor = lista[cnt]
        
        if maior < lista[cnt]:
            maior = lista[cnt]

        cnt += 1

    dif = maior - menor 

    return dif

def par_impare(lista):
    cnt = 0
    par = 0
    imp = 0

    while cnt < 10:
        if lista[cnt] % 2 == 0:
            par += 1
        else:
            imp += 1
        
        cnt += 1
    
    return par, imp
        


lis = []
dif = 0
pares_impares = 0

leitura(lis)
dif = maior_menor(lis)
pares_impares = par_impare(lis)


print ("Valores do vetor:",lis)
print ("Diferença entra o maior e menor do vetor: ",dif)
print ("Nº de pares e impares do vetor: ", pares_impares)

