chamada = {
    'joao': 'F',
    'maria': 'C',
    'pedro': 'C',
    'jose': 'F',
    'luis': 'C'
}

print(chamada)

#percorre todos os itens do dicionario, obtendo a chave de cada item
for chave in chamada:
    print(chave)

print('-' * 10)

#percorre todos os itens do dicionario, obtendo o valor de cada item
for valor in chamada.values():
    print(valor)

print('-' * 10)

# percorre todos os itens do dicionario, obtendo o par chave/valor de cada item
for chave,valor in chamada.items():
    print(f'{chave} --> {valor}')

