#import pandas as pd
#import numpy as np

lista_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
objetivo_suma_ = 10
lista_n = []
def encontrar_suma(lista, objetivo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                lista_n.append(f'{lista[i]}-{lista[j]}')
    return lista_n

#print(lista_n)
numero_valido = encontrar_suma(lista_, objetivo_suma_)


for i in numero_valido:
    print(f'los numeros que cumplen el objetivo al sumarlos son: {i}')

