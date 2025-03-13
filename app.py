from flask import Flask, jsonify, request
#app.debbug
#Dicionário

dici = {
    "alunos":[
        {
            "id":1,
            "nome":"caio",
            "idade": 25,
            "turma_id": 3,
            "data_nascimento": "10/10/2005",
            "nota_primeiro_semestre": 10.00,
            "nota_segundo_semestre": 9.00,
            "media_final": 9.00
        }
    ],

    "professor":[
        {
            "id":2,
            "nome":"rafael",
            "idade": 15,
            "materia": "Desenvolvimento web",
            "observacoes": "Gosto de lesionar"
        }
    ],

     "turma":[
        {
            "id":3,
            "descricao":"api's",
            "professor_id":2,
            "ativo": "Ativa"
        }
    ]
}

app = Flask(__name__) #Criação de uma instância da classe Flask. __name__ representa o nome do módulo atual


#POST (CREATE)
@app.route('/alunos',methods=['POST'])
def createAluno():
    dados = request.json
    print(dados)
    for turma in dici["turma"]:
        if turma["id"] == dados["turma_id"]:
            dici['alunos'].append(dados)
            return jsonify(dados)
        else:
            return jsonify(["Não foi possível inserir o aluno na turma."])

        



@app.route('/professor',methods=['POST'])
def createProfessores():
    dados = request.json
    dici['professor'].append(dados)
    return jsonify(dados)

@app.route('/turma',methods=['POST'])
def createTurma():
    dados = request.json
    print(dados)

    for professor in dici["professor"]:
        if professor["id"] == dados["professor_id"]:
            dici['turma'].append(dados)
            return jsonify(dados)
        else:
            return jsonify(["Não foi possível cadastrar o professor na turma."])

#GET(READ)
@app.route('/alunos', methods=['GET']) #define a rota para a api - precisa obrigatoriamente de uma função
def getAluno():
    dados = dici['alunos']
    return jsonify(dados) #retorna os dados em formato json

@app.route("/professor", methods=['GET'])
def getProfessor():
    dados = dici['professor']
    return jsonify(dados)

@app.route ('/turma', methods=['GET'])
def getTurma():
    dados = dici['turma']
    return jsonify (dados)

#PUT(UPDATE)
@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    alunos = dici["alunos"]
    for aluno in alunos:
        if aluno['id'] == idAluno:
            dados = request.json
            aluno["id"] = dados['id']
            aluno['nome'] = dados['nome']
            return jsonify(dados)
        else:
            return jsonify("Aluno não encontrado")
        
@app.route("/professor/<int:idProfessor>", methods=['PUT'])
def updateProfessores(idProfessor):
    professor = dici["professor"]
    for professor in professor :
        if professor['id'] == idProfessor:
            dados = request.json
            professor["id"] = dados['id']
            professor['nome'] = dados['nome']
            return jsonify(dados)
        else:
            return jsonify("Professor não encontrado")
        
@app.route("/turma/<int:idTurma>", methods=['PUT'])
def updateTurma(idTurma):
    turmas = dici["Turma"]
    for turma in turmas:
        if turma['id'] == idTurma:
            dados = request.json
            turma["id"] = dados['id']
            turma['nome'] = dados['nome']
            return jsonify(dados)
        else:
            return jsonify("Turma não encontrada")
        


if __name__ == '__main__': #Verifica se está sendo executado pelo python
    app.run(debug=True) #Se estiver sendo executado, ent app.run inicia o servidor de desenv do flask
#O argumento debug=True ativa o modo de depuração, o que é útil durante o desenvolvimento, pois fornece mensagens de erro detalhadas e reinicia
#automaticamente o servidor quando o código é alterado.



# Todos do grupo vai ter que fazer esse processo
#vai ter que ter 3 post(create), delete, get(read), put(update) - crud para professor, aluno e turma
