from flask import Flask
import biblioteca
import funcoes
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# Rota Raiz
# CORS(app, resources={r"/preco/*": {"origins": "*"}})
# CORS(app, resources={r"/garantia/*": {"origins": "*"}})
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin
@app.route("/")
# @cross_origin


def raiz():
    return "<h1>Olá : Mundo</h1>"

@cross_origin
@app.route("/preco/<item>")
# @cross_origin
def get_pesq_preco(item):
    dicionario = funcoes.pesqpreco(item)
    return json.dumps(dicionario)

@cross_origin
@app.route("/garantia/<nromotor>")
# @cross_origin
def get_garantia(nromotor):
    dicionario = biblioteca.ConsultaGarantia(nromotor)
    return json.dumps(dicionario)

if __name__ == "__main__":
    app.run(debug=True)
