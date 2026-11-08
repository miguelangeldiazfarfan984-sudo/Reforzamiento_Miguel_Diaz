# Miguel Angel Diaz Farfan
# Reforzamiento 01 - Ejercicio 03: Conversión de cadenas y operaciones numéricas
# 1. Variable str que contiene un número entero positivo
primer_valor_texto = "42"

# 2. Variable int con otro valor numérico
segundo_valor = 18

# 3. Convertir la primera variable a int para poder operar
primer_valor = int(primer_valor_texto)

# 4. Suma y multiplicación de ambos valores
suma = primer_valor + segundo_valor
multiplicacion = primer_valor * segundo_valor

# 5. Promedio de los dos números
promedio = suma / 2

# 6. Convertir la suma a str y concatenarla con el mensaje
resultado_final = "El resultado final es: " + str(suma)

# 7. Mostrar los resultados
print(f"Primer valor: {primer_valor}")
print(f"Segundo valor: {segundo_valor}")
print(f"Suma: {suma}")
print(f"Multiplicación: {multiplicacion}")
print(f"Promedio: {promedio:.2f}")
print(f"Tipo de dato convertido: {type(primer_valor)}")
print(resultado_final)