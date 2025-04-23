# def setUp(self):
#         # Configura o app para modo de teste
#         app.config['TESTING'] = True
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#         self.app = app.test_client()
#         with app.app_context():
#             db.create_all()

#     def tearDown(self):
#         with app.app_context():
#             db.session.remove()
#             db.drop_all()

#     def client():
#         with app.test_client() as client:
#             with app.app_context():
#                 db.create_all()
#             yield client
#             with app.app_context():
#                 db.drop_all()


#     def test_crud_professor(client):
#         # Create
#         r = requests.post('http://127.0.0.1:8001/professor', json={
#             "nome": "Carlos",
#             "idade": 45,
#             "materia": "História",
#             "observacoes": "Pontual"
#         })
#         assert r.status_code == 200
#         professor_id = r.json()['id']

#         # Read
#         r = requests.get(f'http://127.0.0.1:8001/professor/{professor_id}')
#         assert r.status_code == 200
#         assert r.json()['nome'] == "Carlos"

#         # Update
#         r = requests.put(f'http://127.0.0.1:8001/professor/{professor_id}', json={
#             "nome": "Carlos Silva",
#             "idade": 46,
#             "materia": "História",
#             "observacoes": "Atualizado"
#         })
#         assert r.status_code == 200
#         assert r.json()['nome'] == "Carlos Silva"

#         # Delete
#         r = requests.delete(f'http://127.0.0.1:8001/professor/{professor_id}')
#         assert r.status_code == 200


#     def test_crud_turma(client):
#         # Pré-cria professor
#         r = requests.post(f'http://127.0.0.1:8001/professor', json={
#             "nome": "Ana",
#             "idade": 35,
#             "materia": "Matemática",
#             "observacoes": ""
#         })
#         prof_id = r.json()['id']

#         # Create turma
#         r = requests.post(f'http://127.0.0.1:8001/turma', json={
#             "descricao": "6º Ano A",
#             "professor_id": prof_id,
#             "ativo": "Sim"
#         })
#         assert r.status_code == 200
#         turma_id = r.json()['id']

#         # Read turma
#         r = requests.get(f'http://127.0.0.1:8001/turma/{turma_id}')
#         assert r.status_code == 200
#         assert r.json()['descricao'] == "6º Ano A"

#         # Update turma
#         r = requests.put(f'http://127.0.0.1:8001/turma/{turma_id}', json={
#             "descricao": "6º Ano B",
#             "professor_id": prof_id,
#             "ativo": "Sim"
#         })
#         assert r.status_code == 200
#         assert r.json()['descricao'] == "6º Ano B"

#         # Delete turma
#         r = requests.delete(f'http://127.0.0.1:8001/turma/{turma_id}')
#         assert r.status_code == 200


#     def test_crud_aluno(client):
#         # Cria professor e turma
#         r = requests.post(f'http://127.0.0.1:8001/professor', json={
#             "nome": "Fernanda",
#             "idade": 40,
#             "materia": "Geografia",
#             "observacoes": ""
#         })
        
#         professor_criado = r.json()
#         professor_id = professor_criado['id']


#         r = requests.post(f'http://127.0.0.1:8001/turma', json={
#             "descricao": "7º Ano C",
#             "professor_id": professor_id,
#             "ativo": "Sim"
#         })
#         turma_criada = r.json()
#         turma_id = turma_criada['id']

#         # Create aluno
#         r = requests.post(f'http://127.0.0.1:8001/alunos', json={
#             "nome": "Pedro",
#             "data_nascimento": "20/01/2010",
#             "nota_primeiro_semestre": 8.0,
#             "nota_segundo_semestre": 7.5,
#             "media_final": 7.75,
#             "turma_id": turma_id
#         })
#         assert r.status_code == 200
#         aluno_criado = r.json()
#         aluno_id = aluno_criado['id']

#         # Read aluno
#         r = requests.get(f'http://127.0.0.1:8001/alunos/{aluno_id}')
#         assert r.status_code == 200
#         print(r.content)
#         assert r.json()['nome'] == "Pedro"



#         # Update aluno
#         r = requests.put(f'http://127.0.0.1:8001/alunos/{aluno_id}', json={
#             "nome": "Pedro Silva",
#             "data_nascimento": "20/01/2010",
#             "nota_primeiro_semestre": 9.0,
#             "nota_segundo_semestre": 8.0,
#             "media_final": 8.5,
#             "turma_id": turma_id
#         })
#         assert r.status_code == 200
#         assert r.json()['nome'] == "Pedro Silva"

#         # Delete aluno
#         r = requests.delete(f'http://127.0.0.1:8001/alunos/{aluno_id}')
#         assert r.status_code == 200



# Criar testes de integração com o banco
# Swagger
# Relatório
# 4° Deploy 
# relação many populations
# --------------------
# - Passar para o MYSQL (Baixar e configurar)
# Criar uma função decodificação jwt - validação nas rotas - JWT
# 2° JTW
# - Mexer com o Docker
# - Deploy
 


'''--------------------------------------------------------------'''
# docker build -t saladeaula . - cria imagem (imagem é uma receita para o container)
# docker run -p 8001:8001 saladeaula professor - cria container

# duplicacao = verificar_duplicacao(dados['id'])
    # if duplicacao:
    #     return duplicacao

    # def verificar_duplicacao(id):
#     if Turma.query.get(id):
#         return jsonify({"error": f"Turma com id {id} já existe."}), 400
#     return None


# def setUp(self):
#     self.app = app.test_client()
#     self.app_context = app.app_context()
#     self.app_context.push()
    
#     # Limpa as tabelas manualmente
#     from models.modelAluno import Aluno
#     from models.modelProfessor import Professor
#     from models.modelTurma import Turma

#     db.session.query(Aluno).delete()
#     db.session.query(Turma).delete()
#     db.session.query(Professor).delete()
#     db.session.commit()