def ordenar(lista):
    i = 0

    j = int(input("Introduza o nº de números que quer inserir na lista: "))

    while i < j:

        x = int(input("Introduza um nº: "))

        lista.append(x)

        i += 1

    lista.sort()
    return lista

lis = []

lis = ordenar(lis)

print("Lista ordenada do menor para o maior: ", lis)
