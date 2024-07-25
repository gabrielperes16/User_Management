from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')


tabela_route= Blueprint('tabela',__name__)
@tabela_route.route('/tabela/<name_users>')
def tabela(name_users):
    return render_template('calculos.html',name_users=name_users)
