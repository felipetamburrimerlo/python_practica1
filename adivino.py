# Adivina adivinador....
import random
numero_aleatorio = random.randrange(101)
gane = False
print("Tenés 5 intentos para adivinar un número entre 0 y 100")
intento = 1
while intento < 6 and not gane:
    numero_ingresado = int(input('Ingresá tu número: '))
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Mmm... No.. Ese número no es... Seguí intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
