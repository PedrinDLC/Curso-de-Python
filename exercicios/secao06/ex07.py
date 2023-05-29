print('Informe 10 valores para calcular a média entre eles')
print('Números negativos serão ignorados')

soma = 0
cont = 0

for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    if num > 0:
        soma += num
        cont += 1
print(f'Média: {soma / cont}')
