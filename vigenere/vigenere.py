import sys
from cs50 import get_string

def Check(k):
    for char in k:
        if not char.isalpha():
            return False
        return True

if len(sys.argv) != 2 or not Check(sys.argv[1]):
    print("usage: ./vigenere k")
    sys.exit(1)

k = sys.argv[1]
TXT = get_string("plaintext: ")
C = 0

print("ciphertext: ", end="")

for char in TXT:
    if not char.isalpha():
        print(char, end="")
        continue

    # correccion de codigo ascii
    CCA = 56 if char.isupper() else 97

    # caracter corregido
    CC = ord(char) - CCA

    KC = ord(k[C % len(k)].upper()) - 65

