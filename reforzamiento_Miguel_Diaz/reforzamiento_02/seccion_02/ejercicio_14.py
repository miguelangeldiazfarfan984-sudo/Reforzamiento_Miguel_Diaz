# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 14: Administración de estudiantes

# 1. Lista con cinco estudiantes
estudiantes = ["Sofía", "Andrés", "Lucía", "Renato", "Daniela"]
lista_original = estudiantes.copy()   # se guarda la lista original para mostrarla

# 2. Estudiante que se desea buscar
estudiante_buscado = "Lucía"

# 3. Comprobar si el estudiante existe
if estudiante_buscado in estudiantes:
    estudiantes.remove(estudiante_buscado)   # se elimina con remove()
    resultado = "Estudiante eliminado correctamente."
else:
    estudiantes.append(estudiante_buscado)   # se agrega con append()
    resultado = "Estudiante no encontrado. Se agregó a la lista."

# 4. Insertar un estudiante adicional en la segunda posición (índice 1)
nuevo_estudiante = "Mateo"
estudiantes.insert(1, nuevo_estudiante)

# 5. Mostrar resultados
print(f"Lista original: {lista_original}")
print(f"Estudiante buscado: {estudiante_buscado}")
print(f"Resultado: {resultado}")
print(f"Nuevo estudiante insertado: {nuevo_estudiante}")
print(f"Lista actualizada: {estudiantes}")
print(f"Cantidad de estudiantes: {len(estudiantes)}")
