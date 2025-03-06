def piramide_invertida(filas):
    for i in range(filas, 0, -1):
        print('*' * i)

# Llamar a la función con el número de filas deseado
filas = int(input("Ingrese el número de filas para la pirámide invertida: "))
piramide_invertida(filas)
