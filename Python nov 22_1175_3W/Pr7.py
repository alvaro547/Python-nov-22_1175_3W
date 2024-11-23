print(" ")
print("Alvaro Campechano 3W")
print(" ")
def es_palindromo():
    """
    Solicita al usuario ingresar una palabra y verifica si es un palíndromo.

    Retorna:
    bool: True si la palabra es un palíndromo, False en caso contrario.
    """
    palabra = input("Ingresa una palabra: ").strip()  # Solicita la palabra al usuario y elimina espacios extra

    # Verifica si la palabra es igual a su versión invertida
    return palabra == palabra[::-1]

# Ejemplo de uso:
print(es_palindromo())  # Debería devolver True o False
