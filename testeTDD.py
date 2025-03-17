import requests
import unittest


class TestStringMethods(unittest.TestCase):

#Testar criação

    def test_criar_professor(self):
        r = requests.post('http://127.0.0.1:5000/professor', json={
            'id':2,
            'nome':'Caio',
            'idade':26, 
            'materia': "Desenvolvimento de APIs",
            'observacoes': "Flask"})
            
        if r.status_code != 201:
            self.fail(f"Erro ao criar professor Caio. Status Code: {r.status_code}")

        r = requests.post('http://127.0.0.1:5000/professor', json={
            'id':3,
            'nome':'Mariana',
            'idade':26, 
            'materia': "Matemática Aplica",
            'observacoes': "Operadores"})
        
            
        if r.status_code != 201:
            self.fail(f"Erro ao criar professor Mariana. Status Code: {r.status_code}")
                
        r_lista = requests.get('http://127.0.0.1:5000/professor')
        if r_lista.status_code != 200:
            self.fail(f"Erro ao obter a lista de professores. Status Code: {r_lista.status_code}")
                
        lista_retornada = r_lista.json()
        achei_caio = False
        achei_mari = False
        for professor in lista_retornada:
            if professor['nome'] == 'Caio':
                achei_caio = True
            if professor['nome'] == 'Mariana':
                achei_mari = True
            
        if not achei_caio:
            self.fail('Professor Caio não apareceu na lista de professores')
        if not achei_mari:
            self.fail('Professora Matemática Aplicada não apareceu na lista de professores')

    def test_retorna_lista_professores(self):
        r = requests.get('http://127.0.0.1:5000/professor')
        if r.status_code == 404:
            self.fail("Voce nao definiu a pagina '/professor' no seu server")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))   


    def test_criar_turma(self):
        r = requests.post('http://127.0.0.1:5000/turma', json={
            'id':2,
            'descricao':'Desenvolvimento de APIs',
            'professor_id':2, 
            'ativo': "Ativo"})
            
        if r.status_code != 201:
            self.fail(f"Erro ao criar turma Desenvolvimento de APIs. Status Code: {r.status_code}")

        r = requests.post('http://127.0.0.1:5000/turma', json={
            'id':3,
            'descricao':'Matemática Aplicada',
            'professor_id':3, 
            'ativo': "Ativo"})
            
        if r.status_code != 201:
            self.fail(f"Erro ao criar turma Matemática Aplicada. Status Code: {r.status_code}")
                
        r_lista = requests.get('http://127.0.0.1:5000/turma')
        if r_lista.status_code != 200:
            self.fail(f"Erro ao obter a lista de turmas. Status Code: {r_lista.status_code}")
                
        lista_retornada = r_lista.json()
        achei_api = False
        achei_mat = False
        for aluno in lista_retornada:
            if aluno['descricao'] == 'Desenvolvimento de APIs':
                achei_api = True
            if aluno['descricao'] == 'Matemática Aplicada':
                achei_mat = True
            
        if not achei_api:
            self.fail('Turma Desenvolvimento de APIs não apareceu na lista de turmas')
        if not achei_mat:
            self.fail('Turma Matemática Aplicada não apareceu na lista de turma')


    def test_retorna_lista_turma(self):
        r = requests.get('http://127.0.0.1:5000/turma')
        if r.status_code == 404:
            self.fail("Voce nao definiu a pagina '/turma' no seu server")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))

    def test_criar_aluno(self):
        r = requests.post('http://127.0.0.1:5000/alunos', json={
            'id': 4,
            'nome': 'José',
            'idade': 19,
            'data_nascimento': "13/05/2005",
            'nota_primeiro_semestre': 9,
            'nota_segundo_semestre': 8,
            'media_final': 8.5,
            'turma_id': 1
        })
        if r.status_code != 201:
            self.fail(f"Erro ao criar aluno José. Status Code: {r.status_code}")

        r = requests.post('http://127.0.0.1:5000/alunos', json={
            'id': 5,
            'nome': 'Letícia',
            'idade': 19,
            'data_nascimento': "22/02/2004",
            'nota_primeiro_semestre': 10,
            'nota_segundo_semestre': 8,
            'media_final': 9,
            'turma_id': 1
        })
        if r.status_code != 201:
            self.fail(f"Erro ao criar aluna Letícia. Status Code: {r.status_code}")
            
        r_lista = requests.get('http://127.0.0.1:5000/alunos')
        if r_lista.status_code != 200:
            self.fail(f"Erro ao obter a lista de alunos. Status Code: {r_lista.status_code}")
            
        lista_retornada = r_lista.json()
        achei_jose = False
        achei_leticia = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'José':
                achei_jose = True
            if aluno['nome'] == 'Letícia':
                achei_leticia = True
        
        if not achei_jose:
            self.fail('Aluno José não apareceu na lista de alunos')
        if not achei_leticia:
            self.fail('Aluna Letícia não apareceu na lista de alunos')
    
    def test_retorna_lista_alunos(self):
        r = requests.get('http://127.0.0.1:5000/alunos')
        if r.status_code == 404:
            return self.fail("Voce nao definiu a pagina '/alunos' no seu server")
            
        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))

        
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
 



# Testar campos nulos
# Testar Atualizar
# Testar Apagar
# Testar reseta
