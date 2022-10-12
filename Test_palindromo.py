import unittest
from main import palindromo 

class TestPalabraPalindromo(unittest.TestCase):
    def test_1(self):
        palabra_palindromo = palindromo("neuquen")
        self.assertEqual(palabra_palindromo,"Es una palabra palindromo")
    
    def test_2(self):
        palabra_palindromo = palindromo("sometemos")
        self.assertEqual(palabra_palindromo,"Es una palabra palindromo")

    def test_3(self):
        palabra_palindromo = palindromo("oso")
        self.assertEqual(palabra_palindromo,"Es una palabra palindromo")

    def test_4(self):
        palabra_palindromo = palindromo("torta")
        self.assertEqual(palabra_palindromo,"No es una palabra palindromo")

if __name__ == "__main__":
    unittest.main()