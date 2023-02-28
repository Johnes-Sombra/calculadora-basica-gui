# Projeto - Calculadora simples

import time

print("#############################################")
print("#...........................................#")
print("#...........................................#")
print("#............CALCULADORA....................#")
print("#...............SOMBRA......................#")
print("#...........................................#")
print("#############################################")

time.sleep(1)

input('Tecle Enter para continuar')

print("\n" * 130)

numero01 = 0
numero02 = 0
resultado = 0
operacao = 0

while True:

        try:
                numero01 = int(input('Digite o primeiro valor a ser calculado: '))

                operacao = input('Escolha o operador a ser usado: +, -, * ou / ')

                numero02 = int(input('Digite o segundo valor: '))

                if operacao == '+':
                    resultado = numero01 + numero02

                elif operacao == '-':
                    resultado = numero01 - numero02

                elif operacao == '*':
                    resultado = numero01 * numero02

                elif operacao == '/':
                    resultado = numero01 / numero02

                else:
                    resultado = resultado
                print(str(numero01) + ' ' + str(operacao) + ' ' + str(numero02) + ' = ' + str(resultado))
        except:
                print('Digite uma operação válida!')