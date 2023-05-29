vh = float(input('Informe o valor da hora trabalhada: R$'))
ht = int(input('Informe o total de horas trabalhadas no mês: '))
total = (vh * ht) * 1.10
print(f'O valor a ser pago é de R${total:.2f}')
