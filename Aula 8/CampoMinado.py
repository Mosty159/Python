import random
from os import system
system("cls")
random.random()

def main():
    n_minas = int(input("Introduza o nº de minas: "))
    minas = []
    derrota = 0
    tabuleiro = [["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ["-", "-", "-", "-", "-", "-", "-", "-", "-"]]
    
    loc_minas = []
    cnt = 0
    while cnt < n_minas:
        col = random.randrange(0, 9)
        linha = random.randrange(0, 9)
        loc_minas.append([linha,col])
        cnt += 1
        
    i = 0
    while i < 9:
        j = 0
        minas.append([])
        while j < 9:                     
            minas[i].append(0)
            j += 1
        i += 1
    
    
    i = 0    
    while i < n_minas:
        minas[loc_minas[i][0]][loc_minas[i][1]] = "b"
        i += 1
    
    print(loc_minas)

    for i in range(0, n_minas):
            for j in range(0, n_minas): 
                    print(i,j)
                    if minas[i][j] == "b":
                        if j == 8:
                            i += 1
                            j = 0
                        else:
                            j += 1
                    else:
                        if i == 0:
                            if j == 0:
                                if minas[i+1][j] == "b":
                                    minas[i][j] += 1
                                elif minas[i+1][j+1] == "b":
                                    minas[i][j] += 1
                                elif minas[i][j+1] == "b":
                                    minas[i][j] += 1
                            elif j == 8:
                                if minas[i+1][j] == "b":
                                    minas[i][j] += 1
                                elif minas[i-1][j-1] == "b":
                                    minas[i][j] += 1
                                elif minas[i][j-1] == "b":
                                    minas[i][j] += 1
                            elif minas[i][j+1] == "b":
                                minas[i][j] += 1
                            elif minas[i][j-1] == "b":
                                minas[i][j] += 1
                            elif minas[i+1][j] == "b":
                                minas[i][j] += 1
                            elif minas[i+1][j-1] == "b":
                                minas[i][j] += 1
                            elif minas[i+1][j+1] == "b":
                                minas[i][j] += 1
                        else:
                            if j == 0:
                                if minas[i+1][j] == "b":
                                    minas[i][j] += 1
                                elif minas[i+1][j+1] == "b":
                                    minas[i][j] += 1
                                elif minas[i][j+1] == "b":
                                    minas[i][j] += 1
                            elif j == 8:
                                if minas[i+1][j] == "b":
                                    minas[i][j] += 1
                                elif minas[i-1][j-1] == "b":
                                    minas[i][j] += 1
                                elif minas[i][j-1] == "b":
                                    minas[i][j] += 1
                            elif minas[i][j+1] == "b":
                                minas[i][j] += 1
                            elif minas[i][j-1] == "b":
                                minas[i][j] += 1
                            elif minas[i+1][j] == "b":
                                minas[i][j] += 1
                            elif minas[i+1][j-1] == "b":
                                minas[i][j] += 1
                            elif minas[i+1][j+1] == "b":
                                minas[i][j] += 1
                            elif minas[i-1][j] == "b":
                                minas[i][j] += 1
                            elif minas[i-1][j-1] == "b":
                                minas[i][j] += 1
                            elif minas[i-1][j+1] == "b":
                                minas[i][j] += 1
                    
    
    while True:
        print("-------------------------------------------------------------")
        print("Insira a linha e coluna onde quer clicar: ")
        li = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        
        
        if minas[li - 1][coluna - 1] == "b":
            derrota += 1
            break
                
        print(minas)

        if derrota == 1:
            break
    print("Perdeste, boa sorte para a proxima")
main()