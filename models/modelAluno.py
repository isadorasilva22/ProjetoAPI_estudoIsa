from flask import jsonify
from models.modelTurma import turmaPorID
from config import db
from datetime import datetime

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    data_nascimento = db.Column(db.Date)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

    turma = db.relationship('Turma', backref='Aluno')

    def __init__(self, nome, idade, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final, turma_id):
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final
        self.turma_id = turma_id


    def to_dict(self):
        return {'id': self.id,
                'nome': self.nome,
                'idade': self.idade,
                'data_nascimento': self.data_nascimento,
                'nota_primeiro_semestre': self.nota_primeiro_semestre,
                'nota_segundo_semestre': self.nota_segundo_semestre,
                'media_final': self.media_final,
                'turma_id': self.turma_id}

def verificar_duplicacao(id):
    if Aluno.query.get(id):
        return jsonify({"error": f"Aluno com ID {id} já existe."}), 400
    return None

def verificar_campo_null(dados):
    for chave, valor in dados.items():
        if valor == None:
            return jsonify({"error": f"O campo" + chave + "informado é obrigatório."}), 400
    return None

# Create
def createAluno(dados):    
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio

    turma_existente = turmaPorID(dados['turma_id'])
    if not turma_existente:
        return jsonify({"error": "Turma não existe"}), 404

    duplicacao = verificar_duplicacao(dados['id'])
    if duplicacao:
        return duplicacao

    novo_aluno = Aluno(
        nome=dados['nome'],
        idade=dados['idade'],
        data_nascimento=datetime.strptime(dados['data_nascimento'], "%d/%m/%Y"),
        nota_primeiro_semestre=dados['nota_primeiro_semestre'],
        nota_segundo_semestre=dados['nota_segundo_semestre'],
        media_final=dados['media_final'],
        turma_id=dados['turma_id']
    )

    db.session.add(novo_aluno)
    db.session.commit()

    return jsonify(novo_aluno.to_dict()), 200

# Get      
def todosAlunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos]), 200
    
def alunoPorID(idAluno):
    aluno = Aluno.query.get(idAluno)
    if aluno:
        return jsonify(aluno.to_dict()), 200
    return jsonify({"error": "Aluno não encontrado"}), 404

# Put
def updateAluno(idAluno, dados):
    vazio = verificar_campo_null(dados)
    if vazio:
        return vazio

    aluno = Aluno.query.get(idAluno)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404

    for chave, valor in dados.items():
        if hasattr(aluno, chave):
            setattr(aluno, chave, valor)

    db.session.commit()
    return jsonify(aluno.to_dict()), 200

# Delete

def deleteAluno(idAluno):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"}), 404

    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno deletado com sucesso"}), 200
    
            
    