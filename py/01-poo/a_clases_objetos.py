# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Programación Orientada a Objetos (POO): Clases y Objetos
# Este código está completamente en español.

# ====================================================
# INTRODUCCIÓN A CLASES Y OBJETOS
# ====================================================

# La Programación Orientada a Objetos (POO) se basa en el concepto de "objetos".
#
# CLASE: Es un MOLDE o PLANTILLA para crear objetos. Define las propiedades
#        (atributos) y los comportamientos (métodos) comunes.
# OBJETO: Es una INSTANCIA real de una clase. Es el elemento funcional.

# ----------------------------------------------------
# 1. CLASE BÁSICA Y CREACIÓN DE OBJETO
# ----------------------------------------------------

# Definimos la plantilla 'Persona' usando la palabra clave 'class'.
class Persona:
    # La palabra clave 'pass' se usa cuando la clase no tiene ningún código todavía.
    pass

# Creamos un objeto 'p' que es una instancia de la clase 'Persona'.
# Esto se llama INSTANCIACIÓN.
p = Persona()
print("El objeto creado:", p)
# Al imprimir, Python muestra el tipo de objeto (Persona) y su ubicación en memoria.

###

# ----------------------------------------------------
# 2. CLASE CON ATRIBUTOS Y MÉTODOS
# ----------------------------------------------------

class Persona:
    # El método especial '__init__' (constructor) se ejecuta AUTOMÁTICAMENTE
    # cuando se crea un nuevo objeto. Se usa para definir sus propiedades iniciales.
    # 'self' es una referencia al objeto que se está creando (es obligatorio).
    def __init__(self, nombre, edad):
        # ATRIBUTOS (Propiedades): Guardamos los valores pasados en el objeto.
        # self.nombre y self.edad son las propiedades internas del objeto.
        self.nombre = nombre
        self.edad = edad

    # MÉTODO (Comportamiento): Define una acción que el objeto puede realizar.
    # Siempre incluye 'self' como primer argumento.
    def obtenerNombre(self):
        # Retorna el valor del atributo interno 'nombre'.
        return self.nombre

    def obtenerEdad(self):
        # Retorna el valor del atributo interno 'edad'.
        return self.edad

# Creamos la primera instancia (objeto) 'p1' y le pasamos los datos iniciales.
p1 = Persona("Roberto", 22)
print("\nObjeto con atributos:", p1)

# Usamos los MÉTODOS para interactuar con los datos internos del objeto.
print("El nombre del objeto p1 es:", p1.obtenerNombre())
print("La edad del objeto p1 es:", p1.obtenerEdad())