"""Ejercicio 02 - Registro de calificaciones"""

# Diccionario: nombre del estudiante -> nota final
notas = {"Carlos": 15, "Elena": 9, "Jorge": 17, "Lucía": 12, "Raúl": 7}

print("Estudiantes registrados:")
for nombre, nota in notas.items():
    print("{}: {}".format(nombre, nota))

# Aprobados: nota mayor o igual a 11
aprobados = [nombre for nombre, nota in notas.items() if nota >= 11]
print("Estudiantes aprobados:", ", ".join(aprobados))

# Promedio general y estudiante con la nota más alta
promedio = sum(notas.values()) / len(notas)
mejor = max(notas, key=notas.get)
print("Promedio general: {:.2f}".format(promedio))
print("Nota más alta: {} ({})".format(notas[mejor], mejor))

# Desaprobados = total - aprobados
print("Estudiantes desaprobados:", len(notas) - len(aprobados))
