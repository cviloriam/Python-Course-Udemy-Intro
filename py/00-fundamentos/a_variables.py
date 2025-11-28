# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Este código forma parte de un curso de programación para principiantes
# (niños y personas mayores) y está completamente en español.

# ====================================================
# VARIABLES Y ASIGNACIONES MÚLTIPLES EN PYTHON
# ====================================================

# ----------------------------------------------------
# 1. Asignación de una variable simple (Entero)
# ----------------------------------------------------

# Definimos una variable llamada 'edad' y le asignamos el número 41.
# Una variable es como una 'caja' con una etiqueta que guarda información.
edad = 41

# Usamos la función 'print' para mostrar el contenido de la variable 'edad'
# y un texto que explica lo que estamos mostrando.
print("Edad:", edad)

###

# ----------------------------------------------------
# 2. Asignación de una variable simple (Cadena de texto)
# ----------------------------------------------------

# Definimos la variable 'frase' y le asignamos un texto.
# Los textos (cadenas) siempre van entre comillas.
frase = "Mi nombre es Carlos"

# Mostramos el texto que está guardado en la variable 'frase'.
print("Frase:", frase)

###

# ----------------------------------------------------
# 3. Asignación Múltiple (Valores diferentes)
# ----------------------------------------------------

# Asignación múltiple en una línea:
# Podemos asignar diferentes valores a diferentes variables a la vez.
# Los valores de la derecha (16, 21, 23) se asignan en orden a las variables
# de la izquierda (edad_sara, edad_roberto, edad_miguel).
edad_sara, edad_roberto, edad_miguel = 16, 21, 23

# Mostramos la edad de cada persona.
print("Edad de Sara:", edad_sara)
print("Edad de Roberto:", edad_roberto)
print("Edad de Miguel:", edad_miguel)

###

# ----------------------------------------------------
# 4. Asignación Múltiple (Mismo valor)
# ----------------------------------------------------

# Asignamos el mismo valor (25) a tres variables diferentes a la vez.
# Esto es útil cuando varias variables deben empezar con el mismo valor inicial.
edad_sara = edad_roberto = edad_miguel = 25

# Mostramos los nuevos valores, confirmando que todas son 25.
print("Nueva edad de Sara:", edad_sara)
print("Nueva edad de Roberto:", edad_roberto)
print("Nueva edad de Miguel:", edad_miguel)

###

# ----------------------------------------------------
# 5. Asignación Múltiple Combinada
# ----------------------------------------------------

# Podemos asignar diferentes tipos de datos a variables en una misma línea.
# 'nombre' guarda un texto (Alicia) y 'anos' guarda un número (30).
nombre, anos = "Alicia", 30

# Mostramos la información combinada.
print("Nombre:", nombre)
print("Años:", anos)