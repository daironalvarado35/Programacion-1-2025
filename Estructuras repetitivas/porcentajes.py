encuestas = 0 # ESTO ES UN ACUMULADOR
contador_a = 0 # ESTO ES UN CONTADOR
contador_b = 0 # ESTO ES UN CONTADOR

while encuestas < 14:
    respuesta = input ("Que producto prefiero (a o b)?: ") # le pide al usuario que elija a o b
    match respuesta:
        case "a":
            contador_a += 1
        case "b":
            contador_b += 1
    encuestas += 1 # Despues de cada respuesta se suma 1 al acumulador de encuestas
porcentaje_a = (contador_a * 100) / encuestas # formula para calcular el porcentaje
porcentaje_b = (contador_b * 100) / encuestas

print(f"Porcentaje de personas que eligen el producto A: {porcentaje_a}")
print(f"Porcentaje de personas que eligen el producto B: {porcentaje_b}")