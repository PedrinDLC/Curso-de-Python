print('Informe 10 valores para calcular a média entre eles')

soma = 0

for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    soma += num
print(f'Média: {soma / 10}')
