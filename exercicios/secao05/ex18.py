print('Escola uma das 4 operações: \nAdição : [A]\nSubtração : [S]\nMultiplicação : [M]\nDivisão : [D]')
op = str(input())[0].strip().upper()
if op == 'A':
    n1 = int(input('Informe o 1º número: '))
    n2 = int(input('Informe o 2º número: '))
    print(f'A soma desses números é: {n1 + n2}')
elif op == 'S':
    n1 = int(input('Informe o 1º número: '))
    n2 = int(input('Informe o 2º número: '))
    print(f'A subtração desses números é: {n1 - n2}')
elif op == 'M':
    n1 = int(input('Informe o 1º número: '))
    n2 = int(input('Informe o 2º número: '))
    print(f'O produto desses números é: {n1 * n2}')
elif op == 'D':
    n1 = int(input('Informe o 1º número: '))
    n2 = int(input('Informe o 2º número: '))
    print(f'A divisão entre esses números é: {n1 / n2}')
else:
    print('Operação inválida!')
