"""
IF - ELSE -ELIF
1. A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el
programa deberá determinar la posición del jugador en la cancha, considerando los
siguientes parámetros:
● Menos de 160 cm: Base
● Entre 160 cm y 179 cm: Escolta
● Entre 180 cm y 199 cm: Alero
● 200 cm o más: Ala-Pívot o Pívot

"""
# Declaro la variable altura:

altura = 0

# Evaluo:
altura = int(input("Por favor ingrese su altura: "))
if altura <= 160 :
    print ("Base")
elif altura > 159 and altura < 180 :
    print ("Escolta")
elif altura > 179 and altura < 200:
    print ("Alero")
if altura > 199:
    print("Ala-pivot o pivot")
