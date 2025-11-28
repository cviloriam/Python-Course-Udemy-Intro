# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Diccionarios (Colecciones de Pares Clave-Valor)
# Este código está completamente en español.

# ====================================================
# CONCEPTO BÁSICO DE DICCIONARIOS
# ====================================================

# Los DICCIONARIOS son colecciones que guardan información en pares.
# Piensa en ellos como una guía telefónica: cada NOMBRE es una CLAVE y su
# NÚMERO DE TELÉFONO es el VALOR asociado.

# Características:
# 1. No tienen ORDEN fijo (a diferencia de las Listas).
# 2. Son MUTABLES: se pueden cambiar después de crearlos.
# 3. Se definen usando LLAVES {}.
# 4. Los pares CLAVE: VALOR se separan por dos puntos (:) y, entre pares, por comas (,).

# --- Ejemplo de por qué las Listas no son buenas para datos relacionados: ---
# En una lista es difícil saber qué edad corresponde a qué nombre.
alumnos_lista = ['carlos', 12, 'sofia', 13, 'emilia', 15]
print("Ejemplo en Lista:", alumnos_lista)

###

# ----------------------------------------------------
# 1. CREACIÓN Y ACCESO (CLAVE-VALOR)
# ----------------------------------------------------

# Creamos el mismo conjunto de datos como un DICCIONARIO.
# CLAVE: VALOR
# 'carlos': 12
alumnos_diccionario = {'carlos': 12, 'sofia': 13, 'emilia': 15}
print("Diccionario completo:", alumnos_diccionario)

# Acceso por Clave: Para obtener un valor, usamos la CLAVE entre corchetes [].
# No se usa el índice numérico (0, 1, 2) como en las Listas.
print("Edad de sofia:", alumnos_diccionario['sofia'])
print("Edad de carlos:", alumnos_diccionario['carlos'])

###

# ----------------------------------------------------
# 2. MODIFICAR VALORES
# ----------------------------------------------------

# Para cambiar un valor, accedemos a la clave y le asignamos un nuevo valor.
# Cambiamos la edad de 'sofia' de 13 a 14.
alumnos_diccionario['sofia'] = 14
print("Diccionario después de actualizar:", alumnos_diccionario)

###

# ----------------------------------------------------
# 3. ELIMINAR PARES
# ----------------------------------------------------

# La palabra clave 'del' elimina un par completo (clave y valor) usando la CLAVE.
# Eliminamos el par 'emilia': 15.
del alumnos_diccionario['emilia']
print("Diccionario después de eliminar 'emilia':", alumnos_diccionario)

###

# ----------------------------------------------------
# 4. LONGITUD DEL DICCIONARIO (len)
# ----------------------------------------------------

# La función 'len()' devuelve cuántos pares CLAVE-VALOR tiene el diccionario.
print("Número de pares en el Diccionario:", len(alumnos_diccionario))

###

# ----------------------------------------------------
# 5. CLAVES ÚNICAS
# ----------------------------------------------------

# Las CLAVES en un diccionario DEBEN SER ÚNICAS.
# Si intentas usar la misma clave varias veces, solo se guarda la ÚLTIMA asignación.
alumnos_repetidos = {'carlos': 12, 'carlos': 13, 'carlos': 15}
# El diccionario solo contendrá un 'carlos' con el valor 15.
print("Diccionario con claves repetidas (solo guarda la última):", alumnos_repetidos)