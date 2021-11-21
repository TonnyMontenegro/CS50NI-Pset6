# import functions
from cs50 import get_float
from cs50 import get_int
from cs50 import get_string

# funcion principal
def main():

    #un ciclo que se repite cuando se ingresa un numero invalido
    while True:
        altura = get_int("ingrese la altura que desea: ")
        ancho = altura + 1
        if altura >= 0 and altura <= 23:
            break

    for i in range(1, altura + 1):
        hashes = i + 1
        espacios = ancho - hashes
        # la impresion de los hashes y espacios
        print(" " * espacios, end="")
        print("#" * hashes)

if True:
    main()