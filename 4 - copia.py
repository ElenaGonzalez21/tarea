#Programa para dividir un grupo de alumnos en dos grupos A y B

#Pedir al usuario ingesar su edad
print("Ingrese su nombre:")
nombre=input()

#Pedir al usuario ingresar el genero
print("Ingrese su genero (M pra la mujeres, H para lo hombres):")
genero=input()

#Verificar los datos y establecer a que grupo pertenecen

if ( genero == "M" and nombre < "M") or ( genero =="H" and nombre > "N"):
    grupo="A"
else:
    grupo="B"

#Mostrar las respuestas
print(f"Perteneces al grupo:{grupo}")
