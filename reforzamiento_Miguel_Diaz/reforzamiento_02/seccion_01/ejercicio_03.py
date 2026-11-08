# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 03: Evaluación de un sueldo y operaciones con módulo

# 1. Sueldo del trabajador (int)
sueldo = 3175

# 2. Determinar si el sueldo es par o impar
if sueldo % 2 == 0:
    clasificacion = "Número par"
else:
    clasificacion = "Número impar"

# 3. Bono del 12 %
bono = sueldo * 0.12

# 4. Sueldo total con bono
sueldo_total = sueldo + bono

# 5. Residuo de dividir el sueldo entre 7
residuo = sueldo % 7

# 6. Mostrar resultados
print(f"Sueldo inicial: S/ {sueldo}")
print(f"Clasificación: {clasificacion}")
print(f"Bono (12%): S/ {bono:.2f}")
print(f"Sueldo total: S/ {sueldo_total:.2f}")
print(f"Residuo de dividir entre 7: {residuo}")
