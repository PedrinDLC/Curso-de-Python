soma = 0
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        soma += num
print(f'A soma dos numeros naturais abaixo de 1000 que sao multiplos de 3 ou 5 é {soma}')
