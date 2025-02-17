import string
import random
import os


# def titulo():
#     print("---------------------------------")
#     print("|Generador de contraseñas seguras|")
#     print("---------------------------------")

#REGLAS DEL JUEGO
def reglas():
    print("\nReglas del Generador de Contraseñas:")
    print("- La longitud debe estar entre 5 y 128 caracteres.")
    print("- Puedes incluir letras mayúsculas, minúsculas, números y símbolos.")
    print("- Las contraseñas fáciles de decir contienen solo letras.")
    print("- Las contraseñas fáciles de leer evitan caracteres confusos como '0' y 'O'.")
    print("- Se recomienda usar al menos 3 tipos de caracteres para mayor seguridad.")

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear") 

#FUNCION PEDIR LONGITUD DE LA CONTRASEÑA
def longitud_c():
    while True:
        limpiar_pantalla()
        try:
            longitud = int(input("Ingresa una longitud de la contraseña (5-128): "))
            if 5<= longitud <=128:
                return longitud #ME RETORNA EL VALOR DE LA LONGITUD SOLO SI ES VALIDA
            else:
                print("Longitud fuera de rango")
        except:
            print("Error: Ingresa un numero valido") #MENSAJE DE ERROR EN CASO DE INGRESAR UN DATO DE TIPO STRING

#FUNCION QUE EVALUA SI LA CONTRASEÑA ES FUERTE, MEDIA O DEBIL
def evaluar_seguridad(contraseña):
    longitud = len(contraseña)
    #COMPRUEBA SI LA CONTRASEÑA TIENES DIFERENTES TIPOS DE CARACTERES
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_minus = any(c.islower() for c in contraseña)
    tiene_numeros = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in string.punctuation for c in contraseña)

    #HACE EL CONTEO DE CUANTOS TIPOS DE CARACTERES HAY
    seg_c = sum([tiene_mayus, tiene_minus, tiene_numeros, tiene_simbolos])

    #CONDICION DE SEGURIDAD
    if longitud >= 10 and seg_c >= 3: 
        return " Contraseña de nivel FUERTE " # Es fuerte si tiene al menos 10 caracteres y usa 3 o más tipos de caracteres
    elif 8 <= longitud < 10 and seg_c >= 2:
        return " Contraseña de nivel Medio "  # Es moderada si tiene entre 8 y 9 caracteres y al menos 2 tipos de caracteres
    else:
        return " Contraseña de nivel DÉBIL "  # Es débil si no cumple con los criterios anteriores
    

#FUNCION QUE PERMITE AL USUARIO INGRESAR SU PROPIA CONTRASEÑA 
def contraseña_p():
    longitud = longitud_c()
    print (f"\nIngresa una contraseña con esa longitud {longitud} caracteres ")

    while True:
        contraseña = input("Ingresa tu contraseña: ")

        if len(contraseña) == longitud:
            print(f" Contraseña: {contraseña}")
            print(evaluar_seguridad(contraseña))  # Evaluar seguridad de la contraseña ingresada
            input("\nPresiona Enter para continuar")
            break
        else:
            print(f"La contraseña debe tener {longitud} caracteres")
#FUNCION PARA GENERAR CONTRASEÑA SOLO LETRAS(MAYUS-MINUS)
def contraseña_f_dl():
    longitud = longitud_c()
    letras = string.ascii_letters #AGREGA SOLO LETRAS 
    contraseña = "".join(random.choice(letras) for _ in range(longitud))

    print(f"Contraseña generada {contraseña}")
    print(evaluar_seguridad(contraseña))  # Evaluar seguridad de la contraseña
    input("\n Presiona enter para continuar")

#FUNCION GENERAR CONTRSEÑA FACIL DE DECIR(MAYUS,MINUS Y OPCIONAL NUM Y SIMB)
def contraseña_f_dd():
    longitud = longitud_c()
    letras = string.ascii_letters #Agrega solo letras por defecto

    if input("¿Quieres incluir números? (s/n): ").strip().lower() == 's':
        letras += string.digits
    if input("¿Quieres incluir símbolos? (s/n): ").strip().lower() == 's':
        letras += string.punctuation
    
    contraseña = "".join(random.choice(letras) for _ in range(longitud))

    print(f" Contraseña generada: {contraseña}")
    print(evaluar_seguridad(contraseña))  # Evaluar seguridad de la contraseña
    input("\nPresiona Enter para continuar")

#FUNION GENERAR CONTRASEÑA CON TODOS LOS CARACTERES O ELIGIR QUE OPCIONES UTILIZAR
def contraseña_t():
    longitud = longitud_c()
    caracteres = string.ascii_letters + string.digits + string.punctuation 

    print("\n La contraseña se generará con mayúsculas, minúsculas, números y símbolos.")
    mod = input("¿Quieres modificar esta combinación? (s/n): ").strip().lower()

    if mod == 's':
        caracteres = string.ascii_letters
        
        if input("¿Incluir numeros? (s/n): ").strip().lower() == 's':
            caracteres += string.digits
        if input("¿Incluir simbolos? (s/n): ").strip().lower() == 's':
            caracteres += string.punctuation
        
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña generada: {contraseña}")
    print(evaluar_seguridad(contraseña))  # Evaluar seguridad de la contraseña
    input("\nPresiona Enter para continuar")

#MENU PARA SELLECIONAR EL TIPO DE CONTRASEÑA A GENERAR
def menu_generar_contraseña():
    while True:
        limpiar_pantalla()
        print("\nOpciones para generar contraseña:")
        print("1. Yo genero mi propia contraseña")
        print("2. Contraseña automática fácil de decir")
        print("3. Contraseña automática fácil de leer")
        print("4. Todos los caracteres")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nSeleccionaste: Yo genero mi propia contraseña.")
            contraseña_p()
        elif opcion == "2":
            print("\nSeleccionaste: Contraseña automática fácil de decir.")
            contraseña_f_dl()
        elif opcion == "3":
            print("\nSeleccionaste: Contraseña automática fácil de leer.")
            contraseña_f_dd()
        elif opcion == "4":
            print("\nSeleccionaste: Todos los caracteres.")
            contraseña_t()
        elif opcion == "5":
            print("\nVolviendo al menú principal")
            break  # Sale del submenú y vuelve al menú principal
        else:
            print("\n Opción no válida. Inténtalo de nuevo.")

#FUNCION MENU PRINCIPAL
def menu_p():
    while True:
        limpiar_pantalla()
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
            limpiar_pantalla()  # Limpia la pantalla antes de mostrar las reglas
            reglas()
            input("\nPresiona Enter para volver al menú")
        elif opcion == "3":
            print("\nSaliendo del programa")
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