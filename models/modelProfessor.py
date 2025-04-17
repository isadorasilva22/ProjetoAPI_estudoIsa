from flask import jsonify
from config import db

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100))
    observacoes = db.Column(db.String(100))

    turmas = db.relationship('Turma', backref='Professor', lazy=True)

    def __init__(self, nome, idade, materia, observacoes):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes


    def to_dict(self):
        return {'id': self.id,
                'nome': self.nome,
                'idade': self.idade,
                'materia': self.materia,
                'observacoes': self.observacoes
                }

def verificar_duplicacao(id):
    if Professor.query.get(id):
        return jsonify({"error": f"Professor com ID {id} já existe."}), 400
    return None

def verificar_campo_null(dados):
    for chave, valor in dados.items():
        if valor == None:
            return jsonify({"error": f"O campo" + chave + "informado é obrigatório."}), 400
    return None

# Create
def createProfessor(dados):    
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio

    duplicacao = verificar_duplicacao(dados['id'])
    if duplicacao:
        return duplicacao

    novo_professor = Professor(
        nome=dados['nome'],
        idade=dados['idade'],
        materia=dados['materia'],
        observacoes=dados['observacoes']
    )

    db.session.add(novo_professor)
    db.session.commit()

    return jsonify(novo_professor.to_dict()), 200

# Get      
def todosProfessores():
    professores = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professores]), 200
    
def professorPorID(idProfessor):
    professor = Professor.query.get(idProfessor)
    if professor:
        return jsonify(professor.to_dict()), 200
    return jsonify({"error": "Professor não encontrado"}), 404

# Put
def updateProfessor(idProfessor, dados):
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio

    professor = Professor.query.get(idProfessor)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404

    for chave, valor in dados.items():
        if hasattr(professor, chave):
            setattr(professor, chave, valor)

    db.session.commit()
    return jsonify(professor.to_dict()), 200

# Delete

def deleteProfessor(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        return jsonify({"error": "Professor não encontrado"}), 404

    db.session.delete(professor)
    db.session.commit()
    return jsonify({"message": "Professor deletado com sucesso"}), 200
    
print(Professor.__table__)
