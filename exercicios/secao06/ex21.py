n1 = int(input('Valor inicial: '))
n2 = int(input('Valor final: '))

soma = 0
mult = 1

for num in range(n1, n2+1):
    if num % 2 == 0:
        soma += num
    else:
        mult *= num

print(f'Soma dos números pares entre {n1} e {n2}: {soma}')
print(f'Produto dos números ímpares entre {n1} e {n2}: {mult}')
