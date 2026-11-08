# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 15: Eliminación de elementos duplicados

# 1. Lista con cinco empresas tecnológicas
empresas = ["Apple", "Nvidia", "Samsung", "Intel", "Cisco"]

# 2. Copia independiente con copy()
empresas_ampliada = empresas.copy()

# 3. Tres empresas adicionales (dos ya existen en la lista original)
empresa_extra_1 = "Nvidia"
empresa_extra_2 = "Intel"
empresa_extra_3 = "Adobe"
empresas_ampliada.append(empresa_extra_1)
empresas_ampliada.append(empresa_extra_2)
empresas_ampliada.append(empresa_extra_3)

# 4. Nueva lista sin repetidos, manteniendo el orden de primera aparición
empresas_sin_duplicados = []
for empresa in empresas_ampliada:
    if empresa not in empresas_sin_duplicados:
        empresas_sin_duplicados.append(empresa)

# 6. Cantidad de elementos repetidos eliminados
duplicados_eliminados = len(empresas_ampliada) - len(empresas_sin_duplicados)

# 5. Mostrar resultados
print(f"Lista original: {empresas}")
print(f"Lista con nuevos elementos: {empresas_ampliada}")
print(f"Lista sin duplicados: {empresas_sin_duplicados}")
print(f"Elementos duplicados eliminados: {duplicados_eliminados}")
