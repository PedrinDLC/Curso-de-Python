dias = int(input('Informe os dias trabalhados: '))
tp = (dias * 30) - ((dias * 30) * 0.08)
print(f'Deverá ser pago: R${tp:.2f}')
