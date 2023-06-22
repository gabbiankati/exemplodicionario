alunos = [
    {'nome': 'Joao', 'email': 'joao@gmail.com'},
    {'nome': 'Pedro', 'email': 'pedro@gmail.com'},
]

for a in alunos:
    print(a)

for a in alunos:
    print(a['nome'])
    print(a['email'])
    print('-' * 5)

print(alunos[1]['nome'])