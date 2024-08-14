import pyodbc
from flask import request

# Conexão com o banco de dados
dados_conexao = pyodbc.connect(
    'Driver={SQL Server};'  # Corrigido o nome do driver
    "Server=DESKTOP-LUI5215;"
    'Database=banco'
)

cursor = dados_conexao.cursor()

# Verifica se a variável submit está definida
if 'submit' in request.form:
    nome = request.form['nome']
    telefone = request.form['telefone']
    quantidade = request.form['quantidade']
    dia = request.form['dia']

    # Aqui você pode adicionar o código para inserir os dados no banco
    query = "INSERT INTO cadastro_cliente (nome_cliente, telefone, quantidade, data_cliente) VALUES (nome), (telefone), (quantidade), (data))"
    cursor.execute(query, (nome, telefone, quantidade, dia))
    dados_conexao.commit()

# Fechando a conexão com o banco de dados
dados_conexao.close()
