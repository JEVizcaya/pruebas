def contar_palabras(frase):
    # Dividir la frase en palabras utilizando el espacio como delimitador
    palabras = frase.split()
    # Contar y devolver el número de palabras
    return len(palabras)

# Pedir al usuario una frase
frase = input("Ingresa una frase: ")
numero_de_palabras = contar_palabras(frase)

print(f"El número de palabras en la frase es: {numero_de_palabras}")

def contar_letra(frase, letra):
    # Contar cuántas veces se repite la letra en la frase
    return frase.count(letra)

# Pedir al usuario una frase y la letra a contar

letra = input("Ingresa la letra que deseas contar: ")

# Asegurarse de que la letra tenga solo un carácter
if len(letra) == 1:
    repeticiones = contar_letra(frase, letra)
    print(f"La letra '{letra}' se repite {repeticiones} veces en la frase.")
else:
    print("Por favor, ingresa solo una letra.") 

