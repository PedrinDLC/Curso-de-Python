print('Digite 10 valores para somá-los: ')

soma = 0

for i in range(10):
    num = int(input(f'Digite o {i + 1}º número: '))
    soma = soma + num
print(f'Somatório: {soma}')
