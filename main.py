from flask import Flask, make_response, jsonify, request
from bd import Carros
# Instanciando flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            message='Lista de carros.',
            data = Carros
            ) #Retornando a tabela carros 
    )
    
@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json #faz uma requisicao solicitando o bojeto
    Carros.append(carro) # adiciono na lista o carro
    return make_response(
        jsonify(
            message='Carro cadastrado com sucesso!',
            data=carro
        )
    )


app.run()