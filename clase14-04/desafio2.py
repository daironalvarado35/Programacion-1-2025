"""
2. Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un
mensaje según el valor:
● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
● 4 y 5 ---> Aprobado, la nota es ...
● 1, 2 y 3 ---> Desaprobado, la nota es …
Adjuntar Github en este formulario
https://forms.gle/1rdRgpfbGW96Cawd6

"""
import random

# Generar una nota aleatoria entre 1 y 10
nota = random.randint(1, 10)

# Evaluar la nota con if, elif y else

if nota > 5 and nota < 11 :
    print(f"Promoción directa, la nota es: {nota}")
elif nota > 3 and nota < 6 :
    print (f"Aprobado, la nota es {nota}")
else:
    print(f"Desaprobado, la nota es: {nota}")
