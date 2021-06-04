"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
a = 10 cm * 10 cm
a = 100 cm² * 2
a = 200 cm²   O dobro desta área
"""

a = float(input('Área ?'))
a_em_dobro = (a * a) * 2
print('\nÁrea informada em dobro: %.2f m²' % a_em_dobro)