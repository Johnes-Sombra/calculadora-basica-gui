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

def primo(n):
    for val in range(2,n):
        if n % val == 0:
            return False

    return True