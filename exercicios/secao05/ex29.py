from random import randint

acertos = 0


# Primeira questão
a, b = randint(1, 100), randint(1, 100)

print(f'Qual é a soma de {a} + {b}? ')
resp = int(input())
if a + b == resp:
    print('Parabéns. Você acertou!')
    acertos += 1
else:
    print(f'Que pena, voce errou! \nA resposta era {a + b}')

# Segunda questão
a, b = randint(1, 100), randint(1, 100)

print(f'Qual é a soma de {a} + {b}? ')
resp = int(input())
if a + b == resp:
    print('Parabéns. Você acertou!')
    acertos += 1
else:
    print(f'Que pena, voce errou! \nA resposta era {a + b}')

# Terceira questão
a, b = randint(1, 100), randint(1, 100)

print(f'Qual é a soma de {a} + {b}? ')
resp = int(input())
if a + b == resp:
    print('Parabéns. Você acertou!')
    acertos += 1
else:
    print(f'Que pena, voce errou! \nA resposta era {a + b}')

# Quarta questão
a, b = randint(1, 100), randint(1, 100)

print(f'Qual é a soma de {a} + {b}? ')
resp = int(input())
if a + b == resp:
    print('Parabéns. Você acertou!')
    acertos += 1
else:
    print(f'Que pena, voce errou! \nA resposta era {a + b}')

# Quinta questão
a, b = randint(1, 100), randint(1, 100)

print(f'Qual é a soma de {a} + {b}? ')
resp = int(input())
if a + b == resp:
    print('Parabéns. Você acertou!')
    acertos += 1
else:
    print(f'Que pena, voce errou! \nA resposta era {a + b}')

print('FIM DA PROVA!!')
print(f'VOCÊ ACERTOU {acertos} QUESTÕES')
