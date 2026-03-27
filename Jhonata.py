from flask import Flask, jsonify, request

app = Flask(__name__)
 
jogos = [
    {
        'id': 1,
        'titulo': 'God of War Ragnarok',
        'Data_Lancamento': '09 de Novembro de 2026'
    },
    {
        'id': 2,
        'titulo': 'God of war 2018',
        'Data_Lancamento': '20 de Abril de 2018'
    },
    {
        'id': 3,
        'titulo': 'The Last of Us',
        'Data_Lancamento': '14 de junho de 2013'
    }
]

#Consultar(todos)
@app.route('/jogos',methods=['GET'])
def obter_livros():
    return jsonify(jogos)
#Consultar(ID)
@app.route('/jogos/<int:id>', methods=['GET'])
def obter_jogos_por_id(id):
    for jogo in jogos:
        if jogo.get('id') == id:
            return jsonify(jogo)

#Editar
@app.route('/jogos/<int:id>', methods=['PUT'])
def editar_jogo_por_id(id):
    jogo_alterado = request.get_json()
    for indice, jogo in enumerate(jogos):
        if jogo.get('id') == id:
            jogos[indice].update(jogo_alterado)
            return jsonify(jogo[indice])
#Criar     
@app.route('/jogos', methods=['POST'])   
def incluir_novo_jogo():
    novo_jogo = request.get_json()
    livros.append(novo_jogo)
    return jsonify(jogos)

#Excluir
@app.route('/jogos/<int:id>', methods=['DELETE'])
def excluir_jogo(id):
    for indice, jogo in enumerate(jogos):
        if jogo.get('id') == id:
            del jogos[indice]

    return jsonify(jogos)

app.run(port=5000,host='localhost',debug=True)
