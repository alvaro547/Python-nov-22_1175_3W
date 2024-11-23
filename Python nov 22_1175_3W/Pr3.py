print(" ")
print("Alvaro Campechano 3W")
print(" ")
def longitud(elemento):
    """
    Calcula la longitud de una lista o cadena.

    Parámetros:
    elemento (str, list): La lista o cadena de la cual calcular la longitud.

    Retorna:
    int: El número de elementos en la lista o caracteres en la cadena.
    """
    contador = 0
    for _ in elemento:
        contador += 1
    return contador

# Ejemplo de uso:
print(longitud("Hola"))  # Debería devolver 4
print(longitud([1, 2, 3, 4]))  # Debería devolver 4
