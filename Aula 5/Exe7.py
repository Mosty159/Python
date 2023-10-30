def nome(nome):
    x = nome.split()

    c = " "
    cnt = 0

    if len(x) >= 2:
        ul = x[-1]
        for cnt in range(len(x) - 1):
            c = c + x[cnt] + " "
            
        c = ul + "," + c
    else:
        c = nome
   
    return c

nom = str(input("Introduza um nome: "))
r = nome(nom)
print(r)
