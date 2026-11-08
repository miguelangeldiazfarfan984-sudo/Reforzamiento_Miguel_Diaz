# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 04: Promedio de calificaciones

# 1. Cinco calificaciones (float) entre 0 y 20
nota_1 = 16.0
nota_2 = 13.5
nota_3 = 18.5
nota_4 = 11.0
nota_5 = 15.0

# 2. Suma de las calificaciones
suma_notas = nota_1 + nota_2 + nota_3 + nota_4 + nota_5

# 3. Promedio aritmético
promedio = suma_notas / 5

# 4. Diferencia entre la nota más alta y la más baja
nota_mayor = max(nota_1, nota_2, nota_3, nota_4, nota_5)
nota_menor = min(nota_1, nota_2, nota_3, nota_4, nota_5)
diferencia = nota_mayor - nota_menor

# 5. Estado del estudiante (nota mínima 11)
if promedio >= 11:
    estado = "APROBADO"
else:
    estado = "DESAPROBADO"

# 6. Mostrar resultados
print(f"Notas: {nota_1}, {nota_2}, {nota_3}, {nota_4}, {nota_5}")
print(f"Suma de notas: {suma_notas}")
print(f"Promedio: {promedio:.2f}")
print(f"Diferencia entre nota mayor y menor: {diferencia:.2f}")
print(f"Estado: {estado}")
