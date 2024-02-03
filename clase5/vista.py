# id libros clase - 5

from modelo import obtener_liros

def mostrar_libros():
    libros =obtener_liros()
    for libro in libros:
        print(f"ID: {libro['id']}, titulo:{libro['titulo']}, autor:{libro['autor']}")