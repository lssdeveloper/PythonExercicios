"""
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9)
"""

try:
    f = float(input('Informe quantos Fahrenheit ?'))  # fahrenheit
except ValueError:
    print('Ops. Algo deu errado na entrada de dados! Informe um valor númerico válido.')

celsius = 5 * ((f - 32) / 9)
print('A conversão do grau Fahrenheit %.2f para Celsius é %.2f ' % (f, celsius))
