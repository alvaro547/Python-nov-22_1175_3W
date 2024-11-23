print(" ")
print("Alvaro Campechano 3W")
print(" ")
def max_de_tres(a, b, c):
    """
    Devuelve el mayor de tres números dados.

    Parámetros:
    a (int, float): Primer número a comparar.
    b (int, float): Segundo número a comparar.
    c (int, float): Tercer número a comparar.

    Retorna:
    int, float: El número mayor entre a, b y c.
    """
    return max(max(a, b), c)

# Ejemplo de uso:
print(max_de_tres(5, 10, 7))  # Debería devolver 10
