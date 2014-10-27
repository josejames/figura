class Figura():

    def __init__(self,args):
        self.figura = args[0]
        self.parametros = args[1:]

    def getArea(self):

        if self.figura == 'cuadrado':
           return self.cuadrado(self.parametros[0])
        elif self.figura == 'circulo':
            return round(self.circulo(self.parametros[0]), 2)
        elif self.figura == 'rectangulo':
           return self.rectangulo(self.parametros[0], self.parametros[1])

    def rectangulo(self, lado, lado2):
        return lado * lado2

    def cuadrado(self, lado):
        return lado ** 2

    def triangulo(self, base, altura):
        return (base * altura) / 2

    def circulo(self, radio):
        return 3.1416 * (radio ** 2)

    def poligono(self, per, apot):
        return (per * apot) / 2
