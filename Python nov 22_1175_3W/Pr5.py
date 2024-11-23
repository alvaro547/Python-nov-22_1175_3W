print(" ")
print("Alvaro Campechano 3W")
print(" ")
def suma(lista):
    """
    Suma todos los números en una lista.

    Parámetros:
    lista (list): Lista de números (enteros o flotantes).

    Retorna:
    int, float: La suma de todos los números en la lista.
    """
    total = 0
    for num in lista:
        total += num
    return total

def multip(lista):
    """
    Multiplica todos los números en una lista.

    Parámetros:
    lista (list): Lista de números (enteros o flotantes).

    Retorna:
    int, float: El producto de todos los números en la lista.
    """
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

# Ejemplo de uso:
print(suma([1, 2, 3, 4]))  # Debería devolver 10
print(multip([1, 2, 3, 4]))  # Debería devolver 24
