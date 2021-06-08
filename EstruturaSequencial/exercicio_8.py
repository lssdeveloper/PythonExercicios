"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% \para o Imposto de Renda,
8% \para o INSS e 5% \para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
descontos e o salário líquido, conforme a tabela abaixo:
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
"""

try:
    salario_por_hora = float(input('Quanto você ganha por hora ?'))
    qtas_horas_por_mes = float(input('Quantas horas por mês ?'))
except ValueError:
    print('Ops. Algo deu errado na entrada de dados! Informe um valor númerico válido.')
salario_bruto = salario_por_hora * qtas_horas_por_mes
ir = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
descontos = ir + inss + sindicato


salario_liquido = salario_bruto - descontos

print('Seu salário bruto: R$ %.2f' % salario_bruto)
print('Seu salário líquido: R$ %.2f' % salario_liquido)
print('Seu desconto Imposto de Renda: R$ %.2f' % ir)
print('Seu desconto INSS: R$ %.2f' % inss)
print('Seu desconto sindicato: R$ %.2f' % sindicato)
print('Total de desconto: R$ %.2f' % descontos)

# 40.90 * 220 horas

