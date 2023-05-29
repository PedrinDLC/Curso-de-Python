print('-='*10)
print(f'{"Calculadora de IMC":^20}')
print('-='*10)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura (em metros): '))

imc = peso / altura ** 2

if imc <= 18.5:
    print(f'{imc:.1f}. Abaixo do peso!')
elif 18.6 <= imc <= 24.9:
    print(f'{imc:.1f}. Saudável!')
elif 25 <= imc <= 29.9:
    print(f'{imc:.1f}. Acima do peso!')
elif 30 <= imc <= 34.9:
    print(f'{imc:.1f}. Obesidade Grau I!')
elif 35 <= imc <= 39.9:
    print(f'{imc:.1f}. Obesidade Grau II(severa)!')
elif imc > 40:
    print(f'{imc:.1f}. Obesidade Grau III(mórbida)!')
