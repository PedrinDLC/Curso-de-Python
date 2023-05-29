print('-='*20)
print('Verificador de Aposentadoria')
print('-='*20)

idade = int(input('Informe a sua idade: '))
tempo = int(input('Informe o seu tempo de serviço (em anos): '))

if idade >= 65:
    print('Você já pode se aposentar.')
elif tempo >= 30:
    print('Você já pode se aposentar.')
elif idade >= 60 and tempo >= 25:
    print('Você já pode se aposentar.')
else:
    print('Você ainda não pode se aposentar.')
