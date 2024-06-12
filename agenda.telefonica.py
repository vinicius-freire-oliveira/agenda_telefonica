# Criação do dicionário
contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')]

contatos = dict(contatos_lista)
print(contatos)

# Tratamento da exceção do tipo KeyError, método específico para busca de valores, o get()
print(contatos.get('Yan', 'Contato não encontrado'))
print(contatos.get('João', 'Contato não encontrado'))

# Verificar se um contato está em nosso dicionário através da palavra chave in
print('Yan' in contatos)

# Para obtermos valores
print('9999-9999' in contatos.values())

# Adicionando valores ao dicionário
contatos['João'] = '8887-7778'
print(contatos)

# Removendo itens do dicionário
del contatos['Marina']
print(contatos)

# Remover um item que não existe
contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
            'Marina': '8877-7788', 'João': '8887-7778'}

print(contatos.pop('Marina', 'Contato não encontrado'))
print(contatos.pop('Catarina', 'Contato não encontrado'))
print()
print(contatos)

# Juntando dois dicionários
meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                    'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                        'Luiza': '4567-7654'}

for nome in contatos_do_pedro:
    meus_contatos[nome] = contatos_do_pedro[nome]

print(meus_contatos)

# Melhor forma de juntar dicionários
meus_contatos.update(contatos_do_pedro)
print(meus_contatos)

# O problema do prefixo 9 e compreensões de dicionário
meus_contatos_novo = {nome: '9' + meus_contatos[nome] for nome in meus_contatos}
print(meus_contatos_novo)

# Views vs. listas
valores = meus_contatos_novo.values()
print(valores)

# Memória com a Views
print(valores.__sizeof__())
