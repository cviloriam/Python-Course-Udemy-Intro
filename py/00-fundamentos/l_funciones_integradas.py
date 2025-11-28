# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Funciones Integradas de Python
# Este código está completamente en español.

# ====================================================
# FUNCIONES INTEGRADAS (Built-in Functions)
# ====================================================

# Python ya tiene muchas funciones predefinidas que podemos usar directamente
# sin necesidad de importarlas o definirlas.

# ----------------------------------------------------
# 1. abs(), bool(), dir(), help()
# ----------------------------------------------------

# abs(): Devuelve el valor absoluto (sin signo) de un número.
print("abs(-23):", abs(-23)) # Resultado: 23

# bool(): Convierte un valor a Booleano (Verdadero o Falso).
# 0, None, listas/cadenas vacías siempre son Falso. Cualquier otro valor es Verdadero.
print("bool(0):", bool(0))        # Resultado: False
print("bool(100):", bool(100))    # Resultado: True
print("bool(None):", bool(None))  # Resultado: False (None es el equivalente a 'Nada')

# dir(): Devuelve una lista de los atributos y métodos disponibles para un objeto.
# Útil para ver qué podemos hacer con un tipo de dato (como la cadena 'hola').
print("\ndir('hola'):", dir('hola'))

# help(): Muestra la documentación o ayuda sobre una función o método.
# Mostramos la ayuda sobre el método '.upper()' de las cadenas de texto.
print("\nhelp('hola'.upper):")
print(help('hola'.upper))

###

# ----------------------------------------------------
# 2. eval() y exec() (Ejecución de Código)
# ----------------------------------------------------

# Estas funciones son avanzadas y permiten ejecutar código Python escrito como texto.
# ¡Deben usarse con precaución, ya que representan un riesgo de seguridad!

sentencia = "print('¡Hola desde eval!')"

# eval(): Evalúa y ejecuta una ÚNICA expresión Python (ej. una operación matemática).
# En este caso, la expresión es la llamada a la función print.
print("eval(sentencia):")
eval(sentencia)

# exec(): Ejecuta una cadena de texto como un BLOQUE completo de código Python.
print("exec(sentencia):")
exec(sentencia)

###

# ----------------------------------------------------
# 3. CONVERSIÓN DE TIPOS (str(), int(), float())
# ----------------------------------------------------

# str(): Convierte un valor a una cadena de texto (String).
# Necesario para concatenar (pegar) números con texto.
print("str(100):", str(100))
print("Concatenación con str():", "hola " + str(100))

# int(): Convierte un valor (ej. una cadena) a un número entero.
# Esto nos permite realizar operaciones matemáticas.
# La cadena "123" se convierte en el número 123.
print("int('123') + 456:", int("123") + 456) # Resultado: 579

# float(): Convierte un valor (ej. una cadena) a un número decimal (flotante).
# La cadena "123.45" se convierte en el número 123.45.
print("float('123.45') + 0.23:", float("123.45") + 0.23) # Resultado: 123.68