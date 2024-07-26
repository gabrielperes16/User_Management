from flask import Blueprint,render_template
from database.cliente import CLIENTES
cliente_route = Blueprint('cliente', __name__)

    #Documentation ⭳
"""
Rotas Clientes

    -/clientes/ (GET)- Listar os clientes
    -/clientes/ (POST) - Listar os clientes
    -/clientes/new (GET)- Listar os clientes
    -/clientes/<id> - obter os dados de um cliente
    -/clientes/<id>/edit- renderizar um formulario para editar
    -/clientes/<id>/update- atualizar os dados do clientes
    -/clientes/<id>/delete  (DELETE)- atualizar os dados do clientes
"""

@cliente_route .route('/')
def lista_clientes():
    return  render_template('lista_cliente.html', clientes=CLIENTES)



@cliente_route .route('/', methods=['POST'])
def inserir_clientes(cliente_id):
    pass
    
@cliente_route .route('/new')
def form_cliente(cliente_id):
    return render_template('form_cliente.html')


@cliente_route .route('/<int:cliente_id>')
def detalhe_clientes(cliente_id):
    return render_template('detalhe_cliente.html')
    

    
@cliente_route .route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')
    

@cliente_route .route('/<int:cliente_id>/update',methods=['PUT'])
def atualizar_clientes(cliente_id):
    pass
    

@cliente_route .route('/<int:cliente_id>/delete',methods=['DELETE'])
def deletar_clientes(cliente_id):
    pass
    

