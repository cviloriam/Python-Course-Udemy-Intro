# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Operadores Aritméticos y Cadenas de Texto
# Este código está completamente en español, incluyendo variables, mensajes y comentarios.

# ====================================================
# 1. OPERADORES ARITMÉTICOS (CON NÚMEROS)
# ====================================================

# Operadores Aritméticos:
# + (Suma)
# - (Resta)
# * (Multiplicación)
# / (División)
# % (Módulo o Residuo)

edad1 = 12
edad2 = 18

# Suma (+): Une los dos números. Resultado: 30
print("Resultado de la Suma:", edad1 + edad2)

# Multiplicación (*): Multiplica los dos números. Resultado: 216
print("Resultado de la Multiplicación:", edad1 * edad2)

# División (/): Divide y el resultado siempre es un número decimal (flotante). Resultado: 0.666...
print("Resultado de la División:", edad1 / edad2)

# Módulo (%): Devuelve el residuo de la división entera.
# 12 / 18 = 0 y sobran 12. Resultado: 12
print("Resultado del Módulo (Residuo):", edad1 % edad2)

###

# ====================================================
# 2. CADENAS DE TEXTO (STRINGS)
# ====================================================

# Las cadenas de texto o 'strings' son secuencias de caracteres que van entre comillas.

frase1 = "hoy es un hermoso día"
# Simplemente imprime el contenido de la variable 'frase1'.
print("Imprimiendo cadena simple:", frase1)

###

# ----------------------------------------------------
# 3. OPERADOR + (CONCATENACIÓN DE CADENAS)
# ----------------------------------------------------

# El operador '+' PEGA dos o más cadenas de texto una al lado de la otra.
nombre = "carlos"
apellido = "perez"

# Concatenación simple: No añade espacios, las palabras quedan pegadas.
print("Nombres pegados:", nombre + apellido)

# Concatenación con espacio: Se añade una cadena de espacio (" ") entre las variables.
print("Nombres separados:", nombre + " " + apellido)

###

# ----------------------------------------------------
# 4. OPERADOR * (REPETICIÓN DE CADENAS)
# ----------------------------------------------------

# El operador '*' con una cadena y un número repite la cadena ese número de veces.
print("Repetición de cadena:", "hola" * 10)

###

# ----------------------------------------------------
# 5. INDEXACIÓN Y SLICING (ACCEDER A PARTES DE LA CADENA)
# ----------------------------------------------------

# Podemos acceder a caracteres específicos de una cadena usando corchetes [].
# La cuenta de la posición (el índice) SIEMPRE comienza en 0.

frase_larga = "carlos estaba jugando baloncesto"

# Indexación simple: Accede al carácter en la posición 0 (la primera letra).
print("Primer carácter (Índice 0):", frase_larga[0]) # Resultado: 'c'

# Slicing (corte): Accede a un rango de caracteres [inicio : fin].
# [0:6] significa empezar en la posición 0 e ir HASTA la posición 6, pero SIN INCLUIRLA.
# Los caracteres tomados son los de las posiciones 0, 1, 2, 3, 4 y 5.
print("Rango de caracteres [0:6]:", frase_larga[0:6]) # Resultado: 'carlos'