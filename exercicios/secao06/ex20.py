num = qtd = qtd_pares = 0

while True:
    num = int(input('Digite um número (1000 para sair do programa): '))
    if num == 1000:
        break
    elif num % 2 == 0:
        qtd_pares += 1
    qtd += 1

print(f'Foram digitados {qtd} númneros e {qtd_pares} eram pares')
