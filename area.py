entrada = input().split()


pi = 3.14159
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

triangulo = (a * c) / 2
circulo = pi * pow(c, 2)
trapezio = (a + b) * c / 2
quadrado = pow(b, 2)
retangulo = a * b

print(F'TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}')