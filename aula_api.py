from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from def_api import conexao, deletar, inserir, selecionar, selecionar_tudo, atualizar

projeto = Flask(__name__)
api = Api(projeto)

parser = reqparse.RequestParser()
parser.add_argument("nome", type=str)


class Projeto(Resource):
    def get(self, codigo = None):
        if codigo == None:
            db = conexao()
            return selecionar_tudo(db)
        else:
            db = conexao()
            return selecionar(db, codigo)    


    def put(self, codigo):
        db = conexao()
        nome = request.form["nome"]
        atualizar(db, codigo, nome)
        return selecionar(db, codigo) 


    def post(self):
        db = conexao()
        args = parser.parse_args()
        nome = args["nome"]
        inserir(db, nome)
        return selecionar_tudo(db)


    def delete(self, codigo):
        db = conexao()
        deletar(db, codigo)
        return selecionar_tudo(db)

api.add_resource(Projeto, "/<int:codigo>", "/")


projeto.run(debug=True)












