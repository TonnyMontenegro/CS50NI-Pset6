import sys
from cs50 import get_string

# si los argumentos son mas o menos de 2 nos indica el uso correcto y cierra el programa
if len(sys.argv) != 2:
    print("forma de uso: /caesar k")
    sys.exit(1)

# K es la llave que usaremos para cifrar
k = int(sys.argv[1])

# TI es el texto ingresado por el usuario
TI = get_string("plaintext: ")


print("ciphertext: ", end = "")

# recorre caracter por caracter el texto ingresado si no es alfabetico lo dea tal cual esta
for Char in TI:
    if not Char.isalpha():
        print(Char, end = "")
        continue

    """ si es un caracter alfabetico
    procede a cifrarlo y reajustar la letra en
    dependencia de si es mayuscula o minuscula"""

    # correccion de codigo ascii
    CCA = 65 if Char.isupper() else 97

    # caracter corregido
    CC = ord(Char) - CCA

    # añade el cifrado
    C = (CC + k) % 26

    print(chr(C + CCA), end="")

print()