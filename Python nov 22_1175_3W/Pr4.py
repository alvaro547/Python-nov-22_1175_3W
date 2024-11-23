print(" ")
print("Alvaro Campechano 3W")
print(" ")
def es_vocal_usuario():
    """
    Solicita al usuario ingresar un carácter y verifica si es una vocal (a, e, i, o, u).
    Imprime un mensaje indicando si es una vocal o no.
    """
    # Solicitar al usuario que ingrese una letra
    caracter = input("Ingresa una letra: ").lower()

    # Verificar si es una vocal
    if caracter in 'aeiou':
        print(f"{caracter} es una vocal.")
    else:
        print(f"{caracter} no es una vocal.")

# Llamada a la función
es_vocal_usuario()
