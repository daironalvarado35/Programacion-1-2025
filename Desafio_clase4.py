# edad_user = int(input('Ingrese su edad: '))

# if edad_user <= 0 or edad_user > 120:
#     print('Edad invalida')
# else:
#     if edad_user < 13:
#         print('Acceso denegado. Debes tener al menos 13 años para entrar')
#     elif 13 <= edad_user <= 17:
#         print ('Acceso restringido. Estás en modo adolescente')
#     else:
#         print ('Acceso completo concedido')


## Ejercicio de Gotita S.A.##

metros_consumidos = float(input('Ingrese cantidad de metros consumidos en m3: '))

tipo_cliente = input('Ingrese tipo de cliente [Residencial / Comercial / Industrial]: ')


tarifa_base = 7000
costo_m3 = 200

subtotal = metros_consumidos * costo_m3
print (f'Subtotal: {subtotal}')

if tipo_cliente == 'Residencial':
    #Caso Especial
    if (subtotal + tarifa_base) < 35000: 
        descuento_5 = subtotal * 0.05
        subtotal  = (subtotal + tarifa_base) - descuento_5
        print (f'Subtotal del Caso Especial: {subtotal}')

    if metros_consumidos < 30:
        descuento_10 = subtotal * 0.10
        subtotal = subtotal - descuento_10
        print (f'Subtotal con 10% de descuento ${descuento_10} quedaria ${subtotal}')
    elif metros_consumidos > 80:
        recargo_15 = subtotal * 0.15
        subtotal = subtotal + recargo_15
        print (f'Subtotal con 15% de recargo ${recargo_15} quedaria ${subtotal}')


   
##Corregir el resto del codigo con la variable subtotal##
        
# elif tipo_cliente == 'Comercial':
#     if metros_consumidos > 300:
#          descuento_12 = tarifaxm3 * 0.12
#          tarifa_total = tarifaxm3 - descuento_12
#     elif metros_consumidos > 150:
#         descuento_8 = tarifaxm3 * 0.08
#         tarifa_total = tarifaxm3 - descuento_8    
#     elif metros_consumidos < 50:
#         recargo_5 = tarifaxm3 * 0.05
#         tarifa_total = tarifaxm3 + recargo_5

# elif tipo_cliente == 'Industrial':
#     if metros_consumidos > 1000:
#          descuento_30 = tarifaxm3 * 0.30
#          tarifa_total = tarifaxm3 - descuento_30 
#     elif metros_consumidos > 500:
#         descuento_20 = tarifaxm3 * 0.20
#         tarifa_total = tarifaxm3 - descuento_20
#     elif metros_consumidos < 200:
#         recargo_10 = tarifaxm3 * 0.10
#         tarifa_total = tarifaxm3 + recargo_10



iva = subtotal * 0.21
subtotal = subtotal + iva  

##falta mostrar todo en print##

# print (f'El total es : ${subtotal}')
#print(round(subtotal,2))
print(f"El total es : ${subtotal:.2f}") ##2f para redondear el flotante