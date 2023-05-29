sal = float(input('Informe seu salário: '))
prest = float(input('Informe o valor da prestação do empréstimo: '))
if prest > (0.2 * sal):
    print('Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')
