print('Digite 3 números: ')
num1 = int(input('Primeiro: '))
num2 = int(input('Segundo: '))
num3 = int(input('Terceiro: '))

maior = menor = meio = num1

# Maior
if maior < num2:
    maior = num2
if maior < num3:
    maior = num3

# Menor

if menor > num2:
    menor = num2
if menor > num3:
    menor = num3

# Meio

if menor < num2 < maior:
    meio = num2
if menor < num3 < maior:
    meio = num3

print('\nOrdem crescente')
print(f'{menor}\n{meio}\n{maior}')
