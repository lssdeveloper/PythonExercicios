"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
(0 °C × 9/5) + 32 = 32 °F
"""

try:
    c = float(input('Informe graus Celsius:'))
except ValueError:
    print('Ops. Algo deu errado na entrada de dados! Informe um valor númerico válido.')

f = 32 + (c * 9) / 5
print('Graus em Fahrenheit: %.2f ' % f)
