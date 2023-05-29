soma = 0

num = int(input("Digite um número: "))

for n in range(1, num):
    if num % n == 0:
        soma += n
print(f'A soma dos divisores de {num} é {soma}')
