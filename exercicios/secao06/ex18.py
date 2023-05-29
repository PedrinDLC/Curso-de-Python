n = int(input('Quantas vezes o programa deve rodar? '))

maior = qtd = 0

for i in range(n):
    num = int(input('Digite um número: '))
    if i == 0:
        maior = menor = num
    if num > maior:
        maior = num
        qtd = 1
    elif num == maior:
        qtd += 1

print(f'O maior número foi {maior} e ele foi digitado {qtd} vezes.')
