# from email.mime import base
# from lib2to3.pytree import Base
# from fastapi import FastAPI
from flask import Flask
from pydantic import BaseModel
# import uvicorn
import biblioteca
import funcoes
import json
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

# Rota Raiz


@app.route("/")
def raiz():
    return "<h1>Olá : Mundo</h1>"

# Criar model


# class Usuario(BaseModel):
#     id: int
#     email: str
#     senha: str


# # Criar base de dados
# base_de_dados = [
#     Usuario(id=1, email="teste@teste.com", senha="teste=123"),
#     Usuario(id=2, email="teste1@teste.com", senha="teste=1234")
# ]
# # Rota Get All


@app.route("/preco/<item>")
def get_pesq_preco(item):
    dicionario = funcoes.pesqpreco(item)
    return json.dumps(dicionario)

@app.route("/garantia/<nromotor>")
def get_garantia(nromotor):
    dicionario = biblioteca.ConsultaGarantia(nromotor)
    return json.dumps(dicionario)


# Rota Get Id

# @app.route("/usuarios/{id_usuario}")
# def get_usuario_usando_id(id_usuario: int):
#     for usuario in base_de_dados:
#         if(usuario.id == id_usuario):
#             return usuario
#     return {"Statud": 404, "Mensagem": "Não encontrado o usuario"}

# Rota Insere"


# @app.route("/usuario")
# def insere_usuario(usuario: Usuario):
#     # criar regras de negocio
#     base_de_dados.append(usuario)
#     return usuario

if __name__ == "__main__":  
    app.run(debug=True)
    
