# Jhones Sombra
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

# Calculador de números primos

def primo(n):
    for val in range(2,n):
        if n % val == 0:
            return False

    return True
        
def exibe():
    n = int(input('Exibir primos até o número: '))
    for val in range(2,n+1):
        if(primo(val)):
            print(val)
    
while True:
    exibe()
