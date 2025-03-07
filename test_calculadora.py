import unittest

from calculadora import calculadora
class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.calc = calculadora()


    def test_suma(self):

            self.assertEqual(self.calc.suma(5,2),7)
            self.assertEqual(self.calc.suma(0,0),0)

    def test_resta_positivos(self):
        self.assertEqual(10 - 5, 5)
       


    def test_multiplicacion_positivos(self):
        self.assertEqual(3 * 4, 12)
        
        

    def test_multiplicacion_por_cero(self):
        self.assertEqual(5 * 0, 0)

    def test_multiplicacion_negativo_por_positivo(self):
        self.assertEqual(-3 * 4, -12)

    def test_division_exacta(self):
        self.assertEqual(10 / 2, 5)

    def test_division_decimal(self):
        self.assertEqual(7 / 2, 3.5)

    def test_division_periodica(self):
        self.assertAlmostEqual(10 / 3, 3.3333, places=4)

if __name__ == '__main__':
    unittest.main()



