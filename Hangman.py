"""
Obtener una palabra aleatoriamente desde un archivo
Poner _ segun el largo de la palabra
Poner una letra, si la letra es correcta se reemplaza _ por la letra
Si es incorrecto se descuenta una vida (total de 5)
Si vidas llegan a 0 es GAME OVER
Si las letras se rellenan ganaste
"""


# generate random integer values
from random import seed
from random import randint

# Iniciar Juego
def iniciar(palabra):
    a = ''
    for i in range(len(palabra)):
        a += '_'
    return a

# Reemplazar letra
def adivinar(guess, letra, vidas, palabraJuego):
    cantidad = 0
    for i in range(len(palabraJuego)):
        if palabraJuego[i] == letra:
            guess = guess[:i] + letra + guess[i + 1:]
            cantidad += 1
    if cantidad == 0:
        vidas -= 1
    
    return (guess, letra, vidas)

def comprobar(guess):
    for i in range(len(guess)):
        if guess[i] == '_':
            return False
    return True

# seed random number generator
seed(None, 2)

palabras = open("palabras.txt", "r")
lista = palabras.readlines()
palabras.close()

cantidadPalabras = len(lista)
pos = randint(0, cantidadPalabras - 1)

palabraJuego = lista[pos]
palabraJuego = palabraJuego[:-1]

guess = iniciar(palabraJuego)
print(guess)

# Parametros de juego
gameOver = False
vidas = 5
print(palabraJuego)

while not gameOver:
    letra = input("Ingrese una letra: ")
    guess, letra, vidas = adivinar(guess, letra, vidas, palabraJuego)
    print(guess)
    print("vidas = " + str(vidas))
    if vidas == 0 or comprobar(guess):
        gameOver = True
        print("GAME OVER")
