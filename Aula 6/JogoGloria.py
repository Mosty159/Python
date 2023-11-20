def desenhar_t(lista):
    cnt = 0
    desenha = "[Inicio]"
    while cnt <= 80 :
        desenha = desenha + "["+ lista[cnt] + "]"+ "["+ lista[cnt + 1] + "]" + "["+ lista[cnt + 2] + "]"+"["+ lista[cnt + 3] + "]"+"["+ lista[cnt + 4] + "]"+"["+ lista[cnt + 5] + "]"+"["+ lista[cnt + 6] + "]"+"["+ lista[cnt + 7] + "]"+ "["+ lista[cnt + 8] + "]"+ "["+ lista[cnt + 9] + "] \n"
        cnt += 10

    print(desenha)

import random
from os import system
system("cls")
def main():
    print("-----REGRAS-----")
    print("Passáro - Avança 9 casas e se na primeira rodada conseguir um 3 e 6 ganha logo mas se conseguir um 5 e um 4 avança para a casa 15")
    print("Ponte, Caminho de ferro e Estalagem - Fica uma rodada sem jogar")
    print("Carro, Vapor - Fica 2 rodadas sem jogar")
    print("Caranguejo -  Recua o nº de casas que avançou e caso cai na casa passáro recua mais 9 casa")
    print("Poço - O jogador fica nesta casa até todos tiverem o ultropassado ou chegar alguem nas mesma casa que ele")
    print("Morte - Remove o jogador de jogo fazendo com que a lista de jogadores mude(ex: o jogador 2 cai na casa Morte então o jogador 3 passa a ser o jogador 2)")
    print("Inferno - Faz com que o jogador volta a casa 1")
    print("Purgatório - O jogador fica preso nessa casa até alguem chegar para trocar com ele")
    print("----------------")
    n_jogadores = int(input("Introduza o número de jogadores(Minímo de 2 jogadores e Máximo de 6):"))

    if n_jogadores >= 2 and n_jogadores <= 6:
        jogadores = []
        vez_jogador = []
        jogador = []
        voltas = 1
        vitoria = 0
        jogadorpoco = 0
        aux = 0 
        i = 1
        while i <= n_jogadores:
            jogadores.append(0)
            jogador.append(i)
            vez_jogador.append("0")
            i += 1     
        random.random()
        tabuleiro = []
        cnt = 1
        
        while cnt <= 90:
            if cnt == 90:
                tabuleiro.append("Glória")
            elif cnt == 5:
                tabuleiro.append("Ponte")
            elif cnt == 14:
                tabuleiro.append("Carro")
            elif cnt == 23:
                tabuleiro.append("Caminho de Ferro")
            elif cnt == 32:
                tabuleiro.append("Vapor")
            elif cnt == 41:
                tabuleiro.append("Estalagem")
            elif cnt == 50:
                tabuleiro.append("Caranguejo")
            elif cnt == 59:
                tabuleiro.append("Poço")
            elif cnt == 68:
                tabuleiro.append("Morte")
            elif cnt == 77:
                tabuleiro.append("Inferno")
            elif cnt == 86:
                tabuleiro.append("Purgatório")
            elif cnt % 9 == 0:
                tabuleiro.append("Passáro")
            else:
                tabuleiro.append(str(cnt))
            
            cnt += 1  
                  
        i = 0             
        jogadores[2] = 58
        jogadores[3] = 57

        while True:
                if vez_jogador[i] == "0":
                    print("-------------------------------------------------------------------------------------------------------------")
                    print("É a vez do jogador ", jogador[i])
                    input()
                    dado1 = 1#random.randrange(1, 7)
                    dado2 = 0#random.randrange(1,7)    
                    print("Conseguiu avançar:", dado1 + dado2,"casas")
                    jogadores[i] = jogadores[i] + (dado1 + dado2)
                    if jogadores[i] >= 90:
                        print("O JOGADOR", jogador[i], "GANHOU")
                        print("Chegandoo à casa: Glória")
                        vitoria = "win"
                        break
                    print("Chegando à casa:", tabuleiro[jogadores[i] - 1])     

                    if tabuleiro[jogadores[i] - 1] == "Passáro" and voltas == 1:
                        if dado1 == 6 or dado2 == 6:
                            print("O JOGADOR", jogador[i], "GANHOU")
                        elif dado1 == 5 or dado2 == 5:
                            jogadores[i] = 15
                
                
                    if tabuleiro[jogadores[i] - 1] == "Passáro":
                        jogadores[i] = jogadores[i] + 9  
                    elif tabuleiro[jogadores[i] - 1] == "Ponte" or tabuleiro[jogadores[i] - 1] == "Caminho de Ferro" or tabuleiro[jogadores[i] - 1] == "Estalagem" :
                        vez_jogador[i] = 1
                    elif tabuleiro[jogadores[i] - 1] == "Carro" or tabuleiro[jogadores[i] - 1] == "Vapor" :
                        vez_jogador[i] = 2    
                    elif tabuleiro[jogadores[i] - 1] == "Caranguejo":
                        jogadores[i] = jogadores[i] - (dado1 + dado2)
                        if tabuleiro[jogadores[i] - 1] == "Passáro":
                            jogadores[i] = jogadores[i] - 9
                    elif tabuleiro[jogadores[i] - 1] == "Poço":
                        vez_jogador[i] = "poço"                 
                    elif tabuleiro[jogadores[i] - 1] == "Inferno":
                        jogadores[i] = 1
                    elif tabuleiro[jogadores[i] - 1] == "Purgatório":
                        vez_jogador[i] = "pur"
                        

                    if jogadores[i] >= 90:
                        print("O JOGADOR", jogador[i], "GANHOU")
                        print("Chegandoo à casa: Glória")
                        break
                        
                elif vez_jogador[i] == "poço":
                    cnt = 0
                    jogadorpoco = 0                
                    while cnt < n_jogadores:
                        if i != cnt:
                            if jogadores[i] < jogadores[cnt]:
                                jogadorpoco += 1
                                if jogadorpoco == (n_jogadores - 1):
                                    vez_jogador[i] = "0"
                            elif jogadores[i] == jogadores[cnt]:
                                    vez_jogador[i] = "0"
                                    
                        cnt += 1
                        
                elif vez_jogador[i] == "pur":
                    cnt = 0
                    while cnt < n_jogadores:
                        if i != cnt:
                            if jogadores[i] == jogadores[cnt]:
                                vez_jogador[i] = "0"
                        cnt += 1
                else:
                    vez_jogador[i] -= 1   
                    if vez_jogador[i] == 0:
                        vez_jogador[i] = "0"       
                            
                if vitoria == "win":
                    break    

                if tabuleiro[jogadores[i] - 1] == "Caranguejo":
                        jogadores[i] = jogadores[i] - (dado1 + dado2)
                        if tabuleiro[jogadores[i] - 1] == "Passáro":
                            jogadores[i] = jogadores[i] - 9             
                            
                i += 1    
                if i == len(jogadores):
                    print("-------------------------------------------------------------------------------------------------------------")
                    i = 0
                    cnt = 0
                    j = 0

                    while j < len(jogadores):
                        if tabuleiro[jogadores[j] - 1] == "Morte":
                            jogadores.pop(j) 
                        j += 1
                    print("Resultados da ",voltas,"ª rodada")
                    for cnt in range(len(jogadores)):
                        if jogadores[cnt] == 90:
                            aux = ("Glória")
                        elif jogadores[cnt] == 5:
                            aux = ("Ponte")
                        elif jogadores[cnt] == 14:
                            aux = ("Carro")
                        elif jogadores[cnt] == 23:
                            aux = ("Caminho de Ferro")
                        elif jogadores[cnt] == 32:
                            aux = ("Vapor")
                        elif jogadores[cnt] == 41:
                            aux = ("Estalagem")
                        elif jogadores[cnt] == 50:
                            aux = ("Caranguejo")
                        elif jogadores[cnt] == 59:
                            aux = ("Poço")
                        elif jogadores[cnt] == 68:
                            aux = ("Morte")
                        elif jogadores[cnt] == 77:
                            aux = ("Inferno")
                        elif jogadores[cnt] == 86:
                            aux = ("Purgatório")
                        elif jogadores[cnt] % 9 == 0:
                            aux = ("Passáro")
                        else:
                            aux = jogadores[cnt]
                        print("Jogador", jogador[cnt], ":", aux)  
                    desenhar_t(tabuleiro) 
                    voltas += 1
    else:
        print("Não pode jogar com essa quantidade de jogadores")
main()