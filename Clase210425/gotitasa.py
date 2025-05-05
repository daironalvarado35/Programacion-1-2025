
consumoTotal = int(input("ingrese la cantidad de metros consumidos: "))
tipoCliente = str(input("ingrese que tipo de cliente es:"))
valorMetroCubico = 200
cargoFijo = 7000
montoSinDescuento = 0
montoFinalPagar = 0
porcentaje = 0
operacion = 0

# Calculos:

if consumoTotal < 30 and tipoCliente == "Residencial" :
    montoSinDescuento = consumoTotal * valorMetroCubico
    porcentaje = 10 * montoSinDescuento / 100
    montoFinalPagar = montoSinDescuento - porcentaje
    print (f"el monto a pagar es {montoFinalPagar}")

elif consumoTotal > 80 and tipoCliente == "Residencial" :
    montoSinDescuento = consumoTotal * valorMetroCubico
    porcentaje = 15 * montoSinDescuento / 100
    montoFinalPagar = montoSinDescuento + porcentaje
    print (f"el monto a pagar es {montoFinalPagar}")

elif consumoTotal > 150 and tipoCliente == "Comercial" :
    montoSinDescuento = consumoTotal * valorMetroCubico
    porcentaje = 8 * montoSinDescuento / 100
    montoFinalPagar = montoSinDescuento - porcentaje
    print (f"el monto a pagar es {montoFinalPagar}")

elif consumoTotal > 300 and tipoCliente == "Comercial" :
    montoSinDescuento = consumoTotal * valorMetroCubico
    porcentaje = 12 * montoSinDescuento / 100
    montoFinalPagar = montoSinDescuento - porcentaje
    print (f"el monto a pagar es {montoFinalPagar}")

elif consumoTotal < 50 and tipoCliente == "Comercial" :
    montoSinDescuento = consumoTotal * valorMetroCubico
    porcentaje = 12 * montoSinDescuento / 100
    montoFinalPagar = montoSinDescuento - porcentaje
    print (f"el monto a pagar es {montoFinalPagar}")