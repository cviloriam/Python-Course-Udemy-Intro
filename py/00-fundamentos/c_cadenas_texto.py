# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Formato y Marcadores de Posición en Cadenas de Texto
# Este código está completamente en español.

# ====================================================
# 1. MÉTODO BÁSICO: CONCATENACIÓN CON EL OPERADOR +
# ====================================================

# La forma más sencilla de añadir variables a una frase es con el operador '+',
# pero requiere que los números se conviertan a texto y puede ser confuso.
nombre = "carlos"
print(nombre + " tiene 15 años")

###

# ====================================================
# 2. MÉTODO ANTIGUO: FORMATO % (OPERADOR MODULO)
# ====================================================

# Este es un método de formateo más antiguo que usa marcadores de posición especiales
# para indicar dónde deben ir los valores.

nombre = "carlos"
# %s es el marcador de posición para una cadena de texto (string).
frase = "%s tiene 15 años"

# El operador % indica a Python que inserte el valor de 'nombre' en el %s.
print("Formato %s:", frase % nombre)

###

# Asignación de múltiples marcadores %s
frase = "%s %s fue presidente de los Estados Unidos"

# Se usa una TUPLA (valores entre paréntesis) para pasar los valores en el orden correcto.
print("Múltiples %s:", frase % ("Barack", "Obama"))

###

# Marcadores para diferentes TIPOS DE DATOS:
# %s: Cadena de texto (string)
# %d: Número entero (decimal/integer)
nombre = "avi"
edad = 23
frase = "%s tiene %d años"

# CORRECCIÓN: El operador correcto para el formato % es el símbolo % (módulo), no '&'.
# Se pasa una tupla (nombre, edad) con todos los valores.
print("Combinando %s y %d:", frase % (nombre, edad))

###

# ====================================================
# 3. MÉTODO MODERNO Y RECOMENDADO: f-STRINGS
# ====================================================

# El método más moderno y fácil de leer es usando 'f-strings' (cadenas f).
# Se añade una 'f' antes de las comillas y se incluye la variable directamente
# entre llaves {}.

nombre = "avi"
print(f"Saludo con f-string: Hola, {nombre}")

###

# Los f-strings también permiten incluir expresiones y operaciones directamente.
x = 10
y = 20

# Python calculará 'x + y' y pondrá el resultado (30) dentro de la cadena.
print(f"Operación en f-string: La suma de x y y es {x + y}")