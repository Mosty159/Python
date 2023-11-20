from os import system
system("cls")

palavra = str(input("Jogador 1 introduza uma palavra para o jogador 2 descobrir:"))
pala = []
cnt = 0
for cnt in range(len(palavra)):
    pala.append("_")

print(pala)

i = 0

while i < 6:
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

    if vitoria == len(pala):
        print("PARABÉNS ACERTASTE A PALAVRA")
        break

    print(pala)

    i += 1

print("Perdeste, não conseguis te acertar a palavra a tempo")