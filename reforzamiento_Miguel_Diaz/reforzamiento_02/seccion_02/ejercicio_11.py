# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 11: Registro de estudiantes

# 1. Lista vacía
estudiantes = []

# 2. Cantidad prevista de estudiantes
cantidad_estudiantes = 4

# 3. Cuatro nombres de estudiantes
estudiante_1 = "Valeria"
estudiante_2 = "Diego"
estudiante_3 = "Camila"
estudiante_4 = "Jorge"

# 4. Agregar los nombres uno por uno con append()
estudiantes.append(estudiante_1)
estudiantes.append(estudiante_2)
estudiantes.append(estudiante_3)
estudiantes.append(estudiante_4)

# 6. Comprobar si la cantidad registrada coincide con la prevista
total_registrados = len(estudiantes)
if total_registrados == cantidad_estudiantes:
    coincide = "Sí"
else:
    coincide = "No"

# 8. Orden inverso sin modificar la lista original
orden_inverso = estudiantes[::-1]

# 5, 6 y 7. Mostrar resultados
print(f"Cantidad de estudiantes prevista: {cantidad_estudiantes}")
print(f"Estudiantes registrados: {estudiantes}")
print(f"Total de estudiantes registrados: {total_registrados}")
print(f"¿Coincide con la cantidad prevista?: {coincide}")
print(f"Primer estudiante: {estudiantes[0]}")
print(f"Último estudiante: {estudiantes[-1]}")
print(f"Orden inverso: {orden_inverso}")
