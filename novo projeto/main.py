from flask import Flask
from routes.home import home_route,tabela_route # assuming this code is in a file named home_blueprint.py

app = Flask(__name__)
app.register_blueprint(home_route)
app.register_blueprint(tabela_route)
if __name__ == '__main__':
    app.run(debug=True)
