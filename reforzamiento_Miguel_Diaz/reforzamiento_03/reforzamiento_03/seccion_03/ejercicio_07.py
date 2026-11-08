"""Ejercicio 07 - Cálculos de un círculo"""

class Circulo:
    PI = 3.1416

    def __init__(self, radio):
        self.radio = radio

    # Valida que el radio sea numérico y mayor que cero
    def es_valido(self):
        if isinstance(self.radio, (int, float)) and self.radio > 0:
            return True
        print("Radio {} inválido: debe ser un número mayor que cero".format(self.radio))
        return False

    def calcular_area(self):
        return self.PI * self.radio ** 2 if self.es_valido() else None

    def calcular_perimetro(self):
        return 2 * self.PI * self.radio if self.es_valido() else None

# Objetos con radios diferentes (dos válidos y dos inválidos)
for circulo in (Circulo(4), Circulo(7.5), Circulo(-2), Circulo("abc")):
    if circulo.es_valido():
        print("Radio {}: área = {:.2f}, perímetro = {:.2f}".format(
            circulo.radio, circulo.calcular_area(), circulo.calcular_perimetro()))
