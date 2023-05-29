"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências númericas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for numero in range(10):
    print(numero)


# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor de parada não inclusive (inicio especificado pelo usuario, passo de 1 em 1)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)


# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor de parada não inclusive (inicio especificado pelo usuario, passo especificado pelo usuário)

# Exemplo Forma 3
for num in range(1, 10, 2):
    print(num)


# Forma 4 (inversa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor de parada não inclusive (inicio especificado pelo usuario, passo especificado pelo usuário)

# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)

"""
