"""
2 - A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot

"""

altura = int(input("Por favor ingrese su altura: "))

if altura < 160:
    print ("Jugas de Base")
elif altura <=179:
    print("Jugas de Escolta")
elif altura <=199:
    print("Jugas de Alero")
elif altura <= 250:
    print("Ala-Pívot o Pívot") 
else:
    print("Usted no es humano")