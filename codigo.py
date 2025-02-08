def titulo():
    print("--------------------------")
    print("|Generador de contraseñas|")
    print("--------------------------")

def reglas():
    print("\nReglas del Generador de Contraseñas:")
    print("- La longitud debe estar entre 5 y 128 caracteres.")
    print("- Puedes incluir letras mayúsculas, minúsculas, números y símbolos.")
    print("- Las contraseñas fáciles de decir contienen solo letras.")
    print("- Las contraseñas fáciles de leer evitan caracteres confusos como '0' y 'O'.")
    print("- Se recomienda usar al menos 3 tipos de caracteres para mayor seguridad.")

def menu_generar_contraseña():
    """Muestra el submenú para generar contraseñas"""
    while True:
        print("\nOpciones de generación:")
        print("1. Yo genero mi propia contraseña")
        print("2. Contraseña automática fácil de decir")
        print("3. Contraseña automática fácil de leer")
        print("4. Todos los caracteres")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nSeleccionaste: Yo genero mi propia contraseña.")
        elif opcion == "2":
            print("\nSeleccionaste: Contraseña automática fácil de decir.")
        elif opcion == "3":
            print("\nSeleccionaste: Contraseña automática fácil de leer.")
        elif opcion == "4":
            print("\nSeleccionaste: Todos los caracteres.")
        elif opcion == "5":
            print("\nVolviendo al menú principal...")
            break  # Sale del submenú y vuelve al menú principal
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")

def menu_p():
    while True:
        print("\n---------------------------")
        print("|     Menu de opciones    |")
        print("---------------------------")
        print("1. Generar contraseña")
        print("2. Reglas del generador de contraseñas")
        print("3. Salir")
    
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_generar_contraseña()
        elif opcion == "2":
            reglas()
        elif opcion == "3":
            print("\nSaliendo del programa...")
            break  # Sale del bucle y termina el programa
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")


menu_p()




# while True: #Ciclo infinito 
#     try:
#         #Longitud
#         longitud = int(input("Ingresa un número entero entre 5 y 128: ")) #Pedir dato de longitud al usuario
#         if 5 <= longitud <= 128: #Condicional if que evalua si el numero esta en el rango deseado
#             break #El bucle infinito termina siempre y cuando sea valido
#         else:
#             print("Ingresa la longitud entre 5 y 128 ")
#     except:
#         print("Ingresa un numero estas ingresando letras")

# # Validar si se incluyen mayúsculas
# while True:  # Ciclo infinito para validar la entrada de mayúsculas
#     in_myc = input("¿Desea utilizar mayúsculas en la generación de la contraseña? (s/n): ").strip().lower()
#     if in_myc == "s":
#         in_myc = True
#         print("Se incluirán mayúsculas.")
#         break
#     elif in_myc == "n":
#         in_myc = False
#         print("No se incluirán mayúsculas.")
#         break
#     else:
#         print("Entrada no válida. Ingresa 's' para sí o 'n' para no.")

# # Validar si se incluyen numeros
# while True:
#     num = input("Desea utilizar numeros en la generacion de la contraseña ? (s/n): ").strip().lower()
#     if num == "s":
#         num = True
#         print("Se incluirán numeros.")
#         break
#     elif num == "n":
#         num = False
#         print("No se incluirán numeros.")
#         break
#     else:
#         print("Entrada no válida. Ingresa 's' para sí o 'n' para no.")


# print(f"Longitud de la contraseña a generar es de: {longitud}")
# print(f"Incluir mayúsculas: {'Sí' if in_myc else 'No'}")

# num = int(input("Deseas utilizar numeros: "))
# c_esp = input("Deseas utilizar caracteres especiales")