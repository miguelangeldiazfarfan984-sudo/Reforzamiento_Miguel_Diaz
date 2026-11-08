# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 12: Actualización de una lista de departamentos

# 1. Lista con seis departamentos del Perú
departamentos = ["Loreto", "Cajamarca", "Junín", "Tacna", "Lambayeque", "Ayacucho"]

# 2. Mostrar la lista original
print(f"Lista original: {departamentos}")

# 3. Departamento que se desea buscar y reemplazar
departamento_buscar = "Junín"

# 4. Nuevo departamento
departamento_nuevo = "Huánuco"

print(f"Departamento a reemplazar: {departamento_buscar}")
print(f"Nuevo departamento: {departamento_nuevo}")

# 5. Verificar si el departamento existe en la lista
if departamento_buscar in departamentos:
    # 6. Reemplazarlo usando su índice
    indice = departamentos.index(departamento_buscar)
    departamentos[indice] = departamento_nuevo
    print(f"Lista actualizada: {departamentos}")
else:
    # 7. Si no existe, se conserva la lista original
    print(f"El departamento {departamento_buscar} no fue encontrado.")
    print(f"Lista final: {departamentos}")

# 8. Cantidad de elementos
print(f"Cantidad de departamentos: {len(departamentos)}")
