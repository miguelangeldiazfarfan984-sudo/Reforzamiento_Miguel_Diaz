# Nombre: Miguel Angel Diaz Farfan
# Reforzamiento 02 - Ejercicio 06: Cálculo del importe de una compra

# 1. Datos de la compra
cliente = "Miguel Diaz"
producto = "Ceviche mixto"
precio_unitario = 38.90
cantidad = 4

# 2. Subtotal
subtotal = precio_unitario * cantidad

# 3. Descuento del 10 % si la cantidad es 3 o más
if cantidad >= 3:
    porcentaje_descuento = 0.10
else:
    porcentaje_descuento = 0.0

# 4. Importe del descuento y total a pagar
descuento = subtotal * porcentaje_descuento
total_pagar = subtotal - descuento

# 5. Mostrar resultados
print(f"Cliente: {cliente}")
print(f"Producto: {producto}")
print(f"Precio unitario: S/ {precio_unitario:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: S/ {subtotal:.2f}")
print(f"Descuento ({porcentaje_descuento * 100:.0f}%): S/ {descuento:.2f}")
print(f"Total a pagar: S/ {total_pagar:.2f}")
