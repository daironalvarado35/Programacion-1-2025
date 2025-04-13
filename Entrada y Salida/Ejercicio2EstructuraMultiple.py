"""Premisa:
Ejercicio: Sistema de calificaciones
Imagina que estás creando un programa que evalúa una nota numérica (de 0 a 100) y devuelve una calificación como texto:

Si la nota es 90 o más → "Excelente"

Si la nota está entre 80 y 89 → "Muy bien"

Si la nota está entre 70 y 79 → "Bien"

Si la nota está entre 60 y 69 → "Suficiente"

Si la nota es menor que 60 → "Reprobado"

Si la nota es mayor que 100 o menor que 0 → "Nota inválida"


"""

nota = float(input("Ingrese su nota:"))

if nota > 90:
    print ("Excelente")
elif nota > 79 and nota < 90:
    print("Muy bien")
elif nota > 69 and nota < 80:
    print("Bien")
elif nota > 59 and nota < 70:
    print("suficiente")
elif nota < 60:
    print ("reprobado")
elif nota > 100 or nota < 0:
    print ("Nota invalida")
