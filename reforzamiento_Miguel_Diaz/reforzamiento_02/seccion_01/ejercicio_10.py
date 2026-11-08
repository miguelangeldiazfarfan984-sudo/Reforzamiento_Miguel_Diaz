# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 10: Conversión numérica y verificación de múltiplos

# 1. Dos valores float positivos
valor_decimal_1 = 84.6
valor_decimal_2 = 12.3

# 2. Convertir ambos valores a int
entero_1 = int(valor_decimal_1)
entero_2 = int(valor_decimal_2)

# 3. Mostrar valores originales y convertidos
print(f"Primer valor decimal: {valor_decimal_1}")
print(f"Segundo valor decimal: {valor_decimal_2}")
print(f"Primer entero: {entero_1}")
print(f"Segundo entero: {entero_2}")

# El segundo entero no puede ser cero para evitar una división entre cero
if entero_2 != 0:
    # 4. Comprobar si el primero es múltiplo del segundo con el módulo
    residuo = entero_1 % entero_2
    if residuo == 0:
        es_multiplo = "Sí"
    else:
        es_multiplo = "No"

    # 5. Cociente de ambos enteros
    cociente = entero_1 / entero_2

    # 6. Mostrar resultados
    print(f"¿El primer número es múltiplo del segundo?: {es_multiplo}")
    print(f"Residuo: {residuo}")
    print(f"Cociente: {cociente:.2f}")
else:
    print("El segundo número es cero: no se puede dividir.")
