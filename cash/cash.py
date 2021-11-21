from cs50 import get_float
from math import floor

#declara/define la funcion principal para ser implementada
def main():
    #crea un ciclo infinito a modo de un Do While
    while True:
        #CS = "Cambio Solicitado"
        CS = get_float("ingrese monto a cambiar: ")
        #CE = "Cambio Entero"(redondeado)
        CE = floor(CS * 100)

        #si el cambio solicitado es mayor que 0 rompe el ciclo de arriba
        if CS > 0:
            break
    """M significa moneda y el numero es
    la denominacion de la moneda ya sea
    Moneda de 25 (M25) o cualquier otra
    divide entre esa denominacion y el
    residuo es lo que esa denominacion
    no puede restar y se lo pasaria
    a la sig"""
    M25 = CE // 25
    M10 = (CE % 25) // 10
    M5 = ((CE % 25) % 10) // 5
    M1 = ((CE % 25) % 10) % 5

    #imprime la suma de los contadores para cada moneda
    print(f"{M25 + M10 + M5 + M1}")

#llama a main
if __name__ == "__main__":
    main()