import random

censo = []
alfabeto = "abcdefghijklnmopqstuvwyz"
numero = 0

print("creando censo....")

for i in range (500_000):
    aumento = random.randint(1,2)
    numero += aumento

    letras = random.sample(alfabeto, 5)
    nombre = "".join(letras)

    edad = random.randint(18, 99)

    impuestos = random.choice((True, True, True, False))

    censo.append([numero, nombre, edad, impuestos])

    if len(censo) % 100_000 ==
        print()