print(" ")
print("Alvaro Campechano 3W")
print(" ")
def procedimiento(lista):
    """
    Imprime un histograma visual basado en los números de la lista.

    Parámetros:
    lista (list): Lista de números enteros que representan las alturas del histograma.

    Ejemplo de salida:
    Si la lista es [4, 9, 7], se imprimirá:
    ****
    *********
    *******
    """
    for num in lista:
        print('*' * num)

# Ejemplo de uso:
procedimiento([4, 9, 7])  
# Debería imprimir:
# ****
# *********
# *******
