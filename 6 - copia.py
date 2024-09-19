#Programa para calcular descuento de zapatos

#Determinamos precio de cada zapato
precioDeZapato = 80

#Solicitamos la numeros de zapatos que desea compar al usuario
numeroDeZapato= int(input("Ingrese el numero de zapatos que desea comprar: "))

#Calculamos el total antes de descuento
totalCompra =precioDeZapato*numeroDeZapato

#Determinamos el porcentaje de descuento

if numeroDeZapato > 30:
 descuento = 0.40  
 
elif numeroDeZapato >= 20:
 descuento = 0.20  
 
elif numeroDeZapato > 10:
 descuento = 0.10  
 
else:
 descuento = 0.00  

#Calculamos el total después de aplicar el descuento
totalDescuento = totalCompra * (1 - descuento)

#Mostrar resultados al usuario
print(f"Total original: ${totalCompra: }")
print(f"Descuento aplicado: {descuento * 100: }%")
print(f"Total después del descuento: {totalDescuento: }")
