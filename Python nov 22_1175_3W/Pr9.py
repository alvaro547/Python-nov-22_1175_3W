print(" ")
print("Alvaro Campechano 3W")
print(" ")
def generar_n_caracteres(n, caracter):
    """
    Genera una cadena de n caracteres repetidos.

    Parámetros:
    n (int): El número de repeticiones del carácter.
    caracter (str): El carácter que se repetirá.

    Retorna:
    str: Una cadena formada por n repeticiones del carácter.
    """
    return caracter * n

# Ejemplo de uso:
print(generar_n_caracteres(5, "n"))  # Debería devolver "nnnnnn"
