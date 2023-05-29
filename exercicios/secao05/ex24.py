preco = float(input('Informe o valor do produto: R$'))
estado = str(input('Informe o estado destino (sigla): ')).upper().strip()

if estado == 'MG':
    print(f'O preço final acrescido de imposto será de R${preco * 1.07:.2f}')
elif estado == 'SP':
    print(f'O preço final acrescido de imposto será de R${preco * 1.12:.2f}')
elif estado == 'RJ':
    print(f'O preço final acrescido de imposto será de R${preco * 1.15:.2f}')
elif estado == 'MS':
    print(f'O preço final acrescido de imposto será de R${preco * 1.08:.2f}')
else:
    print('Estado Inválido!')
