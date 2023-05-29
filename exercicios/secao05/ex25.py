print('\033[34m-='*25)
print(f'\033[36m{"Calculadora de Equação do 2º grau":^50}')
print('\033[34m-='*25)

print('\033[mrepresentação: \033[31max² + bx + c = 0')
print('\033[m')
print('Informe os valores de')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == 0:
    print('Não é uma equação de 2º grau!')
else:
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('\033[31mNão existe raiz dentro dos reais\033[m')
    elif delta == 0:
        # raiz única
        x = (-b + (delta ** (1/2))) / (2*a)
        print(f'Raiz única. X = {x}')
    elif delta > 0:
        # 2 raizes
        x1 = (-b + (delta ** (1/2))) / (2*a)
        x2 = (-b - (delta ** (1/2))) / (2*a)
        print(f'x1 = {x1} \nx2 = {x2}')
