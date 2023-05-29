print('-='*20)
print(f'|{"CARDÁPIO":^38}|')
print('-='*20)
print('| Especificação   |  Código  |  Preço  |')
print(f'|{"-"*38}|')
print('| Cachorro Quente |   100    |   1.20  |')
print('| Bauru Simples   |   101    |   1.30  |')
print('| Bauru com Ovo   |   102    |   1.50  |')
print('| Hamburguer      |   103    |   1.20  |')
print('| Cheeseburguer   |   104    |   1.70  |')
print('| Suco            |   105    |   2.20  |')
print('| Refrigerante    |   106    |   1.00  |')
print('-='*20)

cod = int(input('Informe o código do produto que deseja pedir: '))
qtd = int(input('Informe a quantidade: '))

if cod == 100:
    print(f'Valor da conta: R${1.2 * qtd:.2f}')
elif cod == 101:
    print(f'Valor da conta: R${1.3 * qtd:.2f}')
elif cod == 102:
    print(f'Valor da conta: R${1.5 * qtd:.2f}')
elif cod == 103:
    print(f'Valor da conta: R${1.2 * qtd:.2f}')
elif cod == 104:
    print(f'Valor da conta: R${1.7 * qtd:.2f}')
elif cod == 105:
    print(f'Valor da conta: R${2.2 * qtd:.2f}')
elif cod == 106:
    print(f'Valor da conta: R${1.0 * qtd:.2f}')
else:
    print('Código inválido!')
