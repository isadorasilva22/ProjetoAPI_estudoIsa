
@app.route('/professor',methods=['POST'])


def createProfessores():
    try:
        dados = request.get_json()  
        if not dados:
            return jsonify({"error": "Dados inválidos no corpo da requisição."}), 400

        dici['professor'].append(dados)
        return jsonify(dados), 201  
    except Exception as e:
        print(f"Erro ao criar professor: {e}")
        return jsonify("error"), 500
    

def createTurma():
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"error": "Dados inválidos no corpo da requisição."}), 400

        professor_id = dados.get('professor_id')
        if professor_id is None:
            return jsonify({"error": "Campo 'professor_id' é obrigatório."}), 400

        professor_encontrado = False
        for professor in dici["professor"]:
            if professor["id"] == professor_id:
                dici['turma'].append(dados)
                professor_encontrado = True
                return jsonify(dados), 201
        
        if not professor_encontrado:
            return jsonify({"error": f"Professor com ID {professor_id} não encontrado."}), 404
            
    except :
        print("Erro ao criar turma")
        return jsonify({"error"}), 500

    
def updateAlunos(idAluno):
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"error": "Dados inválidos no corpo da requisição."}), 400

        for aluno in dici["alunos"]:
            if aluno['id'] == idAluno:
                # Atualiza os campos, usando .get() para valores opcionais
                aluno['id'] = dados.get('id', aluno['id'])  # Mantém o valor antigo se 'id' não estiver nos dados
                aluno['nome'] = dados.get('nome', aluno['nome'])

                return jsonify(aluno), 200

        return jsonify({"error": f"Aluno com ID {idAluno} não encontrado."}), 404



def updateTurma(idTurma):
    try:
        dados = request.get_json()
        if not dados:
            return jsonify({"error": "Dados inválidos no corpo da requisição."}), 400

        for turma in dici["turma"]:  
            if turma['id'] == idTurma:
                turma['id'] = dados.get('id', turma['id'])
                turma['nome'] = dados.get('nome', turma['nome']) 
                return jsonify(turma), 200

        return jsonify({"error": f"Turma com ID {idTurma} não encontrada."}), 404
    except Exception as e:
        print(f"Erro ao atualizar turma: {e}")
        return jsonify({"error": f"Erro interno ao atualizar turma: {str(e)}"}), 500

