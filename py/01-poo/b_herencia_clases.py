# ====================================================
# METADATOS DEL ARCHIVO
# ====================================================

# Autor del Código: Carlos Viloria
# Fecha de Creación: 28 de Noviembre de 2025
# Repositorio de GitHub: https://github.com/cviloriam/Python-Course-Udemy-Intro

# Módulo del Curso: Herencia de Clases (Reutilización de Código)
# Este código está completamente en español.

# ====================================================
# CONCEPTO DE HERENCIA
# ====================================================

# La HERENCIA es una característica de la POO que permite crear nuevas clases
# (llamadas SUBCLASES o Clases HIJAS) basadas en clases ya existentes
# (llamadas SUPERCLASES o Clases PADRES).
#
# El objetivo es REUTILIZAR código y evitar reescribir propiedades y métodos.

# ----------------------------------------------------
# 1. CLASE PADRE (SUPERCLASE)
# ----------------------------------------------------

class Coche:
    # El constructor define las propiedades básicas que todo coche debe tener.
    def __init__(self):
        self.ruedas = 4
        self.asientos = 5

    # Método básico de comportamiento.
    def conducir(self):
        print("Conduciendo un coche...")

# Creamos un objeto de la clase Padre.
miCoche = Coche()
miCoche.conducir() # Resultado: "Conduciendo un coche..."

###

# ----------------------------------------------------
# 2. CLASE HIJA (SUBCLASE) CON ANULACIÓN DE MÉTODO
# ----------------------------------------------------

# 'CocheDeportivo' hereda de 'Coche', lo que significa que ya tiene 'ruedas' y 'asientos'.
class CocheDeportivo(Coche):
    def __init__(self):
        # La función 'super().__init__()' llama al constructor de la clase Padre ('Coche').
        # Esto asegura que las propiedades de la clase Padre (ruedas=4, asientos=5)
        # se inicialicen primero.
        super().__init__()

        # Sobrescribimos o añadimos propiedades específicas del Deportivo.
        self.potencia_motor = '400 HP'
        self.asientos = 2 # Sobrescribimos el valor de 'asientos' del Padre.

    # Anulamos (Sobrescribimos) el método 'conducir' del Padre.
    # El objeto CocheDeportivo tendrá su propia forma de conducir.
    def conducir(self):
        print("Conduciendo un coche deportivo... ¡Rápido!")

# Creamos un objeto de la clase Hija.
miCocheDeportivo = CocheDeportivo()
miCocheDeportivo.conducir() # Resultado: "Conduciendo un coche deportivo... ¡Rápido!"

###

# ----------------------------------------------------
# 3. CLASE HIJA SIN ANULACIÓN DE MÉTODO
# ----------------------------------------------------

# El mismo CocheDeportivo, pero esta vez NO definimos el método 'conducir'.
class CocheDeportivo(Coche):
    def __init__(self):
        super().__init__()
        self.potencia_motor = '400 HP'
        self.asientos = 2

# Creamos un objeto de esta nueva clase Hija.
miOtroCocheDeportivo = CocheDeportivo()

# Como no definimos 'conducir' en la Clase Hija, Python busca el método
# en la Clase Padre ('Coche') y ejecuta ese.
miOtroCocheDeportivo.conducir() # Resultado: "Conduciendo un coche..."