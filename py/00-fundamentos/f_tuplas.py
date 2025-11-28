# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Introducción a las Tuplas (Colecciones Inmutables)
# Este código está completamente en español.

# ====================================================
# CONCEPTO BÁSICO DE TUPLAS
# ====================================================

# Las TUPLAS son colecciones de ítems muy similares a las Listas, pero con
# una diferencia fundamental: son INMUTABLES.
#
# INMUTABLE significa que una vez que la tupla ha sido creada,
# NO puedes cambiar, añadir o eliminar sus elementos.
#
# Las tuplas se definen usando PARÉNTESIS ().
# Los elementos se separan por comas.

# ----------------------------------------------------
# 1. CREACIÓN, ACCESO E INMUTABILIDAD
# ----------------------------------------------------

# Creamos una tupla de frutas.
tupla_frutas = ('naranjas', 'manzanas', 'bananas')
print("Tupla completa:", tupla_frutas)

# Acceso por índice: Al igual que las Listas, la cuenta comienza en 0.
print("Primer elemento (Índice 0):", tupla_frutas[0]) # Resultado: 'naranjas'

# Corte (Slicing): También funciona igual que en las Listas [inicio : fin (no incluido)].
print("Corte [0:2]:", tupla_frutas[0:2]) # Resultado: ('naranjas', 'manzanas')

# --- INMUTABILIDAD ---
# Intento de cambiar el primer elemento de la tupla:
# tupla_frutas[0] = 'cerezas'
# Descomentar la línea de arriba causará un error (TypeError),
# ya que las tuplas no soportan la asignación de elementos (son inmutables).
# Se deja como comentario para evitar errores de ejecución en el script.

###

# ----------------------------------------------------
# 2. OPERACIONES: CONCATENACIÓN
# ----------------------------------------------------

# Aunque no puedes cambiar una tupla existente, sí puedes crear una NUEVA
# tupla uniendo (concatenando) dos o más tuplas con el operador '+'.

tupla_numeros = (12, 14)

# Concatenamos la tupla de frutas y la tupla de números.
tupla_combinada = tupla_frutas + tupla_numeros
print("Tupla combinada (+):", tupla_combinada)

# NOTA: La tupla_frutas original y tupla_numeros siguen sin modificarse.
# Solo hemos creado una tupla completamente nueva.