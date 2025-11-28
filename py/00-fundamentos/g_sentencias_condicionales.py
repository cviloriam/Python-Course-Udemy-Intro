# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Sentencias Condicionales (Toma de Decisiones)
# Este código está completamente en español.

# ====================================================
# 1. INTRODUCCIÓN A LAS SENTENCIAS CONDICIONALES
# ====================================================

# Las Sentencias Condicionales (if, elif, else) permiten que el programa
# ejecute código solo si ciertas condiciones son VERDADERAS.

# --- Estructura 'si' (if) simple ---
# La condición se evalúa: ¿Es 5 mayor que 3? (Verdadero)
if 5 > 3:
    # Como la condición es Verdadera, este código indentado se ejecuta.
    print("La condición '5 > 3' fue Verdadera: hola")

###

# --- Estructura 'si' (if) y 'si no' (else) ---
# La condición se evalúa: ¿Es 3 menor que 2? (Falso)
if 3 < 2:
    # Este código no se ejecuta.
    print("hola")
else:
    # El bloque 'si no' (else) se ejecuta solo cuando la condición 'if' fue Falsa.
    print("La condición '3 < 2' fue Falsa: La condición no fue verdadera")

# ----------------------------------------------------
# OPERADORES DE RELACIÓN (COMPARACIÓN)
# ----------------------------------------------------
# >   Mayor que
# <   Menor que
# >=  Mayor o igual que
# <=  Menor o igual que
# ==  Igual a (para comparar)
# !=  Diferente de

# ADVERTENCIA IMPORTANTE:
# Recuerda que '=' es ASIGNACIÓN (para guardar un valor).
# '==' es COMPARACIÓN (para preguntar si dos valores son iguales).

# Descomenta las líneas de abajo para ver el error de sintaxis:
# if 5 = 3:
#     print('hola')

###

# --- Uso correcto del operador de igualdad (==) ---
# Condición: ¿Es 5 igual a 3? (Falso)
if 5 == 3:
    # Este código no se ejecuta.
    print('El 5 es igual al 3: hola')

###

# ====================================================
# 2. SENTENCIAS 'SI NO SI' (ELIF)
# ====================================================

# La sentencia 'elif' (else if) permite probar múltiples condiciones
# de forma secuencial. Tan pronto como una condición es Verdadera,
# el programa ejecuta ese bloque y salta el resto de la estructura.

edad = 16

if edad <= 15:
    print("Tienes menos de 16 años") # Falso
elif edad == 16:
    print("Tienes exactamente 16 años") # Verdadero: Se ejecuta y termina aquí.
elif edad == 17:
    print("Tienes exactamente 17 años") # Esta condición ya no se evalúa.
else:
    print("Tienes más de 16 años") # Este bloque ya no se ejecuta.

###

# ====================================================
# 3. OPERADORES LÓGICOS (Y, O)
# ====================================================

# Los operadores lógicos 'and' (y) y 'or' (o) permiten combinar condiciones.

edad = 16

if edad < 13:
    print("Eres un niño") # Falso

# Condición 'y' (and): Ambas subcondiciones deben ser Verdaderas.
# 1. ¿Es 16 mayor o igual a 13? (Verdadero)
# 2. ¿Es 16 menor que 18? (Verdadero)
elif edad >= 13 and edad < 18:
    print("Eres un adolescente") # Verdadero: Se ejecuta.

else:
    print("Eres un adulto")

###

# Condición 'o' (or): Solo UNA de las subcondiciones debe ser Verdadera.
# 1. ¿Es 5 mayor que 3? (Verdadero)
# 2. ¿Es 2 menor que 1? (Falso)
# Como la primera es Verdadera, toda la condición es Verdadera.
if 5 > 3 or 2 < 1:
    print("El operador 'o' fue Verdadero: hola")