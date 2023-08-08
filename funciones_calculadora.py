#SUMA
class SumaCalculadora:
    def __init__(self):
        self.resultado = 0

    def sumar(self, num1, num2):
        self.resultado = num1 + num2

    def obtener_resultado(self):
        return self.resultado

calculadora = SumaCalculadora()

num1 = float(input("Ingrese el primer número a sumar: "))
num2 = float(input("Ingrese el segundo número: "))

calculadora.sumar(num1, num2)

print("El resultado de la suma es:", calculadora.obtener_resultado())
print("------------------------------------------------")
#RESTA
class RestaCalculadora:
    def __init__(self):
        self.resultado = 0

    def restar(self, num1, num2):
        self.resultado = num1 - num2

    def obtener_resultado(self):
        return self.resultado

calculadora = RestaCalculadora()

num1 = float(input("Ingrese minuendo: "))
num2 = float(input("Ingrese sustraendo: "))

calculadora.restar(num1, num2)

print("La diferencia es:", calculadora.obtener_resultado())
print("------------------------------------------------")
#MULTIPLICACIÓN
class MultiplicarCalculadora:
    def __init__(self):
        self.resultado = 0

    def multiplicar(self, num1, num2):
        self.resultado = num1 * num2

    def obtener_resultado(self):
        return self.resultado

calculadora = MultiplicarCalculadora()

num1 = float(input("Ingrese multiplicando: "))
num2 = float(input("Ingrese multiplicador: "))

calculadora.multiplicar(num1, num2)

print("El producto es:", calculadora.obtener_resultado())
print("------------------------------------------------")
#DIVISIÓN
class DividirCalculadora:
    def __init__(self):
        self.resultado = 0

    def dividir(self, num1, num2):
        if num2 == 0:
            print("Error: No es posible dividir entre cero.")
        else:
            self.resultado = num1 / num2

    def obtener_resultado(self):
        return self.resultado

calculadora = DividirCalculadora()

num1 = float(input("Ingrese dividendo: "))
num2 = float(input("Ingrese divisor: "))

calculadora.dividir(num1, num2)

print("El cociente es:", calculadora.obtener_resultado())

print("------------------------------------------------")
#POTENCIA
class PotenciaCalculadora:
    def __init__(self):
        self.resultado = 0

    def potencia(self, num1, num2):
        self.resultado = num1 ** num2

    def obtener_resultado(self):
        return self.resultado

calculadora = PotenciaCalculadora()

num1 = float(input("Ingrese numero base: "))
num2 = float(input("Ingrese el exponente: "))

calculadora.potencia(num1, num2)

print("La potencia es:", calculadora.obtener_resultado())

print("------------------------------------------------")
#RAIZ
class RadicacionCalculadora:
    def __init__(self):
        self.radicando = 0
        self.indice = 0
        self.resultado = 0

    def ingresar_valores(self):
        self.radicando = float(input("Ingrese el radicando: "))
        self.indice = int(input("Ingrese el índice: "))

    def calcular_raiz(self):
        self.resultado = self.radicando ** (1 / self.indice)

    def mostrar_resultado(self):
        print("La raíz {} de {} es: {}".format(self.indice, self.radicando, self.resultado))

calculadora = RadicacionCalculadora()

calculadora.ingresar_valores()
calculadora.calcular_raiz()
calculadora.mostrar_resultado()
