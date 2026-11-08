# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 02: Cálculo del volumen de una esfera

# 1. Radio de la esfera (float)
radio_1 = 4.2

# 2. Valor de pi
pi = 3.14159

# 3. Diámetro de la primera esfera
diametro_1 = radio_1 * 2

# 4. Volumen: V = (4/3) * pi * radio^3
volumen_1 = (4 / 3) * pi * radio_1 ** 3

# 5. Segunda esfera con el doble del radio
radio_2 = radio_1 * 2
volumen_2 = (4 / 3) * pi * radio_2 ** 3

# 6. Mostrar resultados
print(f"Radio de la primera esfera: {radio_1}")
print(f"Diámetro de la primera esfera: {diametro_1}")
print(f"Volumen de la primera esfera: {volumen_1:.2f}")
print(f"Radio de la segunda esfera: {radio_2}")
print(f"Volumen de la segunda esfera: {volumen_2:.2f}")
