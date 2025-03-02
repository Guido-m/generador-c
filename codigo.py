import string #MODULO QUE CONTIENE CONSTANTES Y FUNCIONES(PARA TRABAJAR CON CADENAS)
import random #MODULO PARA GENERAR VALORES DE MANERA ALEATORIA
import os

#REGLAS DEL JUEGO
#LA FUNCIÓN REGLAS MUESTRA POR PANTALLA LAS REGLAS DEL GENERADOR DE CONTRASEÑAS.
def reglas():
    print("\nReglas del Generador de Contraseñas:")
    print("- La longitud debe estar entre 5 y 128 caracteres.")
    print("- Puedes incluir letras mayúsculas, minúsculas, números y símbolos.")
    print("- Las contraseñas fáciles de decir contienen solo letras.")
    print("- Las contraseñas fáciles de leer evitan caracteres confusos como '0' y 'O'.")
    print("- Se recomienda usar al menos 3 tipos de caracteres para mayor seguridad.")

#FUNCION LIMPIAR PANTALLA, LIMPIA LA CONSOLA
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear") 

#FUNCION LONGITUD_C
#SOLICITA AL USUARIO LA LONGITUD  PARA LA CONTRASEÑA Y VALIDA QUE ESTÉ ENTRE 5 Y 128 CARACTERES
def longitud_c():
    while True:
        limpiar_pantalla()# LIMPIA LA PANTALLA ANTES DE SOLICITAR LA ENTRADA
        try:
            longitud = int(input("Ingresa una longitud de la contraseña (5-128): "))# PIDE AL USUARIO QUE INGRESE LA LONGITUD Y LA CONVIERTE A ENTERO
            if 5<= longitud <=128:
                return longitud #ME RETORNA EL VALOR DE LA LONGITUD SOLO SI ES VALIDA
            else:
                print("Longitud fuera de rango")# INFORMA SI EL NÚMERO ESTÁ FUERA DEL RANGO PERMITIDO
        except:
            print("Error: Ingresa un numero valido") # EN CASO DE ERROR (POR EJEMPLO, SI SE INGRESA TEXTO EN LUGAR DE NÚMERO)

#FUNCIÓN EVALUAR_SEGURIDAD
#EVALÚA LA FORTALEZA DE UNA CONTRASEÑA, BASÁNDOSE EN SU LONGITUD Y LA VARIEDAD DE TIPOS DE CARACTERES QUE CONTIENE
def evaluar_seguridad(contraseña):
    longitud = len(contraseña)
    #COMPRUEBA SI LA CONTRASEÑA CONTIENE AL MENOS UN CARÁCTER DE CADA TIPO
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_minus = any(c.islower() for c in contraseña)
    tiene_numeros = any(c.isdigit() for c in contraseña)
    tiene_simbolos = any(c in string.punctuation for c in contraseña)

    #HACE EL CONTEO DE CUANTOS TIPOS DE CARACTERES DIFERENTES HAY EN LA CONTRASEÑA
    seg_c = sum([tiene_mayus, tiene_minus, tiene_numeros, tiene_simbolos])

    #CONDICION DE SEGURIDAD SEGÚN LA LONGITUD Y LA VARIEDAD DE CARACTERES
    if longitud >= 10 and seg_c >= 3: 
        return " Contraseña de nivel FUERTE " # Es fuerte si tiene al menos 10 caracteres y usa 3 o más tipos de caracteres
    elif 8 <= longitud < 10 and seg_c >= 2:
        return " Contraseña de nivel Medio "  # Es moderada si tiene entre 8 y 9 caracteres y al menos 2 tipos de caracteres
    else:
        return " Contraseña de nivel DÉBIL "  # Es débil si no cumple con los criterios anteriores
    
#FUNCIÓN CONTRASEÑA_P
#FUNCION QUE PERMITE AL USUARIO INGRESAR SU PROPIA CONTRASEÑA Y LA EVALÚA
def contraseña_p():
    longitud = longitud_c()# SOLICITA LA LONGITUD DE LA CONTRASEÑA
    print (f"\nIngresa una contraseña con esa longitud {longitud} caracteres ")

    while True:
        contraseña = input("Ingresa tu contraseña: ")

        if len(contraseña) == longitud:
            print(f" Contraseña: {contraseña}")
            # EVALÚA Y MUESTRA LA SEGURIDAD DE LA CONTRASEÑA
            print(evaluar_seguridad(contraseña))  
            input("\nPresiona Enter para continuar")
            break # SALE DEL BUCLE AL CUMPLIR LA CONDICIÓN
        else:
            print(f"La contraseña debe tener {longitud} caracteres")


#FUNCIÓN CONTRASEÑA_F_DL
#GENERA UNA CONTRASEÑA AUTOMÁTICA QUE CONTIENE SOLO LETRAS (MAYÚSCULAS Y MINÚSCULAS).
def contraseña_f_dl():
    longitud = longitud_c()
    letras = string.ascii_letters # UTILIZA TODAS LAS LETRAS DEL ALFABETO (MAYÚSCULAS Y MINÚSCULAS)
    contraseña = "".join(random.choice(letras) for _ in range(longitud))

    print(f"Contraseña generada {contraseña}")
    print(evaluar_seguridad(contraseña))  # Evaluar seguridad de la contraseña
    input("\n Presiona enter para continuar")

#FUNCIÓN CONTRASEÑA_F_DD
#FUNCION GENERAR CONTRASEÑA FACIL DE DECIR(MAYUS,MINUS Y OPCIONAL NUMEROS Y SIMBOLOS)
def contraseña_f_dd():
    longitud = longitud_c() #SOLICITA LA LONGITUD 
    letras = string.ascii_letters #INICIA CON LETRAS 

    #PREGUNTA AL USUARIO SI DESEA INCLUIR NÚMEROS 
    if input("¿Quieres incluir números? (s/n): ").strip().lower() == 's':
        letras += string.digits
    # PREGUNTA AL USUARIO SI DESEA INCLUIR SÍMBOLOS
    if input("¿Quieres incluir símbolos? (s/n): ").strip().lower() == 's':
        letras += string.punctuation
    
    #GENERA LA CONTRASEÑA SELECCIONANDO ALEATORIAMENTE CARACTERES DE LA CADENA RESULTANTE
    contraseña = "".join(random.choice(letras) for _ in range(longitud))

    print(f" Contraseña generada: {contraseña}")
    print(evaluar_seguridad(contraseña))  # Evaluar seguridad de la contraseña
    input("\nPresiona Enter para continuar")

#FUNCIÓN CONTRASEÑA_T
#GENERA UNA CONTRASEÑA USANDO TODAS LAS OPCIONES DE CARACTERES DISPONIBLES, PERMITIENDO AL USUARIO ELEGIR CUÁLES INCLUIR.
def contraseña_t():
    longitud = longitud_c()
    print("\nSelecciona las opciones de caracteres que deseas incluir en la contraseña.")
    print("Debes de eligir al menos 3 opciones de las siguientes")

    #SOLICITA AL USUARIO SI DESEA INCLUIR MAYÚSCULAS
    #.STRIP() ELIMINA ESPACIOS EXTRA, Y .LOWER() CONVIERTE LA ENTRADA A MINÚSCULAS.
    while True:
        mayus = input("¿Incluir mayúsculas? (s/n): ").strip().lower()
        if mayus in ['s', 'n']:
            break
        print("Ingresa 's' para si o 'n' para no ")
    #SOLICITA AL USUARIO SI DESEA INCLUIR MINÚSCULAS
    while True:
        minus = input("¿Incluir minúsculas? (s/n): ").strip().lower()
        if minus in ['s', 'n']:
            break
        print("Entrada no válida. Ingresa 's' para sí o 'n' para no.")
    #SOLICITA AL USUARIO SI DESEA INCLUIR NÚMEROS
    while True:
        numeros = input("¿Incluir números? (s/n): ").strip().lower()
        if numeros in ['s', 'n']:
            break
        print("Entrada no válida. Ingresa 's' para sí o 'n' para no.")
    #SOLICITA AL USUARIO SI DESEA INCLUIR SÍMBOLOS
    while True:
        simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower()
        if simbolos in ['s', 'n']:
            break
        print("Entrada no válida. Ingresa 's' para sí o 'n' para no.")

    #CUENTA CUÁNTAS OPCIONES POSITIVAS SI ELIGIÓ EL USUARIO
    op_esco = 0
    if mayus == 's':
        op_esco += 1
    if minus == 's':
        op_esco += 1
    if numeros == 's':
        op_esco += 1
    if simbolos == 's':
        op_esco += 1
    
    #VERIFICA QUE SE HAYAN SELECCIONADO AL MENOS 3 TIPOS DE CARACTERES
    if op_esco < 3:
        print("\nTienes que escoger 3 combinaciones de caracteres obligatorias.")
        input("Presiona Enter para intentarlo nuevamente...")
        return contraseña_t() #FUNCION DE LOS REQUISITOS
    
    #SE CREA LA CADENA DE CARACTERES DE ACUERDO A LAS ELECCIONES DEL USUARIO
    caracteres = ""
    if mayus == 's':
        caracteres += string.ascii_uppercase # AÑADE LETRAS MAYÚSCULAS
    if minus == 's':
        caracteres += string.ascii_lowercase # AÑADE LETRAS MINÚSCULAS
    if numeros == 's':
        caracteres += string.digits # AÑADE DÍGITOS NUMÉRICOS
    if simbolos == 's':
        caracteres += string.punctuation # AÑADE SÍMBOLOS
    
    #Generar la contraseña
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    print(f"\nContraseña generada: {contraseña}")
    print(evaluar_seguridad(contraseña))
    input("\nPresiona Enter para continuar")
    
#FUNCIÓN MENU_GENERAR_CONTRASEÑA
#MUESTRA UN SUBMENÚ QUE PERMITE AL USUARIO ELEGIR EL MÉTODO PARA GENERAR LA CONTRASEÑA
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
            input("Presiona Enter para continuar...")

#FUNCION MENU PRINCIPAL
#ES EL MENÚ PRINCIPAL QUE PERMITE AL USUARIO ELEGIR ENTRE GENERAR UNA CONTRASEÑA, VER LAS REGLAS O SALIR DEL PROGRAMA
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
            menu_generar_contraseña() # LLAMA AL SUBMENÚ DE GENERACIÓN DE CONTRASEÑAS
        elif opcion == "2":
            limpiar_pantalla()  # LIMPIA LA PANTALLA ANTES DE MOSTRAR LAS REGLAS
            reglas() # MUESTRA LAS REGLAS
            input("\nPresiona Enter para volver al menú")
        elif opcion == "3":
            print("\nSaliendo del programa")
            break  # FINALIZA EL PROGRAMA
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")
            input("Presiona Enter para continuar...")

menu_p() # INICIO DEL PROGRAMA: SE LLAMA AL MENÚ PRINCIPAL PARA COMENZAR LA INTERACCIÓN CON EL USUARIO.




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