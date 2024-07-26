from flask import Blueprint, render_template, request, redirect, url_for
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

# Documentation ⭳
"""
Rotas Clientes

    - /clientes/ (GET) - Listar os clientes
    - /clientes/ (POST) - Inserir um novo cliente
    - /clientes/new (GET) - Formulário para novo cliente
    - /clientes/<int:cliente_id> (GET) - Obter os dados de um cliente
    - /clientes/<int:cliente_id>/edit (GET) - Renderizar um formulário para editar
    - /clientes/<int:cliente_id>/update (PUT) - Atualizar os dados do cliente
    - /clientes/<int:cliente_id>/delete (DELETE) - Deletar o cliente
"""

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_cliente.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    print(request.json)
    return('ok')
@cliente_route.route('/new')
def form_cliente():
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_clientes(cliente_id):
    # Logic to get client details
    return render_template('detalhe_cliente.html', cliente_id=cliente_id)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    # Logic to get client details for editing
    return render_template('form_edit_cliente.html', cliente_id=cliente_id)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_clientes(cliente_id):
    # Logic to update client details
    return redirect(url_for('cliente.detalhe_clientes', cliente_id=cliente_id))

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_clientes(cliente_id):
    # Logic to delete client
    return redirect(url_for('cliente.lista_clientes'))
