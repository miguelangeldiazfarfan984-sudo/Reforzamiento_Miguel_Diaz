"""Ejercicio 01 - Control de inventario"""

# Listas paralelas: productos y sus cantidades (mismo orden)
productos = ["Pan", "Huevos", "Atún", "Yogurt", "Lentejas"]
cantidades = [10, 4, 7, 1, 11]

# Mostrar cada producto con su cantidad
print("Productos registrados:")
for producto, cantidad in zip(productos, cantidades):
    print("{}: {} unidades".format(producto, cantidad))

# Total de unidades registradas
print("Total de unidades disponibles:", sum(cantidades))

# Productos con stock bajo (menos de 5 unidades)
stock_bajo = [(p, c) for p, c in zip(productos, cantidades) if c < 5]
if stock_bajo:
    print("Productos con menos de 5 unidades:")
    for producto, cantidad in stock_bajo:
        print("- {}: {} unidades".format(producto, cantidad))
else:
    print("Ningún producto tiene stock bajo")
