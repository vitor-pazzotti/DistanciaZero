import unittest
from distancia_zero import conta_texto

class TesteDistancia(unittest.TestCase):

    def verifica_zero(self):
        self.assertEqual(conta_texto('1234444444'),
        ('1234444444'))
    
    def quantidade_zero(self):
        self.assertEqual(
            conta_texto('000000'), 6)

    def vazio(self):
        self.assertEqual(
            conta_texto(''),
            ('Redirecionando ao menu.'))

    def espaco_vazio(self):
        self.assertEqual(
            conta_texto('aaaaa    00000000 0000'), 8)
    
    def espaco_inicio(self):
        self.assertEqual(
            conta_texto(' aaaaa00000000'), 8)
    
    def caracter(self):
        self.assertEqual(
            conta_texto('****000/0----0000'), 4)

    def espaço_entre_zeros(self):
        self.assertEqual(
            conta_texto('aCDFSHDl 00 000 0000 00000'),5)


if __name__ == "__main__":
    unittest.main()