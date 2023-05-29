qtd = soma = 0

while True:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if nota == -1:
        break
    else:
        soma += nota
        qtd += 1
print(f"A média das {qtd} notas digitadas é de {soma/qtd:.1f}")
