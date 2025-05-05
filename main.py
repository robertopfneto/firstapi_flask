from flask import Flask, make_response, jsonify
from bd import Carros
# Instanciando flask
app = Flask(__name__)

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(Carros) #Retornando a tabela carros 
    )
    


app.run()