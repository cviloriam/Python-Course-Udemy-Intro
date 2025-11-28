# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Introducción a las Listas (Colecciones de Datos)
# Este código está completamente en español.

# ====================================================
# CONCEPTO BÁSICO DE LISTAS
# ====================================================

# Una LISTA es un tipo de dato que almacena una colección ORDENADA de ítems.
# Son MUTABLES, lo que significa que puedes CAMBIAR, AÑADIR o ELIMINAR sus elementos
# después de crearlas.

# Las listas se definen usando CORCHETES [].
# Los elementos dentro de la lista se separan por COMAS.

# Creamos variables individuales para mostrar que las listas son más eficientes.
articulo1 = 'manzanas'
articulo2 = 'naranjas'
articulo3 = 'bananas'
articulo4 = 'queso'

###

# ----------------------------------------------------
# 1. CREACIÓN, ACCESO Y CORTE (SLICING)
# ----------------------------------------------------

# Creamos una lista llamada 'lista_compras'.
lista_compras = ['manzanas', 'naranjas', 'bananas', 'queso']
print("Lista de compras completa:", lista_compras)

# Acceso por índice: La cuenta de la posición (índice) empieza siempre en 0.
# lista_compras[0] accede al primer elemento: 'manzanas'.
print("Primer elemento (Índice 0):", lista_compras[0])

# lista_compras[2] accede al tercer elemento: 'bananas'.
print("Tercer elemento (Índice 2):", lista_compras[2])

# Corte (Slicing): Acceder a un rango [inicio : fin]. El 'fin' no se incluye.
# [0:2] toma los elementos en la posición 0 y 1 (manzanas y naranjas).
print("Corte [0:2]:", lista_compras[0:2])

# [0:3] toma los elementos 0, 1 y 2 (manzanas, naranjas, bananas).
print("Corte [0:3]:", lista_compras[0:3])

###

# ----------------------------------------------------
# 2. MÉTODO .append() (AÑADIR ELEMENTOS)
# ----------------------------------------------------

# El método '.append()' añade un nuevo elemento al FINAL de la lista.
lista_compras.append('arándanos') # Añade 'arándanos' al final
print("Lista después de añadir:", lista_compras)

###

# ----------------------------------------------------
# 3. ACTUALIZAR ELEMENTOS
# ----------------------------------------------------

# Para cambiar un elemento, accedemos a su índice y le asignamos un nuevo valor.
# Cambiamos el elemento en el índice 0 ('manzanas') por 'cerezas'.
lista_compras[0] = 'cerezas'
print("Lista después de actualizar [0]:", lista_compras)

###

# ----------------------------------------------------
# 4. ELIMINAR ELEMENTOS
# ----------------------------------------------------

# La palabra clave 'del' elimina un elemento usando su índice.
# Eliminamos el elemento en el índice 1, que ahora es 'naranjas'.
del lista_compras[1]
print("Lista después de eliminar [1]:", lista_compras)

###

# ----------------------------------------------------
# 5. LONGITUD DE LA LISTA (len)
# ----------------------------------------------------

# La función 'len()' devuelve cuántos elementos tiene la lista.
print("Longitud de la lista:", len(lista_compras))

###

# ----------------------------------------------------
# 6. OPERACIONES CON LISTAS (CONCATENACIÓN Y REPETICIÓN)
# ----------------------------------------------------

lista_compras2 = ['pan', 'mermelada', 'mantequilla de cacahuete']

# El operador '+' CONCATENA (une) dos listas para formar una nueva.
print("Unión de listas (+):", lista_compras + lista_compras2)

# El operador '*' REPLICA los elementos de la lista el número de veces indicado.
print("Repetición de lista (*2):", lista_compras * 2)

###

# ----------------------------------------------------
# 7. FUNCIONES ÚTILES CON LISTAS NUMÉRICAS
# ----------------------------------------------------

lista_numeros = [1, 4, 7, 23, 6]

# max(): Encuentra el número más grande en la lista.
print("Número Máximo:", max(lista_numeros))

# min(): Encuentra el número más pequeño en la lista.
print("Número Mínimo:", min(lista_numeros))