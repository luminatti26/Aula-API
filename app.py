from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

dado = {1: "ronaldo", 2: "rivaldo"}

class Helloworld(Resource):
    def get(self, codigo):
        return dado[codigo]


    def put(self, codigo):
        dado[codigo] = request.form["nome"]
        return dado


    def delete(self, codigo):
        dado.pop(codigo)
        return dado

api.add_resource(Helloworld, "/<int:codigo>")


app.run(debug=True)






