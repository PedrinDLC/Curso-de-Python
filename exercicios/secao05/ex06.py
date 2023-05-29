n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
if n1 == n2:
    print('Os números são iguais')
elif n1 > n2:
    print(f'O primeiro número é maior e a diferença entre eles é de {n1 - n2}')
else:
    print(f'O segundo número é maior e a diferença entre eles é de {n2 - 1}')
