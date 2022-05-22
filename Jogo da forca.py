import random
print(f"\033[33mJOGO DA FORCA\033[m")
cont=0
palavras_lista = ["cavalo", "flor", "casa", "jumento", "rato", "mochila", "suco", "computador", "musica", "trem", "cu", "banana", "mesa", "caderno", "pote"]
escolha_palavra = random.choice(palavras_lista)
traco= "_"*len(escolha_palavra)
boneco_lista=["┏", "┓", "┏", "┃", "┓", ":)"]
while traco != escolha_palavra:
    print()
    print("\033[36mFORCA >>>>")
    print("|", '—'*20)
    print("|", ' '*18, '|')
    print("|", ' '*18, '|')
    print("|", ' '*18, '|')
    print(f"|                 ", ' ', boneco_lista[5])
    print(f"|                 ", boneco_lista[2],boneco_lista[3], boneco_lista[4])
    print(f"|                 ", '', boneco_lista[0], boneco_lista[1])
    print("\033[36m|")
    print("|")
    print("|")
    print("|                 ", f"\033[31m{traco}\033[m")
    print("\033[36m|\033[m")
    print(f"Chances: {6-cont}")
    print()
    escolha_letra = str(input("Escolha uma letra: "))
    if escolha_letra in escolha_palavra:
        for pos, item in enumerate(escolha_palavra):
            if item == escolha_letra:
                traco = traco[:pos] + escolha_letra + traco[pos+1:]

    else:
        print('\033[31m', '=-' *3, "Não tem essa letra!", '=-'*3, '\033[m')
        boneco_lista[cont] = ''
        cont+=1
    if cont >= 6:
        break
if traco == escolha_palavra:
    print("\033[43mVOCÊ GANHOU PARABENS!!\033[m")
    print('Palavra correta: >>> ', escolha_palavra.upper())
else:
    print("\033[41mVOCÊ PERDEU TODAS AS SUAS CHANCES O JOGO SE ENCERROU!\033[m")
    print('Palavra correta: >>> ', escolha_palavra.upper())

##AAAAA
