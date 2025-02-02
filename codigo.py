print("--------------------------")
print("|Generador de contraseñas|")
print("--------------------------")


while True: #Ciclo infinito 
    try:
        longitud = int(input("Ingresa un número entero entre 5 y 128: ")) #Pedir dato de longitud al usuario
        if 5 <= longitud <= 128: #Condicional if que evalua si el numero esta en el rango deseado
            break #El bucle infinito termina siempre y cuando sea valido
        else:
            print("Ingresa la longitud entre 5 y 128 ")
    except:
        print("Ingresa un numero estas ingresando letras")

# Validar si se incluyen mayúsculas
while True:  # Ciclo infinito para validar la entrada de mayúsculas
    in_myc = input("¿Desea utilizar mayúsculas en la generación de la contraseña? (s/n): ").strip().lower()
    if in_myc == "s":
        in_myc = True
        print("Se incluirán mayúsculas.")
        break
    elif in_myc == "n":
        in_myc = False
        print("No se incluirán mayúsculas.")
        break
    else:
        print("Entrada no válida. Ingresa 's' para sí o 'n' para no.")

print(f"Longitud de la contraseña a generar es de: {longitud}")
print(f"Incluir mayúsculas: {'Sí' if in_myc else 'No'}")

# num = int(input("Deseas utilizar numeros: "))
# c_esp = input("Deseas utilizar caracteres especiales")