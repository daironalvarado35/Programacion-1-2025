# COMBINANDO CONTADORES Y ACUMULADORES PODEMOS CALCULAR PROMEDIO:
# LAS VARIABLES, CONTADORES Y ACUMULADORES SIEMPRE DEBEN DE INICIARSE
total_notas = 0
alumnos_registrados = 0

while True:
    nota = input("Ingrese su nota: ")
    if nota == "FIN":
        break
    else:
        total_notas += int(nota) # Acumulador
        alumnos_registrados += 1 # Contador
promedio = total_notas / alumnos_registrados
print(f"El promedio de la nota es: {promedio}")
