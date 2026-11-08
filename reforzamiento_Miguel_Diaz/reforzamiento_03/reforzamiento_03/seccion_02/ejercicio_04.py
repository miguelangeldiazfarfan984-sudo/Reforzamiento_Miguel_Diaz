"""Ejercicio 04 - Suma de dígitos y comparación"""

# Retorna la suma de los dígitos de un entero positivo
def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

numero_1, numero_2 = 726, 315
suma_1, suma_2 = suma_digitos(numero_1), suma_digitos(numero_2)
print("Suma de dígitos de {}: {}".format(numero_1, suma_1))
print("Suma de dígitos de {}: {}".format(numero_2, suma_2))

# Comparar cuál tiene mayor suma o si hay empate
if suma_1 == suma_2:
    print("Existe un empate")
else:
    print("Mayor suma de dígitos: {}".format(numero_1 if suma_1 > suma_2 else numero_2))

# Números cuya suma de dígitos es menor que 10
for numero, suma in ((numero_1, suma_1), (numero_2, suma_2)):
    if suma < 10:
        print("{} tiene una suma de dígitos menor que 10".format(numero))
