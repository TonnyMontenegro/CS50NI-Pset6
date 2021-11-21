from cs50 import get_int
from math import floor


def main():

    # N es nummero que se almacenaran temporalmente
    N1 = 0
    N2 = 0

    # es el numero de digitos que contiene la CC
    Ndigit = 0

    #Es la suma de probabilidades dobles
    SPD = 0
    # suma de probabilidades simples
    SP = 0

    # CC es credit card
    CC = get_int("ingrese la tarjeta de credito: ")

    # mientras la CC no sea un numero mayor que 0
    while CC > 0:
        N2 = N1
        N1 = CC % 10

        if Ndigit % 2 == 0:
            SP += N1
        else:
            multiplo = 2 * N1
            SPD += (multiplo // 10) + (multiplo % 10)

        CC //= 10
        Ndigit += 1

    valid = (SP + SPD) % 10 == 0
    P2D = (N1 * 10) + N2

    """verifica que cada una de las
    tarjetas sean validas y que coincidan
    con la cantidad de digitos o
    numeracion de cada tipo de tarjeta"""

    if N1 == 4 and Ndigit >= 13 and Ndigit <= 16 and valid:
        print("VISA\n")

    elif P2D >= 51 and P2D <= 55 and Ndigit == 16 and valid:
        print("MASTERCARD\n")

    elif (P2D == 34 or P2D == 37) and Ndigit == 15 and valid:
        print("AMEX\n")

    else:
        print("INVALID\n")


if __name__ == "__main__":
    main()