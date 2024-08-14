import pyodbc
from flask import Blueprint, render_template, request, jsonify, abort
from datetime import datetime
from database.connect import cursor,dados_conexao

# Conexão com o banco de dados


cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """Listar os clientes"""
    cursor.execute("SELECT * FROM cadastro_cliente")
    clientes = cursor.fetchall()

    # Converte os resultados em uma lista de dicionários
    clientes_dict = [
        {
            "id": cliente.id_cliente,
            "nome": cliente.nome_cliente,
            "telefone": cliente.telefone,
            "quantidade": cliente.quantidade,
            "dia": cliente.data_cliente.strftime('%Y-%m-%d')
        }
        for cliente in clientes
    ]

    return render_template('lista_clientes.html', clientes=clientes_dict)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """Inserir os dados do cliente"""
    nome = request.form['nome']
    telefone = request.form['telefone']
    quantidade = request.form['quantidade']
    dia = datetime.now().strftime('%Y-%m-%d')

    query = """
    INSERT INTO cadastro_cliente (nome_cliente, telefone, quantidade, data_cliente) 
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (nome, telefone, quantidade, dia))
    dados_conexao.commit()

    return jsonify({'status': 'Cliente inserido com sucesso'}), 201

@cliente_route.route('/new')
def form_cliente():
    """Formulário para cadastrar um cliente"""
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """Formulário para editar um cliente"""
    query = "SELECT * FROM cadastro_cliente WHERE id_cliente = ?"
    cursor.execute(query, cliente_id)
    cliente = cursor.fetchone()

    if cliente:
        cliente_dict = {
            "id": cliente.id_cliente,
            "nome": cliente.nome_cliente,
            "telefone": cliente.telefone,
            "quantidade": cliente.quantidade,
            "dia": cliente.data_cliente.strftime('%Y-%m-%d')
        }
        return render_template('form_cliente.html', cliente=cliente_dict)
    else:
        abort(404)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """Atualizar informações do cliente"""
    nome = request.form['nome']
    telefone = request.form['telefone']
    quantidade = request.form['quantidade']
    dia = request.form['dia']

    query = """
    UPDATE cadastro_cliente
    SET nome_cliente = ?, telefone = ?, quantidade = ?, data_cliente = ?
    WHERE id_cliente = ?
    """
    cursor.execute(query, (nome, telefone, quantidade, dia, cliente_id))
    dados_conexao.commit()

    return jsonify({'status': 'Cliente atualizado com sucesso'}), 200

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    query = "SELECT * FROM cadastro_cliente WHERE id_cliente = ?"
    cursor.execute(query, cliente_id)
    cliente = cursor.fetchone()

    if cliente:
        try:
            quantidade = int(cliente.quantidade)
            calculo = quantidade * 7
            resultado = f' <strong>{quantidade} X 7 = {calculo:.2f}</strong>'
            contexto = f'O Cliente <strong>{cliente.nome_cliente}</strong> Comprou <strong>{cliente.quantidade}</strong> Garrafas'
            return f'{contexto}{resultado}'
        except ValueError:
            abort(400, description="Quantidade inválida")
    else:
        abort(404)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    query = "DELETE FROM cadastro_cliente WHERE id_cliente = ?"
    cursor.execute(query, cliente_id)
    dados_conexao.commit()

    return jsonify({'deleted': 'ok'})
