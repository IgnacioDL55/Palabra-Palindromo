import unittest

def palindromo(palabra):
    if palabra == palabra[: :-1]:
        return("Es una palabra palindromo")
    else:
        return("No es una palabra palindromo")