num = int(input('Digite um número inteiro: '))
soma = 0
if num <= 0:
    print('Número inválido!')
else:
    numero = str(num)
    for elemento in numero:
        soma = int(elemento) + soma
    print(f'A soma dos aslgarismos desse número é {soma}')
