import string
import random
import os
def titulo():
    print("--------------------------")
    print("|Generador de contraseñas|")
    print("--------------------------")

#REGLAS DEL JUEGO
def reglas():
    print("\nReglas del Generador de Contraseñas:")
    print("- La longitud debe estar entre 5 y 128 caracteres.")
    print("- Puedes incluir letras mayúsculas, minúsculas, números y símbolos.")
    print("- Las contraseñas fáciles de decir contienen solo letras.")
    print("- Las contraseñas fáciles de leer evitan caracteres confusos como '0' y 'O'.")
    print("- Se recomienda usar al menos 3 tipos de caracteres para mayor seguridad.")

#FUNCION PEDIR LONGITUD
def longitud_c():
    while True:
        os.system("cls") #Se limpia la consola antes de pedir la longitud
        try:
            longitud = int(input("Ingresa una longitud de la contraseña (5-128): "))
            if 5<= longitud <=128:
                return longitud #Me retorna el valor de la longitud(Solo si es valida)
            else:
                print("Longitud fuera de rango")
        except:
            print("Error: Ingresa un numero valido") #Mensaje de error en caso de ingresar un dato de tipo string


def contraseña_f_dl():
    longitud = longitud_c()
    letras = string.ascii_letters #Agrega solo letras por defecto

    contraseña ="" #inicializacion de la variable contraseña vacia

    # Genera la contraseña
    for _ in range(longitud):
        contraseña += random.choice(letras)
    print(f"Contraseña generada: {contraseña}")

#FUNCION GENERAR CONTRSEÑA FACIL DE DECIR(mayusculas, minusculas y pregunta si quiere agg numeros y simbolos)
def contraseña_f_dd():
    longitud = longitud_c()
    letras = string.ascii_letters #Agrega solo letras por defecto

    contraseña ="" #inicializacion de la variable contraseña vacia

    #Pregunta si se desean incluir números
    agg_numeros = input("¿Quieres que incluya numeros? (s/n): ").strip().lower()
    if agg_numeros == 's':
        letras += string.digits  # Agrega números (0-9)
    else:
        print("No se agregaran numeros")

    #Pregunta si se desean incluir símbolos
    agg_simbolos = input("¿Quieres que incluya simbolos? (s/n): ").strip().lower()
    if agg_simbolos == 's':
        letras += string.punctuation
    else:
        print("No se agregaran simbolos")

    # Genera la contraseña
    for _ in range(longitud):
        contraseña += random.choice(letras)
    print(f"Contraseña generada: {contraseña}")


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
            contraseña_f_dl()
            input("\nPresiona enter para continuar a las opciones de generacion de contraseña")
        elif opcion == "3":
            print("\nSeleccionaste: Contraseña automática fácil de leer.")
            contraseña_f_dd()
            input("\nPresiona enter para continuar a las opciones de generacion de contraseña")
        elif opcion == "4":
            print("\nSeleccionaste: Todos los caracteres.")
        elif opcion == "5":
            print("\nVolviendo al menú principal...")
            break  # Sale del submenú y vuelve al menú principal
        else:
            print("\n Opción no válida. Inténtalo de nuevo.")

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