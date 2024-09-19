#Programa que pida al usuario las sus calificaciones y la represe con alguna letra del alfabetoentre A-F

# Solicitar al usuario que ingrese la calificacion
calificacion = float(input("Introduzca su calificacion: "))

#Establecer las condiciones para asignar el caracter correspondiente a su calificacion

if 90 <= calificacion <= 100:
        letra = "A"
        
elif 80 <= calificacion < 90:
        letra = "B"
        
elif 70 <= calificacion < 80:
        letra = "C"
        
elif 60 <= calificacion < 70:
        letra = "D"
        
elif 0 <= calificacion < 60:
        letra = "F"

 # Mostrar la calificación correspondiente
print(f"La calificación es: {letra}")
