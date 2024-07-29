from flask import Blueprint, render_template, request
from database.cliente import CLIENTES
from database.models.cliente import Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    """ listar os clientes """
    clientes=Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)
    

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ inserir os dados do cliente """
    
    data = request.json
      
    novo_usuario = Cliente.create(
        nome = data['nome'],
        data = data['data'],
        quantidade = data['quantidade']
    )
    return render_template('item_cliente.html', cliente=novo_usuario)
    

@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar um cliente """
    return render_template('form_cliente.html')
    

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ exibir detalhes do cliente """
    
    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('detalhe_cliente.html', cliente=cliente)
    

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ formulario para editar um cliente """
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    
    return render_template('form_cliente.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar informacoes do cliente """
    cliente_editado = None
    # obter dados do formulario de edicao
    data = request.json
    
    # obter usuario pelo id
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['data'] = data['data']
           
            
            cliente_editado = c
            
    # editar usuario
    return render_template('item_cliente.html', cliente=cliente_editado)
    

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):   
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id ]
    return {'deleted': 'ok'}
