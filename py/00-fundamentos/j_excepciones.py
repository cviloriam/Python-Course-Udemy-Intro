# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Bloques Try-Except (Manejo de Excepciones)
# Referencia: "A Quick and Easy Intro to Python Programming" por Avinash Jain (Udemy)
# Este código está completamente en español.

# ====================================================
# INTRODUCCIÓN A TRY-EXCEPT (INTENTAR - EXCEPTUAR)
# ====================================================

# Los bloques 'try...except' nos permiten ANTICIPAR y CAPTURAR errores (excepciones)
# que podrían hacer que nuestro programa se detenga bruscamente.
#
# El objetivo es que el programa pueda 'fallar con gracia' en lugar de colapsar.

# ----------------------------------------------------
# ESTRUCTURA BÁSICA
# ----------------------------------------------------

# El bloque 'try' contiene el código que PODRÍA causar un error.
try:
    # La variable 'nombre' NO ha sido definida, por lo que intentar usarla
    # generará un error de 'NameError'. Además, se intenta comparar una
    # cadena (nombre) con un número (3), lo que puede causar un 'TypeError'.
    if nombre > 3:
        print("hola")

# El bloque 'except' contiene el código que se ejecutará SOLAMENTE si ocurre
# una excepción (error) en el bloque 'try'.
except:
    # Como el bloque 'try' fallará, el código salta directamente aquí.
    print("¡Atención! Se detectó un error en tu código. Ejecutando solución alternativa.")

# Si el bloque 'try' NO hubiera fallado, el bloque 'except' se habría ignorado.