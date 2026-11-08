"""Ejercicio 06 - Análisis de ventas semanales"""

ventas = [210, 145, 330, 190, 275, 160, 240]

# Total vendido en la semana
def total_ventas(lista):
    return sum(lista)

# Promedio diario de ventas
def promedio_ventas(lista):
    return total_ventas(lista) / len(lista)

# Venta más alta de la semana
def venta_maxima(lista):
    return max(lista)

# Cantidad de días que superaron el promedio
def dias_sobre_promedio(lista):
    return len([venta for venta in lista if venta > promedio_ventas(lista)])

print("Total vendido en la semana: S/ {:.2f}".format(total_ventas(ventas)))
print("Promedio diario de ventas: S/ {:.2f}".format(promedio_ventas(ventas)))
print("Venta máxima de la semana: S/ {:.2f}".format(venta_maxima(ventas)))
print("Días que superaron el promedio: {}".format(dias_sobre_promedio(ventas)))
