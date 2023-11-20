from os import system
import random
random.random()
system("cls")
j = int(input("Queres jogar jogador vs jogador ou jogador vs maquina(1 se for jogador, 0 para maquina)"))
if j == 1:
    palavra = str(input("Jogador 1 introduza uma palavra para o jogador 2 descobrir:"))
    pala = []
    cnt = 0
    win = 0
    tenrest = 10
    for cnt in range(len(palavra)):
        pala.append("_")

    print(pala)

    i = 0

    while i < 10:
        print("----------------------------------------------")
        tentativa = str(input("Jogador 2 insira um caracter:"))

        cnt = 0
        while cnt < len(palavra):
            if palavra[cnt] == tentativa:
                pala[cnt] = tentativa
            cnt += 1

        cnt = 0
        vitoria = 0
        while cnt < len(pala):
            if pala[cnt] != "_":
                vitoria += 1
            cnt += 1

        tenrest -= 1
        print("Tens", tenrest, "tentativas ainda")
        print(pala)

        if vitoria == len(pala):
            print("PARABÉNS ACERTASTE A PALAVRA")
            win = 1
            break

    
        i += 1
        
    if win == 0:
        print("-----------------------------------------------------")
        print("Perdeste, não conseguis te acertar a palavra a tempo, a palavra era", palavra)
elif j == 0:
    listapalavras = ["dado", "cao", "banana", "computador", "janela", "caneta", "montanha", "gelado", "praia", "livro",
        "foguete", "espelho", "chave", "agua", "cadeira", "aviao", "piano", "sapato", "arvore", "bola",
        "telefone", "lapis", "sol", "lua", "mar", "terra", "espada", "tesouro", "fada", "bruxa"]
    x = random.randrange(1, 31)
    palavra = listapalavras[x]
    pala = []
    cnt = 0
    win = 0
    tenrest = 10
    for cnt in range(len(palavra)):
        pala.append("_")

    print(pala)

    i = 0

    while i < 10:
        print("----------------------------------------------")
        tentativa = str(input("Jogador insira um caracter:"))

        cnt = 0
        while cnt < len(palavra):
            if palavra[cnt] == tentativa:
                pala[cnt] = tentativa
            cnt += 1

        cnt = 0
        vitoria = 0
        while cnt < len(pala):
            if pala[cnt] != "_":
                vitoria += 1
            cnt += 1

        tenrest -= 1
        print("Tens", tenrest, "tentativas ainda")
        print(pala)

        if vitoria == len(pala):
            print("PARABÉNS ACERTASTE A PALAVRA")
            win = 1
            break

    
        i += 1
        
    if win == 0:
        print("-----------------------------------------------------")
        print("Perdeste, não conseguis te acertar a palavra a tempo, a palavra era", palavra)
else:
    print("Nº invalido")