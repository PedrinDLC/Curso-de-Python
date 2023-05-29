num = int(input('Digite um número: '))

soma = 0

for i in range(num+1):
    soma += i

print(f'Soma dos {num} primeiros números naturais: {soma}')
