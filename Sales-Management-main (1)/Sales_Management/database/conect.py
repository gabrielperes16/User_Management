import pyodbc

# Definindo os dados de conexão
dados_conexao = (
    'Driver={SQL Server};'  # Corrigido o nome do driver
    "Server=DESKTOP-LUI5215;"
    'Database=banco'
)

# Estabelecendo a conexão
conexao = pyodbc.connect(dados_conexao)
print('Conexão OK!')

# Criando um cursor para executar comandos SQL
cursor = conexao.cursor()

# Comando SQL para inserir dados na tabela
comando = """INSERT INTO cadastro_cliente(id_cliente, nome_cliente, telefone, data_cliente,quantidade)
VALUES
    ({id_cliente},{nome_cliente},{telefone},{data_cliente},{quantidade})

"""



# Executando o comando SQL
cursor.execute(comando)

# Confirmando a transação
cursor.commit()

# Fechando a conexão
conexao.close()
