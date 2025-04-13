"""Estructuras Multiples: if elif else """
"""El elif se puede leer como: sino pero y es utilizado para cuando quieres evaluar mas de dos opciones"""

"""costo = float(input("Ingrese el costo del producto: "))

precio = float (input("Ingrese el precio del producto: "))

if costo < precio:
    utilidad = precio - costo
    print ("Tuviste una utilidad de: ", utilidad)
elif costo > precio:
    perdida = precio - costo
    print ("Tuviste una perdida de: ", perdida)
else:
    print ("Saliste empatado")

"""
########################################################################################################################################################

"""Ejercicio Estructura multiple con Mario:

Mario salta la tortuga → sigue jugando.

La tortuga toca a Mario → pierde una vida. Si se queda sin vidas, reinicia nivel.

Mario pisa la tortuga → la tortuga muere, Mario gana 100 puntos.

"""
# Variables iniciales
accion = input("Que hizo Mario con la tortuga? Puede ser (salta toca pisa): ") .lower()
vidas = 1
puntos = 0


if accion == "salta":
    print("Mario saltó la tortuga. Mario sigue jugando.")
elif accion == "toca":
    vidas -= 1
    print("La tortuga tocó a Mario. Mario pierde una vida.")
    if vidas < 1:
        print("Mario murió. Reinicia el nivel.")
    else:
        print(f"Vidas restantes: {vidas}")
elif accion == "pisa":
    puntos += 100
    print("Mario pisó la tortuga. La tortuga muere, Mario gana 100 puntos.")
    print(f"Puntos: {puntos}")
else:
    print("Acción no reconocida.")