from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ listar os clientes """
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)
    

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.form
    novo_cliente = Cliente.create(
        nome=data['nome'],
        email=data['email'],  # Certifique-se de que 'email' é fornecido
        data_registro=data['data_registro']
    )
    return render_template('item_cliente.html', cliente=novo_cliente)


@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar um cliente """
    return render_template('form_cliente.html')
    

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ exibir detalhes do cliente """
    
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)
    

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ formulario para editar um cliente """
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
@cliente_route.route('/<int:cliente_id>/update', methods=['POST'])
def atualizar_cliente(cliente_id):
    data = request.form
    cliente = Cliente.get_by_id(cliente_id)
    cliente.nome = data['nome']
    cliente.email = data['email']  # Certifique-se de que 'email' é fornecido
    cliente.data_registro = data['data_registro']
    cliente.save()
    return render_template('item_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):   
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}