#Programa para pedir al usuario una contraseña y compararla con la contraseña  almacenada en el programa( Sin tener en cuenta mayusculas y minusculas)

#Almacenar la contraseña ene la variable
contraseñaA= "Contraseña"

#Pedir al usuario que ingrese la contraseña, y almacenar la informacion en otra variable
print("Ingrese la contraseña:")
contraseñaB=input()

#Comparar ambas contraseñas ( Profe no encontre como compararla sin tomer en cuenta la mayuscula y las minuscula con lo que uested dio en clase por eso use lower)

if contraseñaA.lower()== contraseñaB.lower():
    print("La contraseña es valida")
    
else:
    print(" La contraseña es invalida")
