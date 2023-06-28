"""
Módulo Collections - Counter (Contador)

Collection -> High-performance Container Datetypes


Counter -> Recebe um iterável como parametro e cria um objeto do tipo Collections Counter que é
parecido com um dicionário, contendo como chave o elemento da lista passada como parametro e como valor
a quantidade de ocorrencias desse elemento

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui usamos uma Lista
lista = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 5, 5, 45, 45, 66, 66, 43, 34]


# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 7, 2: 7, 3: 4, 4: 4, 5: 2, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

from collections import Counter

# Exemplo 3

texto = """A Wikipédia é um projeto de enciclopédia colaborativa, universal e multilíngue estabelecido na internet 
sob o princípio wiki. Tem como propósito fornecer um conteúdo livre, objetivo e verificável, que todos possam editar 
e melhorar. O projeto é definido pelos princípios fundadores e o conteúdo é disponibilizado sob a licença Creative 
Commons BY-SA e pode ser reutilizado sob a mesma licença, desde que respeitando os termos de uso."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))
