def procurar(lista, pro):
   
    encon = " "
    
    cnt = 0

    for cnt in range(len(lista)):
        if pro == lista[cnt]:
                encon = lista.index(pro)
                break
        else:
            encon = " "



    if encon != " ":
          encon = True
    else:
          encon = False

    return encon


cnt = 0

i = int(input("Introduza o nº de números que quer inserir na lista: "))

lis = []

for cnt in range(i):

        x = int(input("Introduza um nº: "))

        lis.append(x)

proc = int(input("Introduza o nº que quer procurar na lista: "))

encontrado = procurar(lis, proc)

print(encontrado)
