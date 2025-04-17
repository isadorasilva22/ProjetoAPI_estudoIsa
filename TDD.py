import requests
import unittest


class TestStringMethods(unittest.TestCase):


    def test_campo_professor_nome_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "id": '',
            "nome": None,
            "idade": 0,
            "materia": "Nome da materia",
            "observacoes": "Observacao sobre o professor"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo nome informado é obrigatório.', r.json()['error'])

    def test_campo_professor_idade_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "id": '',
            "nome": "Priscilla",
            "idade": None,
            "materia": "Nome da materia",
            "observacoes": "Observacao sobre o professor"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo idade informado é obrigatório.', r.json()['error'])

    def test_campo_professor_materia_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "id": '',
            "nome": "Marcos",
            "idade": 0,
            "materia": None,
            "observacoes": "Observacao sobre o professor"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo materia informado é obrigatório.', r.json()['error'])

    def test_campo_professor_obervacoes_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "id": '',
            "nome": "Lima",
            "idade": 0,
            "materia": "Fisica",
            "observacoes": None
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo observacoes informado é obrigatório.', r.json()['error'])

    def test_update_professor_successo(self):
        r = requests.post('http://127.0.0.1:8001/professor', json={ 
            "id": 10,
            "nome": "Romário",
            "idade": 30,
            "materia": "Desenvolvimento Web",
            "observacoes": "Nenhuma"
        })

       
        assert r.status_code in [200, 200]

        updated_r = {
            "id": 10,
            "nome": "Romário Silva",
            "idade": 30,
            "materia": "Desenvolvimento Web",
            "observacoes": "Nenhuma"
        }
        
        response = requests.put('http://127.0.0.1:8001/professor/10', json=updated_r, headers={"Content-Type": "application/json"})
       

        #tá faltando um get
        assert response.status_code == 200 #Perguntar se o erro é na saída 200 ou no "response.status_code"

        updated_professor = response.json()
        assert updated_professor['nome'] == "Romário Silva"
        assert updated_professor['idade'] == 30
        assert updated_professor['materia'] == "Desenvolvimento Web"
        
        get_response = requests.get('http://127.0.0.1:8001/professor')
        assert get_response.status_code == 200        

    def test_delete_professor(self): 
        r = requests.post('http://127.0.0.1:8001/professor', json={
            'id':8,
            'nome':'Alessandra',
            'idade':63, 
            'materia': "Geografia",
            'observacoes': "Altitude e latitude"
        })
        if r.status_code != 200:
            self.fail(f"Erro ao criar professora Alessandra. Status Code: {r.status_code}")

        professor_criado = r.json()
        professor_id = professor_criado['id']

        r = requests.delete(f'http://127.0.0.1:8001/professor/{professor_id}')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Professor excluído com sucesso', r.json()['message'])

        r_lista = requests.get('http://127.0.0.1:8001/professor')
        self.assertEqual(r_lista.status_code, 200)
        lista_retornada = r_lista.json()
        
        achei_alessandra = False
        for professor in lista_retornada:
            if professor['nome'] == 'Alessandra':
                achei_alessandra = True

        self.assertFalse(achei_alessandra, "A professora Alessandra ainda está na lista de alunos.")

    def test_criar_professor(self):
        r = requests.post('http://127.0.0.1:8001/professor', json={
            'id':2,
            'nome':'Caio',
            'idade':26, 
            'materia': "Desenvolvimento de APIs",
            'observacoes': "Flask"
            })
            
        if r.status_code != 200:
            self.fail(f"Erro ao criar professor Caio. Status Code: {r.status_code}")

        r = requests.post('http://127.0.0.1:8001/professor', json={
            'id':3,
            'nome':'Mariana',
            'idade':26, 
            'materia': "Matemática Aplica",
            'observacoes': "Operadores"})
        
            
        if r.status_code != 200:
            self.fail(f"Erro ao criar professor Mariana. Status Code: {r.status_code}")
                
        r_lista = requests.get('http://127.0.0.1:8001/professor')
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
        r = requests.get('http://127.0.0.1:8001/professor')
        if r.status_code == 404:
            self.fail("Voce nao definiu a pagina '/professor' no seu server")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))   


# TURMA

    def test_campo_turma_descricao_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "id": '',
            "descricao": None,
            "professor_id": 1,
            "ativo": "Status"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo descricao informado é obrigatório.', r.json()['error'])

    def test_campo_turma_professor_id_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "id": '',
            "descricao": "testes rapidos",
            "professor_id": None,
            "ativo": "Status"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo professor_id informado é obrigatório.', r.json()['error'])

    def test_campo_ativo_descricao_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "id": '',
            "descricao": "Probabilidades",
            "professor_id": 1,
            "ativo": None
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo ativo informado é obrigatório.', r.json()['error'])

    def test_update_turma_successo(self):
        r = requests.post('http://127.0.0.1:8001/turma', json={ 
            "id": 10,
            "descricao": "Desenvolvimento Mobile",
            "professor_id": 1,
            "ativo": "Ativo"
        })

       
        assert r.status_code == 200

        updated_r = {
            "id": 10,
            "descricao": "Desenvolvimento Mobile - Kotlin",
            "professor_id": 1,
            "ativo": "Desativado"
        }
        
        response = requests.put('http://127.0.0.1:8001/turma/10', json=updated_r, headers={"Content-Type": "application/json"})
       

        #tá faltando um get
        assert response.status_code == 200 

        updated_turma = response.json()
        assert updated_turma['descricao'] == "Desenvolvimento Mobile - Kotlin"
        assert updated_turma['professor_id'] == 1
        assert updated_turma['ativo'] == "Desativado"
        
        get_response = requests.get('http://127.0.0.1:8001/turma')
        assert get_response.status_code == 200 

    def test_delete_turma(self): 
        r = requests.post('http://127.0.0.1:8001/turma', json={
            'id': 4,
            'descricao': 'Literatura portuguesa',
            'professor_id': 3,
            'ativo': "Ativo"
        })
        if r.status_code != 200:
            self.fail(f"Erro ao criar turma História Moderna. Status Code: {r.status_code}")

        r = requests.delete('http://127.0.0.1:8001/turma/4')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Turma excluída com sucesso.', r.json()['message'])

        r_lista = requests.get('http://127.0.0.1:8001/turma')
        lista_retornada = r_lista.json()
        achei_historia = False
        for turma in lista_retornada:
            if turma['descricao'] == 'Literatura portuguesa':
                achei_historia = True

        self.assertFalse(achei_historia, "A turma Literatura portuguesa ainda está na lista de turmas.")


    def test_criar_turma(self):
        r = requests.post('http://127.0.0.1:8001/turma', json={
            'id':2,
            'descricao':'Desenvolvimento de APIs',
            'professor_id':2, 
            'ativo': "Ativo"})
            
        if r.status_code != 200:
            self.fail(f"Erro ao criar turma Desenvolvimento de APIs. Status Code: {r.status_code}")

        r = requests.post('http://127.0.0.1:8001/turma', json={
            'id':3,
            'descricao':'Matemática Aplicada',
            'professor_id':3, 
            'ativo': "Ativo"})
            
        if r.status_code != 200:
            self.fail(f"Erro ao criar turma Matemática Aplicada. Status Code: {r.status_code}")
                
        r_lista = requests.get('http://127.0.0.1:8001/turma')
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
        r = requests.get('http://127.0.0.1:8001/turma')
        if r.status_code == 404:
            self.fail("Voce nao definiu a pagina '/turma' no seu server")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))


# ALUNO

    def test_campo_aluno_nome_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': '',
            'nome': None,
            'idade': 20,
            'data_nascimento': '01/01/2000',
            'nota_primeiro_semestre': 8.0,
            'nota_segundo_semestre': 9.0,
            'media_final': 8.5,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo nome informado é obrigatório.', r.json()['error'])

    def test_campo_aluno_idade_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': '',
            'nome': 'Manuela',
            'idade': None,
            'data_nascimento': '01/01/2000',
            'nota_primeiro_semestre': 8.0,
            'nota_segundo_semestre': 9.0,
            'media_final': 8.5,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo idade informado é obrigatório.', r.json()['error'])

    def test_campo_aluno_datanasc_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': '',
            'nome': 'Angelina',
            'idade': 50,
            'data_nascimento': None,
            'nota_primeiro_semestre': 8.0,
            'nota_segundo_semestre': 9.0,
            'media_final': 8.5,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo data_nascimento informado é obrigatório.', r.json()['error'])

    def test_campo_aluno_nota_primeiro_semestre_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': '',
            'nome': 'Beatriz',
            'idade': 19,
            'data_nascimento': '03/10/2005',
            'nota_primeiro_semestre': None,
            'nota_segundo_semestre': 9.0,
            'media_final': 8.5,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo nota_primeiro_semestre informado é obrigatório.', r.json()['error'])

    def test_campo_aluno_nota_segundo_semestre_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': '',
            'nome': 'Bianca',
            'idade': 19,
            'data_nascimento': '03/10/2005',
            'nota_primeiro_semestre': 10.0,
            'nota_segundo_semestre': None,
            'media_final': 8.5,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo nota_segundo_semestre informado é obrigatório.', r.json()['error'])

    def test_campo_aluno_media_final_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': '',
            'nome': 'Beatriz',
            'idade': 19,
            'data_nascimento': '03/10/2005',
            'nota_primeiro_semestre': 8.0,
            'nota_segundo_semestre': 9.0,
            'media_final': None,
            'turma_id': 1
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo media_final informado é obrigatório.', r.json()['error'])
    
    def test_campo_aluno_turma_id_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': '',
            'nome': 'Beatriz',
            'idade': 19,
            'data_nascimento': '03/10/2005',
            'nota_primeiro_semestre': 5.0,
            'nota_segundo_semestre': 9.0,
            'media_final': 8.5,
            'turma_id': None
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo turma_id informado é obrigatório.', r.json()['error'])
    
    def test_update_aluno_successo(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={ 
            "id": 10,
            "nome": "Joao",
            "idade": 20,
            "data_nascimento": "2005-02-01",
            "nota_primeiro_semestre": 8.0,
            "nota_segundo_semestre": 9.0,
            "media_final": 8.5,
            "turma_id": 1
        })

        assert r.status_code == 200

        updated_r = {
            "id": 10,
            "nome": "Joao Silva",
            "idade": 21,
            "data_nascimento": "2004-12-01",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 9.2,
            "media_final": 8.75,
            "turma_id": 1
        }
        
        response = requests.put('http://127.0.0.1:8001/alunos/10', json=updated_r, headers={"Content-Type": "application/json"})
        assert response.status_code == 200


        updated_aluno = response.json()
        assert updated_aluno['nome'] == "Joao Silva"
        assert updated_aluno['idade'] == 21
        assert updated_aluno['media_final'] == 8.75
        
        get_response = requests.get('http://127.0.0.1:8001/alunos')
        assert get_response.status_code == 200


    def test_delete_aluno(self): 
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': 6,
            'nome': "Matheus",
            'idade': 19,
            'data_nascimento': "13/05/2005",
            'nota_primeiro_semestre': 9,
            'nota_segundo_semestre': 8,
            'media_final': 8.5,
            'turma_id': 1
        })
        if r.status_code != 200:
            self.fail(f"Erro ao criar aluno Matheus. Status Code: {r.status_code}")

        aluno_criado = r.json()
        aluno_id = aluno_criado['id']

        r = requests.delete(f'http://127.0.0.1:8001/alunos/{aluno_id}')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Aluno excluído com sucesso', r.json()['message'])

        r_lista = requests.get('http://127.0.0.1:8001/alunos')
        self.assertEqual(r_lista.status_code, 200)
        lista_retornada = r_lista.json()

        achei_matheus = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'Matheus':
                achei_matheus = True

        self.assertFalse(achei_matheus, "O aluno Matheus ainda está na lista de alunos.")

    
    def test_criar_aluno(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': 4,
            'nome': 'José',
            'idade': 19,
            'data_nascimento': "13/05/2005",
            'nota_primeiro_semestre': 9,
            'nota_segundo_semestre': 8,
            'media_final': 8.5,
            'turma_id': 1
        })
        if r.status_code != 200:
            print(r.content)
            self.fail(f"Erro ao criar aluno José. Status Code: {r.status_code}")

        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': 5,
            'nome': 'Letícia',
            'idade': 19,
            'data_nascimento': "22/02/2004",
            'nota_primeiro_semestre': 10,
            'nota_segundo_semestre': 8,
            'media_final': 9,
            'turma_id': 1
        })
        if r.status_code != 200:
            self.fail(f"Erro ao criar aluna Letícia. Status Code: {r.status_code}")
            
        r_lista = requests.get('http://127.0.0.1:8001/alunos')
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
        r = requests.get('http://127.0.0.1:8001/alunos')
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


 
