from flask import Flask, jsonify,render_template
from tabela import lista_users
#Routes
#funções
#Template
app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/2')
def tabela():
    return render_template('tabela.html')

@app.route('/usuarios/<name_users>')
def usuarios(name_users):
    return render_template('name_users.html', name_users=name_users)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
