# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 08: Conversión de soles a dólares

# 1. Tipo de cambio (soles por cada dólar)
tipo_cambio = 3.72

# 2. Tres montos en soles
monto_1 = 120.00
monto_2 = 275.50
monto_3 = 510.00

# 3. Convertir cada monto a dólares
dolares_1 = monto_1 / tipo_cambio
dolares_2 = monto_2 / tipo_cambio
dolares_3 = monto_3 / tipo_cambio

# 4. Suma total en soles
total_soles = monto_1 + monto_2 + monto_3

# 5. Total convertido a dólares
total_dolares = total_soles / tipo_cambio

# 6. Mostrar resultados
print(f"Tipo de cambio: S/ {tipo_cambio:.2f}")
print(f"Monto 1: S/ {monto_1:.2f} -> USD {dolares_1:.2f}")
print(f"Monto 2: S/ {monto_2:.2f} -> USD {dolares_2:.2f}")
print(f"Monto 3: S/ {monto_3:.2f} -> USD {dolares_3:.2f}")
print(f"Total en soles: S/ {total_soles:.2f}")
print(f"Total en dólares: USD {total_dolares:.2f}")
