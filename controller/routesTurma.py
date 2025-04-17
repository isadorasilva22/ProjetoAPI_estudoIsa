from flask import Blueprint, request, jsonify
from models import modelTurma

turma_bp = Blueprint('turma', __name__) #Criando uma instância
 
# POST (CREATE)

@turma_bp.route('/turma', methods=['POST'])
def createTurma():
    try:
        dados = request.json

        modelTurma.createTurma(dados)
        return jsonify(dados), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET (READ) - TURMA  
  
@turma_bp.route('/turma', methods=['GET'])
def getTurma():
    try: 
        return modelTurma.todasTurmas() 
    except Exception as e:
        return jsonify ({"error": str(e)}), 500

@turma_bp.route('/turma/<int:id_turma>', methods=['GET'])
def turma_Id(id_turma):
    try:
        modelTurma.turmaPorID(id_turma)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# PUT (UPDATE)

@turma_bp.route("/turma/<int:idTurma>", methods=['PUT'])
def updateTurma(idTurma):
    try:
        dados = request.json

        turma = modelTurma.updateTurma(idTurma, dados)
        return jsonify(turma)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#DELETE

@turma_bp.route('/turma/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
    if modelTurma.deleteTurma(idTurma) == True:
        return jsonify({"message": "Turma excluída com sucesso."}), 200
    else:
        return jsonify({"message": "Turma não encontrada."}), 404

