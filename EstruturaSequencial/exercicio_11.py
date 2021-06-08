"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a.o produto do dobro do primeiro com metade do segundo .
    b.a soma do triplo do primeiro com o terceiro.
    c.o terceiro elevado ao cubo.
"""
try:
    n1 = int(input('Informe um número inteiro:'))
    n2 = int(input('Informe outro número inteiro:'))
    n3 = float(input('Informe um número real:'))
except ValueError:
    print('Ops algo deu errado, informe valores numéricos válidos.')

print('\n*** Cálculo dos valores informados ***\n')

a = (2 * n1) * (n2 / 2)
b = (3 * n1) + n3
c = n3 ** 3

print('\no produto do dobro do primeiro com metade do segundo : %d' % a)
print('\na soma do triplo do primeiro com o terceiro %d' % b)
print('\no terceiro elevado ao cubo %d' % c)


