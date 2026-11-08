"""Ejercicio 03 - Carrito de compras"""

# Precios registrados y productos elegidos por el cliente
precios = {"Monitor": 180, "Cable HDMI": 25, "Webcam": 90, "Parlantes": 60}
carrito = ["Monitor", "Webcam", "Impresora", "Cable HDMI"]

# Recorrer el carrito validando que cada producto exista
print("Productos seleccionados:")
subtotal = 0
for producto in carrito:
    if producto in precios:
        subtotal += precios[producto]
        print("{}: S/ {:.2f}".format(producto, precios[producto]))
    else:
        print("{}: no está registrado, se omite".format(producto))

# Descuento del 10 % si el subtotal supera S/ 200
descuento = subtotal * 0.10 if subtotal > 200 else 0
print("Subtotal: S/ {:.2f}".format(subtotal))
print("Descuento (10 %): S/ {:.2f}".format(descuento))
print("Total a pagar: S/ {:.2f}".format(subtotal - descuento))
