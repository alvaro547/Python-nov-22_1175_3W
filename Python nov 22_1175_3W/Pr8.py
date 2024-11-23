print(" ")
print("Alvaro Campechano 3W")
print(" ")
def superposicion():
    """
    Solicita al usuario ingresar dos listas y verifica si tienen al menos un elemento en común.

    Retorna:
    bool: True si las listas tienen al menos un elemento en común, False en caso contrario.
    """
    # Solicitar las listas al usuario
    lista1 = input("Ingresa los elementos de la primera lista (separados por comas): ").split(',')
    lista2 = input("Ingresa los elementos de la segunda lista (separados por comas): ").split(',')

    # Convertir los elementos a enteros
    lista1 = [elem.strip() for elem in lista1]  # Eliminar espacios extra
    lista2 = [elem.strip() for elem in lista2]  # Eliminar espacios extra

    # Verificar si hay al menos un elemento en común entre las dos listas
    for elem1 in lista1:
        if elem1 in lista2:
            return True
    return False

# Ejemplo de uso:
print(superposicion())  # Debería devolver True o False
