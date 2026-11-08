# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 07: Conversión de temperaturas

# 1. Dos temperaturas en grados Celsius (float)
celsius_1 = 25.5
celsius_2 = 8.0

# 2. Conversión a Fahrenheit: F = (C * 9/5) + 32
fahrenheit_1 = (celsius_1 * 9 / 5) + 32
fahrenheit_2 = (celsius_2 * 9 / 5) + 32

# 3. Conversión a Kelvin: K = C + 273.15
kelvin_1 = celsius_1 + 273.15
kelvin_2 = celsius_2 + 273.15

# 4. Diferencia entre ambas temperaturas en Celsius
diferencia = celsius_1 - celsius_2

# 5. Mostrar resultados
print(f"Temperatura 1: {celsius_1} °C")
print(f"Fahrenheit: {fahrenheit_1:.2f} °F")
print(f"Kelvin: {kelvin_1:.2f} K")
print(f"Temperatura 2: {celsius_2} °C")
print(f"Fahrenheit: {fahrenheit_2:.2f} °F")
print(f"Kelvin: {kelvin_2:.2f} K")
print(f"Diferencia de temperaturas: {diferencia:.2f} °C")
