print('Escolha uma opção: ')
print('1- Soma de 2 números.')
print('2- Diferença entre 2 números (maior pelo menor).')
print('3- Produto entre 2 números.')
print('4- Divisão entre 2 números (o denominador não pode ser zero).')
op = int(input('Opção: '))

if op == 1:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
elif op == 2:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    print(f'A diferença entre {n1} e {n2} é igual a {n1 - n2}')
elif op == 3:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    print(f'O produto entre {n1} e {n2} é igual a {n1 * n2}')
elif op == 4:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    print(f'A divisão entre {n1} e {n2} é igual a {n1 / n2}')
else:
    print('Opção Inválida!')
