print('-='*25)
print(f"{'Analisador de ano bissexto':^50}")
print('-='*25)

ano = int(input('Digite um ano: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} NÃO é BISSEXTO!')
