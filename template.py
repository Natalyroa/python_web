# Llamar librerias antes creadas modelo y vista - clase 5

from modelo import obtener_libros
from template import renderizar_template

def renderizar_template(libros):
    #Simular la renderizacion de un templete de libros
    htlm ="<h1>lista de libros </h1>"
    for libro in libros:
        html += f"<p>ID: {libro['id']}, titulo:{libro['titulo']}, autor:{libro['autor']}"
    return htlm

#Integrar la vista y el templete

def mostrar_libros_con_template():
    libros = obtener_libros()
    html = renderizar_template(libros)
    print
mostrar_libros_con_template