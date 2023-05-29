n = int(input('Informe um número: '))
soma = 0
for i in range(1, n+1):
    soma += 1/i
print(f'Soma harmônica de {n} = {soma}')
