qs = 0
sq = 0

for i in range(1, 101):
    sq += i**2
    qs += i
qs = qs**2

print(f'A diferença do quadrado da soma e a soma dos quadrados dos 100 primeiros numeros naturais é:')
print(f'{qs} - {sq} = {qs - sq}')
