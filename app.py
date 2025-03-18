from flask import Flask, jsonify, request

dici = {
    "alunos": [
        {
            "id": 1,
            "nome": "Nome do aluno",
            "idade": 0,
            "data_nascimento": "Data de nascimento",
            "nota_primeiro_semestre": 0,
            "nota_segundo_semestre": 0,
            "media_final": 0,
            "turma_id": 1
        }
    ],
    "professor": [
        {
            "id": 1,
            "nome": "Nome do professor",
            "idade": 0,
            "materia": "Nome da materia",
            "observacoes": "Observacao sobre o professor"
        }
    ],
    "turma": [
        {
            "id": 1,
            "descricao": "Descriçaõ da turma",
            "professor_id": 1,
            "ativo": "Status"
        }
    ]
}

app = Flask(__name__)

def verificar_duplicacao(id, lista, tipo):
    if any(item['id'] == id for item in lista):
        return jsonify({"error": f"{tipo} com ID {id} já existe."}), 400
    return None

def verificar_campo_null(dados):
    for chave, valor in dados.items():
        if valor == None:
            return jsonify({"error": "O campo " + chave + " informado é obrigatório."})
        
# POST (CREATE)
@app.route('/alunos', methods=['POST'])
def createAluno():
    try:
        dados = request.json
        
        vazio = verificar_campo_null(dados)
        if vazio:
            return vazio, 400

        
        turma_existente = next((turma for turma in dici["turma"] if turma["id"] == dados["turma_id"]), None)
        if not turma_existente:
            return jsonify({"error": "Turma não encontrada."}), 404
        
        
        duplicacao = verificar_duplicacao(dados['id'], dici["alunos"], "Aluno")
        if duplicacao:
            return duplicacao
        

        # dados['id'] = max([aluno['id'] for aluno in dici["alunos"]]) + 1 if dici["alunos"] else 1
        dici['alunos'].append(dados)
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/professor', methods=['POST'])
def createProfessores():
    try:
        dados = request.json
        # dados['id'] = max([professor['id'] for professor in dici["professor"]]) + 1 if dici["professor"] else 1

        vazio = verificar_campo_null(dados)
        if vazio:
            return vazio, 400
        
        duplicacao = verificar_duplicacao(dados['id'], dici["professor"], "Professor")
        if duplicacao:
            return duplicacao
        
        dici['professor'].append(dados)
        
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/turma', methods=['POST'])
def createTurma():
    try:
        dados = request.json

        vazio = verificar_campo_null(dados)
        if vazio:
            return vazio, 400
        
        professor_existente = next((professor for professor in dici["professor"] if professor["id"] == dados["professor_id"]), None)
        if not professor_existente:
            return jsonify({"error": "Professor não encontrado."}), 404
        
        duplicacao = verificar_duplicacao(dados['id'], dici["turma"], "Turma")
        if duplicacao:
            return duplicacao

        # dados['id'] = max([turma['id'] for turma in dici["turma"]]) + 1 if dici["turma"] else 1
        dici['turma'].append(dados)
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET (READ)
@app.route('/alunos', methods=['GET'])
def getAluno():
    dados = dici['alunos'] 
    return jsonify(dados), 200

@app.route("/professor", methods=['GET'])
def getProfessor():
    dados = dici['professor']
    return jsonify(dados), 200

@app.route('/turma', methods=['GET'])
def getTurma():
    dados = dici['turma']
    return jsonify (dados), 200

# PUT (UPDATE)
@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    try:
        dados = request.json
        
        vazio = verificar_campo_null(dados)
        if vazio:
            return vazio, 400
        
        aluno = next((aluno for aluno in dici["alunos"] if aluno["id"] == idAluno), None)
        if not aluno:
            return jsonify({"error": "Aluno nao encontrado"}), 404

        
        dados = request.json
        aluno.update(dados)
        return jsonify(aluno), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/professor/<int:idProfessor>", methods=['PUT'])
def updateProfessores(idProfessor):
    try:
        dados = request.json

        vazio = verificar_campo_null(dados)
        if vazio:
            return vazio, 400
        
        professor = next((professor for professor in dici["professor"] if professor["id"] == idProfessor), None)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404
        
        
        professor.update(dados)
        return jsonify(professor)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/turma/<int:idTurma>", methods=['PUT'])
def updateTurma(idTurma):
    try:
        dados = request.json

        vazio = verificar_campo_null(dados)
        if vazio:
            return vazio, 400
        
        turma = next((turma for turma in dici["turma"] if turma["id"] == idTurma), None)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404
        
        
        turma.update(dados)
        return jsonify(turma), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#DELETE
@app.route('/alunos/<int:idAluno>', methods=['DELETE'])
def delete_aluno(idAluno):
    try:
        aluno = next((aluno for aluno in dici["alunos"] if aluno["id"] == idAluno), None)
        if not aluno:
            return jsonify({"error": "Aluno não encontrado"}), 404
        
        dici["alunos"].remove(aluno)
        return jsonify({"message": f"Aluno com ID {idAluno} foi removido com sucesso."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
        
@app.route('/professor/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    try:
        professor = next((professor for professor in dici["professor"] if professor["id"] == idProfessor), None)
        if not professor:
            return jsonify({"error": "Professor não encontrado"}), 404
        
        dici["professor"].remove(professor)
        return jsonify({"message": f"Professor com ID {idProfessor} foi removido com sucesso."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/turma/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
    try:
        turma = next((turma for turma in dici["turma"] if turma["id"] == idTurma), None)
        if not turma:
            return jsonify({"error": "Turma não encontrada"}), 404
        
        dici["turma"].remove(turma)
        return jsonify({"message": f"Turma com ID {idTurma} foi removida com sucesso."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
