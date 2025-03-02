# 🔐 Generador de Contraseñas Seguras

Un programa en **Python** diseñado para generar contraseñas seguras y personalizadas, permitiendo mejorar la protección de cuentas y datos personales frente a ataques cibernéticos.

---

## 📖 Índice
1. [Descripción](#-descripción)
2. [Características](#-características)
3. [Requisitos previos](#-requisitos-previos)
4. [Instalación y ejecución](#-instalación-y-ejecución)
5. [Modo de uso](#-modo-de-uso)
6. [Estructura del repositorio](#-estructura-del-repositorio)
7. [Ejemplo de uso](#-ejemplo-de-uso)
8. [Posibles mejoras](#-posibles-mejoras)
9. [Licencia](#-licencia)
10. [Autor](#-autor)

---

## 📌 Descripción

El **Generador de Contraseñas Seguras** es una herramienta en **Python** que permite generar claves seguras y evaluar su nivel de fortaleza. Su diseño permite al usuario elegir entre diferentes tipos de contraseñas, asegurando que cumplan con criterios de seguridad esenciales.

Este proyecto ayuda a evitar el uso de contraseñas débiles y fáciles de adivinar, protegiendo información sensible ante ataques de fuerza bruta o ingeniería social.

---

## ⚡ Características

✔ **Modos de generación de contraseñas:**
   - **Personalizada** → El usuario ingresa su propia contraseña y el programa evalúa su seguridad.
   - **Automática con opciones personalizadas**:
     - 🔡 **Yo genero mi propia contraseña** → El usuario puede crear su propia contraseña segura.
     - 🔡 **Fácil de decir** → Solo usa letras para una mejor pronunciación.
     - 🔠 **Fácil de leer** → Evita caracteres confusos como "0" y "O".
     - 🔢 **Todos los caracteres** → Mezcla mayúsculas, minúsculas, números y símbolos para máxima seguridad.

✔ **Evaluación de seguridad:**  
   - Clasifica las contraseñas en **débil, media o fuerte** según su composición.  
   - Recomienda mejoras en caso de que la contraseña sea insegura.  

✔ **Interfaz en consola intuitiva:**  
   - Interacción amigable con el usuario mediante un sistema de menú.  
   - Solicita parámetros de personalización y genera la contraseña en segundos.  

✔ **Compatible con Windows, Linux y macOS.**  
   - Utiliza `os.system("cls" if os.name == "nt" else "clear")` para limpiar la consola según el sistema operativo.  

✔ **Código limpio y modular:**  
   - Organizado en funciones reutilizables para facilitar mejoras futuras.  

---

## 🔧 Requisitos previos

Para ejecutar la aplicación, es necesario tener instalado **Python 3.11.9** o una versión posterior. Puedes verificarlo ejecutando:

```bash
python --version

