import math
num = int(input('Informe um número inteiro: '))
if num < 0:
    print('Número inválido!')
else:
    print(f'O logaritimo desse número é {math.log(num)}')
