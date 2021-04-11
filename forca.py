import random


def jogar():
    exibir_boas_vindas()
    palavra_secreta = carregar_palavra_secreta()

    letras_separadas = separar_letras(palavra_secreta)
    print(letras_separadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = solicitar_chute()

        if (chute in palavra_secreta):
            marcar_chute_correto(palavra_secreta, chute, letras_separadas)
        else:
            erros += 1
            desenhar_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_separadas
        print(letras_separadas)

    if (acertou):
        exibir_mensagem_vitoria()
    else:
        exibir_mensagem_derrota(palavra_secreta)

    print("Fim do jogo.")


def exibir_boas_vindas():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregar_palavra_secreta(nome_arquivo="palavras.txt", primeira_linha_valida=0):
    palavras = []

    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    indice_aleatorio = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[indice_aleatorio].upper()

    return palavra_secreta


def separar_letras(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def solicitar_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute


def marcar_chute_correto(palavra_secreta, chute, letras_separadas):
    indice = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_separadas[indice] = letra
        indice += 1


def exibir_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def exibir_mensagem_derrota(palavra_secreta):
    print("Poxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()
