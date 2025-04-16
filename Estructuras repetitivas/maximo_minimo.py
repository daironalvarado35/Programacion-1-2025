"""
Crea un programa que permita ingresar notas de estudiantes una por una.
El ingreso se detiene cuando el usuario escribe FIN.
Al final, el programa debe mostrar:

La nota más alta (máximo)

La nota más baja (mínimo)

El promedio de todas las notas

La cantidad total de notas ingresadas

"""

total_notas = 0 # acumulador
cantidad_notas = 0 # contador
max_nota = None # maximo
min_nota = None # minimo

while True: 
    nota = input("Ingrese una nota (o 'FIN' para terminar): ")
    if nota.upper() == "FIN":
        break

    nota = int(nota) # asumimos que el usuario siempre escribe un numero entero
    total_notas += nota
    cantidad_notas += 1 

    if max_nota is None or nota > max_nota:
        max_nota = nota
    if min_nota is None or nota < min_nota:
        min_nota= nota

    # Resultados:
promedio = total_notas / cantidad_notas

print (f"\n nota maxima: {max_nota}")
print (f"Nota minima {min_nota}")
print (f"Promedio {promedio}")
print (f"Cantidad de notas: {cantidad_notas}")

# EJEMPLO DE ESTE EJERCICIO USANDO UNA BANDERA

"""
total_notas = 0
cantidad_notas = 0
primer_valor = True  # Bandera

while True:
    nota = input("Ingrese una nota (o FIN para terminar): ")

    if nota == "FIN":
        break

    nota = int(nota)

    total_notas += nota
    cantidad_notas += 1

    if primer_valor:
        max_nota = nota
        min_nota = nota
        primer_valor = False
    else:
        if nota > max_nota:
            max_nota = nota
        if nota < min_nota:
            min_nota = nota

promedio = total_notas / cantidad_notas

print(f"\nNota máxima: {max_nota}")
print(f"Nota mínima: {min_nota}")
print(f"Promedio: {promedio}")


"""


