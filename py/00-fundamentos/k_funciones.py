# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Funciones (Definición y Retorno)
# Este código está completamente en español.

# ====================================================
# CONCEPTO BÁSICO DE FUNCIONES
# ====================================================

# Las FUNCIONES son bloques de código reutilizables que realizan una tarea
# específica. Son como 'mini-programas' dentro de nuestro programa principal.

# Se definen usando la palabra clave 'def' (de 'define').
# La sintaxis es: def nombre_funcion([argumentos]):

# ----------------------------------------------------
# 1. FUNCIÓN SIN ARGUMENTOS NI RETORNO
# ----------------------------------------------------

# Definimos una función simple que solo imprime un mensaje.
def hola_mundo():
    # Este es el cuerpo de la función.
    print("Hola Mundo")

# Llamamos (ejecutamos) la función para que haga su trabajo.
hola_mundo()

###

# ----------------------------------------------------
# 2. FUNCIÓN CON ARGUMENTOS (PARÁMETROS)
# ----------------------------------------------------

# Una función puede aceptar información de entrada, llamada ARGUMENTOS.
# El argumento 'nombre' se usa dentro de la función.
def saludo(nombre):
    # La función usa el argumento 'nombre' que se le pasa al ser llamada.
    print("¡Hola " + nombre + "!")

# Llamamos a la función y le pasamos el valor "Avi" como argumento.
saludo("Carlos")

###

# ----------------------------------------------------
# 3. FUNCIÓN CON ARGUMENTOS (Operación e Impresión)
# ----------------------------------------------------

# Función que acepta dos números y realiza una operación (suma).
def sumar(num1, num2):
    # La función IMPRIME el resultado.
    print("Resultado de la suma (solo imprime):", num1 + num2)

# Llamamos a la función.
sumar(10, 15)

###

# ----------------------------------------------------
# 4. FUNCIÓN CON VALOR DE RETORNO (RETURN)
# ----------------------------------------------------

# El valor más útil de una función es cuando utiliza la palabra clave 'return'.
# 'return' envía el resultado de la función de vuelta al código que la llamó,
# permitiendo usar ese resultado en otras partes del programa.

def sumar_retorno(num1, num2):
    # La función CALCULA el valor y lo DEVUELVE (return).
    return num1 + num2

# El resultado de la función (46) se guarda en la variable 'suma_total'.
suma_total = sumar_retorno(12, 34)
print("Suma guardada en variable:", suma_total)

# --- Código de la función que no se ejecutará ---
def multiplicar(num1, num2):
    # Retorna el resultado inmediatamente.
    return num1 * num2
    # CUALQUIER código después de 'return' en el mismo bloque NUNCA se ejecuta.
    print("hola") # Nunca se ejecutará

# ----------------------------------------------------
# 5. ANIDAMIENTO DE FUNCIONES
# ----------------------------------------------------

# Podemos pasar el valor de retorno de una función como argumento a otra función.
# 1. Se calcula sumar_retorno(1, 2) -> devuelve 3.
# 2. Se calcula sumar_retorno(3, 4) -> devuelve 7.
# 3. Se calcula multiplicar(3, 7) -> devuelve 21.
print("Resultado de anidar funciones:", multiplicar(sumar_retorno(1, 2), sumar_retorno(3, 4)))