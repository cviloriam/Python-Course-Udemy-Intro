# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Bucles 'for' (Repetición de Código)
# Este código está completamente en español.

# ====================================================
# CONCEPTO BÁSICO DE BUCLES 'FOR'
# ====================================================

# Los bucles 'for' (para) permiten ejecutar un bloque de código repetidamente.
# Se usan principalmente para ITERAR (recorrer) sobre una secuencia de elementos
# como listas, tuplas o un rango de números.

# La sintaxis es: 'for' [variable temporal] 'in' [secuencia]:

lista1 = ['manzanas', 'bananas', 'cerezas']
tupla1 = (2, 6, 10)

# --- Iterar sobre una Lista ---
# El bucle se repite tantas veces como elementos haya en 'lista1'.
# En cada repetición, 'elemento' toma el valor del ítem actual.
for elemento in lista1:
    print("Elemento de la lista:", elemento)

# --- Iterar sobre una Tupla ---
# Funciona igual que con las listas.
for elemento in tupla1:
    print("Elemento de la tupla:", elemento)

###

# ====================================================
# 2. LA FUNCIÓN range() (GENERAR SECUENCIAS DE NÚMEROS)
# ====================================================

# La función range() es muy útil para repetir un bloque de código un número fijo de veces
# o para generar secuencias numéricas.

# --- range(fin) ---
# range(10) genera números desde 0 hasta 9 (un total de 10 números).
# El 'fin' (10) NO se incluye.
for i in range(10):
    print("Secuencia 0 a 9:", i)

###

# --- range(inicio, fin) ---
# Genera números desde el 'inicio' (1) hasta el 'fin' (11, no incluido).
# Imprime del 1 al 10.
for i in range(1, 11):
    print("Secuencia 1 a 10:", i)

###

# --- range(inicio, fin, paso) ---
# El tercer argumento 'paso' (step) indica de cuánto en cuánto debe saltar.
# Empieza en 0, va hasta 11 (no incluido), saltando de 2 en 2. (0, 2, 4, 6, 8, 10)
for i in range(0, 11, 2):
    print("Secuencia de 2 en 2:", i)

###

# Ejemplo de conteo de 5 en 5 (Tablas de multiplicar)
# Empieza en 5, va hasta 51 (no incluido), saltando de 5 en 5. (5, 10, 15... 50)
for i in range(5, 51, 5):
    print("Múltiplos de 5:", i)

###

# Repetición simple: Si solo se necesita el bucle para repetir algo 5 veces.
# Aunque 'i' no se use, el bloque de código se repite 5 veces (para i = 0, 1, 2, 3, 4).
for i in range(5):
    print("Esta frase se repite 5 veces.")

###

# ====================================================
# 3. BUCLES ANIDADOS (BUCLES DENTRO DE OTROS BUCLES)
# ====================================================

# Un bucle 'anidado' es un bucle dentro del cuerpo de otro bucle.
# Por cada repetición del bucle EXTERNO (i), el bucle INTERNO (j) se completa
# totalmente.

# Bucle externo se repite 5 veces (i = 0, 1, 2, 3, 4).
for i in range(5):
    # Bucle interno se repite 3 veces (j = 0, 1, 2) por cada valor de 'i'.
    for j in range(3):
        # Muestra el resultado de i * j (ej: 0*0, 0*1, 0*2, luego 1*0, 1*1, 1*2, etc.)
        print(f"Resultado de {i} * {j} = {i * j}")