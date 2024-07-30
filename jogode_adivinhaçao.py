import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Jogo da Adivinhação")
    print("Tente adivinhar um número entre 1 e 100")

    while True:
        tentativa = int(input("Digite seu palpite: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Baixo! Tente novamente")
        elif tentativa > numero_secreto:
            print("Alto! Tente novamente")
        else:
            print(f"Parabéns! Você adivinhou o número secreto em {tentativas} tentativas.")
            break

jogo_adivinhacao()