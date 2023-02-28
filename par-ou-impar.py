# Projeto: Jogo do Par ou Ímpar

import time

print("############################################")
print("#..........................................#")
print("#..........................................#")
print("#...Olá, seja bem-vindo ao meu projeto: ...#")
print("#..........................................#")
print("#..............Jhones.Sombra...............#")
print("############################################")

time.sleep(1)

input("Tecle Enter para continuar")

print("\n" * 130)

while True:
    try:
        valor = int(input("Digite um número inteiro: "))
        if valor % 2 ==0:
            print("Este é um número par!")
        else:
            print("Este é um número impar!")

    except:
        print("Digite apenas números inteiros!")