from flask import Flask, jsonify, request

app = Flask(__name__)
 
exercicios = [
    {
        'id': 1,
        'exercicio': 'Supino inclinado',
        'musculo': 'Peitoral superior'
    },
    {
        'id': 2,
        'exercicio': 'Elevação lateral',
        'musculo': 'Porção lateral do ombro'
    },
    {
        'id': 3,
        'exercicio': 'Tríceps barra reta',
        'musculo': 'Tríceps'
    }
]

# Consultar (todos)
@app.route('/exercicios', methods=['GET'])
def obter_exercicios():
    return jsonify(exercicios)

# Consultar (ID)
@app.route('/exercicios/<int:id>', methods=['GET'])
def obter_exercicio_por_id(id):
    for exercicio in exercicios:
        if exercicio.get('id') == id:
            return jsonify(exercicio)

# Editar
@app.route('/exercicios/<int:id>', methods=['PUT'])
def editar_exercicio_por_id(id):
    exercicio_alterado = request.get_json()
    for indice, exercicio in enumerate(exercicios):
        if exercicio.get('id') == id:
            exercicios[indice].update(exercicio_alterado)
            return jsonify(exercicios[indice])

# Criar     
@app.route('/exercicios', methods=['POST'])   
def incluir_novo_exercicio():
    novo_exercicio = request.get_json()
    exercicios.append(novo_exercicio)
    return jsonify(exercicios)

# Excluir
@app.route('/exercicios/<int:id>', methods=['DELETE'])
def excluir_exercicio(id):
    for indice, exercicio in enumerate(exercicios):
        if exercicio.get('id') == id:
            del exercicios[indice]

    return jsonify(exercicios)

app.run(port=5000, host='localhost', debug=True)