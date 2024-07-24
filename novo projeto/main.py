from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    usuarios = {'nome':'Gabriel'}
    return render_template('inicial.html', usuarios=usuarios)

@app.route('/2')
def tabela():
    return render_template('tabela.html')

@app.route('/usuarios/<name_users>')
def usuarios(name_users):
    return render_template('name_users.html', name_users=name_users)

if __name__ == '__main__':
    app.run(debug=True)
