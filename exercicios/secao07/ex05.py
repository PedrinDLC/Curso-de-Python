num = []
pares = []

for i in range(10):
    num.append(int(input(f'Digite o {i+1}° número: ')))


for elemento in num:
    if elemento % 2 == 0:
        pares.append(elemento)

print(f'Voce digitou um total de {len(pares)} números pares, sendo eles: {pares}')
