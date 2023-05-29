maior = menor = 0

for i in range(10):
    num = int(input(f'{i+1}º número: '))
    if i == 0:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
