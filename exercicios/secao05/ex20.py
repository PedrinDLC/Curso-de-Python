print('\033[32m-='*20)
print(f'\033[34m{"Analisador de Trângulo 3000":^40}')
print('\033[32m-='*20)
print('\033[m', end='')
print('Informe a medida de 3 segmentos para \nverificar se podem formar um triângulo: ')
a = float(input('Primeiro: '))
b = float(input('Segundo: '))
c = float(input('Terceiro: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos podem formar um triângulo ', end='')
    if a == b == c == a:
        print('EQUILÁTERO.')
    elif a != b != c != a:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
