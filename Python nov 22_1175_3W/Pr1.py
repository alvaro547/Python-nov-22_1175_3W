print(" ")
print("Alvaro Campechano 3W")
print(" ")
def max(a, b):
    """
    Devuelve el mayor de los dos números dados.

    Parámetros:
    a (int, float): Primer número a comparar.
    b (int, float): Segundo número a comparar.

    Retorna:
    int, float: El número mayor entre a y b.
    """
    if a > b:
        return a
    else:
        return b

# Ejemplo de uso:
print(max(5, 10))  # Debería devolver 10
