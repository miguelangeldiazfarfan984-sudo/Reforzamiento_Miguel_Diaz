# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 13: Operaciones estadísticas con una lista numérica

# 1. Lista vacía
numeros = []

# 2. Agregar diez números enteros uno por uno con append()
numeros.append(12)
numeros.append(7)
numeros.append(33)
numeros.append(18)
numeros.append(25)
numeros.append(40)
numeros.append(9)
numeros.append(14)
numeros.append(51)
numeros.append(26)

# 3. Suma de todos los elementos
suma_total = sum(numeros)

# 4. Promedio aritmético
promedio = suma_total / len(numeros)

# 5. Valor mayor y menor
numero_mayor = max(numeros)
numero_menor = min(numeros)

# 6. Contar pares e impares recorriendo la lista
cantidad_pares = 0
cantidad_impares = 0
for numero in numeros:
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

# 7. Mostrar resultados
print(f"Números registrados: {numeros}")
print(f"Suma total: {suma_total}")
print(f"Promedio: {promedio:.2f}")
print(f"Número mayor: {numero_mayor}")
print(f"Número menor: {numero_menor}")
print(f"Cantidad de pares: {cantidad_pares}")
print(f"Cantidad de impares: {cantidad_impares}")
