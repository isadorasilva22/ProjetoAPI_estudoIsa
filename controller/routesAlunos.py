from flask import Blueprint, request, jsonify
from models import modelAluno

alunos_bp = Blueprint('alunos', __name__) #Criando uma instância

#Create
@alunos_bp.route('/alunos', methods=['POST'])
def createAluno():
    try:
        dados = request.json
        return modelAluno.createAluno(dados)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#Get
@alunos_bp.route('/alunos', methods=['GET'])
def getAluno():
    try:
        return modelAluno.todosAlunos()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@alunos_bp.route('/alunos/<int:idAluno>', methods=['GET'])
def aluno_Id(id_aluno):
    try:
        return modelAluno.alunoPorID(id_aluno)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#Put
@alunos_bp.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    try:
        dados = request.json
        return modelAluno.updateAluno(idAluno, dados)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#Delete
@alunos_bp.route('/alunos/<int:idAluno>', methods=['DELETE'])
def delete_aluno(idAluno):

    if modelAluno.deleteAluno(idAluno) == True:
        return jsonify ({"message": "Aluno excluído com sucesso"}), 200
    
    else:
        return jsonify({"message": "Aluno não encontrado"}), 404
