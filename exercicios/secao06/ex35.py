vi = int(input('Informe o valor inicial: '))
vf = int(input('Informe o valor final: '))
s = 0
if vi > vf:
    print('Intervalo de valores inválido')
else:
    for n in range(vi, vf+1):
        if n % 2 != 0:
            s += n
print(f'Soma dos impares neste intervalo: {s}')
