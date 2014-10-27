import unittest

from Figura import Figura


class TestCase(unittest.TestCase):

    def test_rectangulo_2_2(self):
        fig = Figura("rectangulo")
        self.assertEqual(4, fig.rectangulo(2, 2))

    def test_rectangulo_4_4(self):
        fig = Figura("rectangulo")
        self.assertEqual(16, fig.rectangulo(4, 4))

    def test_rectangulo_5_4(self):
        fig = Figura("rectangulo")
        self.assertEqual(20, fig.rectangulo(5, 4))

    def test_cuadrado_3(self):
        fig = Figura("cuadrado")
        self.assertEqual(9, fig.cuadrado(3))

    def test_cuadrado_10(self):
        fig = Figura("cuadrado")
        self.assertEqual(100, fig.cuadrado(10))

    def test_cuadrado_5(self):
        fig = Figura("cuadrado")
        self.assertEqual(25, fig.cuadrado(5))

    def test_triangulo_3_4(self):
        fig = Figura("triangulo")
        self.assertEqual(6, fig.triangulo(3, 4))

    def test_triangulo_4_4(self):
        fig = Figura("triangulo")
        self.assertEqual(8, fig.triangulo(4, 4))

    def test_triangulo_5_6(self):
        fig = Figura("triangulo")
        self.assertEqual(15, fig.triangulo(5, 6))

    def test_circulo_4(self):
        fig = Figura("circulo")
        self.assertEqual(50.2656, fig.circulo(4))

    def test_circulo_6(self):
        fig = Figura("circulo")
        self.assertEqual(113.0976, fig.circulo(6))

    def test_circulo_8(self):
        fig = Figura("circulo")
        self.assertEqual(201.0624, fig.circulo(8))

    def test_poligono_5_6(self):
        fig = Figura("poligono")
        self.assertEqual(15, fig.poligono(5, 6))

    def test_poligono_6_10(self):
        fig = Figura("poligono")
        self.assertEqual(30, fig.poligono(6, 10))

    def test_poligono_5_4(self):
        fig = Figura("poligono")
        self.assertEqual(10, fig.poligono(5, 4))


if __name__ == '__main__':
    unittest.main()
