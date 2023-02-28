"""
Programa para calcular o Índice de Massa Corporal - IMC.
"""

# Bibliotecas
import time
import os

# Variáveis


#----------Tela de Inicio----------#
print('#-------------------------------#')
print('#-------------------------------#')
print('#------Calculadora de IMC-------#')
print('#-------------------------------#')
print('#-------------------------------#')

time.sleep(1)

print()
tecle = input('Tecle "Enter" para continuar. ')
os.system('cls') or None
print()
#----------Tela de Inicio----------#

#----------Entrada de Dados do Usuário----------#
print('Vamos precisar de alguns dados.')
nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2
time.sleep(1)
#----------Entrada de Dados do Usuário----------#

#----------Resumo do Usuário----------#
print()
print(f'{nome} tem {altura:.2f} de altura pesando {peso} kg')
print(f'Seu IMC é: {imc:.2f}')

time.sleep(1)
#----------Resumo do Usuário----------#

#----------Calculo do IMC----------#
if imc <= 18.50:
    tabimc = '--> Abaixo do Peso'

elif imc > 18.50 and imc < 24.90:
    tabimc = '--> Sobrepeso'

elif imc > 25.00 and imc < 29.90:
    tabimc = '--> Obesidade Grau I'

elif imc > 30.00 and imc < 34.90:
    tabimc = '--> Obesidade Grau II'

elif imc > 35.00 and imc < 49.90:
    tabimc = '--. Obesidade Grau III ou Mórbida'

else:
    tabimc = '--> Thais Carla'
#----------Calculo do IMC----------#

# Mensagem de recursos adicionais
# print('De acordo com a Organização Mundial da Saúde, seu IMC')

# mensagem = 'está abaixo do recomendado para a sua altura.'
# mensagem21 = 'Para manter o valor de IMC normal, seu peso pode variar entre {63.3} e {85.2} kg.'

# mensagem = 'está normal para a sua altura.'
# mensagem2 = 'Para manter o valor de IMC normal, seu peso pode variar entre {63.3} e {85.2} kg.'

# mensagem = 'está acima do recomendado para a sua altura.'
# mensagem3 = 'Para atingir um valor de IMC normal, seu peso deve estar entre {63.3} e {85.2} kg.'

print()
print('De acordo com a Organização Mundial da Saúde, seu IMC é: ')
print(tabimc)
