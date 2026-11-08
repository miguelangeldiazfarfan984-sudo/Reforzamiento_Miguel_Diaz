"""Ejercicio 05 - Eliminación de un elemento de una lista"""

# Retorna una nueva lista sin la primera aparición del valor
def eliminar_valor(lista, valor):
    nueva_lista = lista.copy()  # copia para no modificar la original
    if valor in nueva_lista:
        nueva_lista.remove(valor)
    return nueva_lista

numeros = [5, 15, 25, 15, 35]

# Prueba con un valor existente (15) y otro inexistente (99)
for valor in (15, 99):
    print("Original: {} | Buscado: {} | Resultado: {}".format(numeros, valor, eliminar_valor(numeros, valor)))
