# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 17: Gestión de información de dos usuarios

# 1. Dos listas vacías
usuario_1 = []
usuario_2 = []

# 2 y 3. Registrar Nombre, Apellido paterno, Edad y Profesión con append() e insert()
usuario_1.append("Miguel")
usuario_1.append(29)
usuario_1.insert(1, "Diaz")        # el apellido va en la posición 1
usuario_1.append("Ingeniero")

usuario_2.append("Carla")
usuario_2.append("Rojas")
usuario_2.append("Abogada")
usuario_2.insert(2, 27)            # la edad va en la posición 2

print(f"Usuario 1: {usuario_1}")
print(f"Usuario 2: {usuario_2}")

# 4. Suma de edades (la edad está en el índice 2)
suma_edades = usuario_1[2] + usuario_2[2]
print(f"Suma de edades: {suma_edades}")

# 5. Concatenar ambas listas
lista_concatenada = usuario_1 + usuario_2
print(f"Lista concatenada: {lista_concatenada}")

# 6. Mostrar la lista en orden inverso (sin modificarla)
print(f"Lista en orden inverso: {lista_concatenada[::-1]}")

# 7. Eliminar la edad del primer usuario y el apellido del segundo
lista_final = lista_concatenada.copy()
lista_final.pop(2)                 # edad del primer usuario (índice 2)
lista_final.remove("Rojas")        # apellido paterno del segundo usuario

# 8. Actualizar la profesión del segundo usuario (ahora es el último elemento)
lista_final[-1] = "Gerente de Proyectos"

# 9. Mostrar la lista original concatenada, la final y su cantidad de elementos
print(f"Lista concatenada original: {lista_concatenada}")
print(f"Lista final modificada: {lista_final}")
print(f"Cantidad final de elementos: {len(lista_final)}")
