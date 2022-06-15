
from flask import Flask
import biblioteca
import funcoes
import json
import os 

app = Flask(__name__)

# Rota Raiz


@app.route("/")
def raiz():
    return "<h1>Olá : Mundo</h1>"


@app.route("/preco/<item>")
def get_pesq_preco(item):
    dicionario = funcoes.pesqpreco(item)
    return json.dumps(dicionario)


@app.route("/garantia/<nromotor>")
def get_garantia(nromotor):
    dicionario = biblioteca.ConsultaGarantia(nromotor)
    return json.dumps(dicionario)


if __name__ == "__main__":
    # port = int(os.getenv('PORT'), '80')
    app.run(debug=True)
    