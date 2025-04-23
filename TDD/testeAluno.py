import unittest 
import requests

class AlunoTestStringMethods(unittest.TestCase):

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

    def test_update_aluno_sucesso(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={ 
            "nome": "Joao",
            "idade": 20,
            "data_nascimento": "01/02/2005",
            "nota_primeiro_semestre": 8.0,
            "nota_segundo_semestre": 9.0,
            "media_final": 8.5,
            "turma_id": 1
        })
        
        assert r.status_code == 200

        aluno_criado = r.json()
        aluno_id = aluno_criado['id']

        updated_r = {
            "id": aluno_id,
            "nome": "Joao Silva",
            "idade": 0,
            "data_nascimento": "01/12/2004",
            "nota_primeiro_semestre": 8.5,
            "nota_segundo_semestre": 9.2,
            "media_final": 8.75,
            "turma_id": 1
        }

        
        response = requests.put(f'http://127.0.0.1:8001/alunos/{aluno_id}', json=updated_r, headers={"Content-Type": "application/json"})
        assert response.status_code == 200

        updated_aluno = response.json()
        assert updated_aluno['nome'] == "Joao Silva"
        assert updated_aluno['media_final'] == 8.75
        
        get_response = requests.get('http://127.0.0.1:8001/alunos')
       
        assert get_response.status_code == 200


    def test_delete_aluno(self): 
        requests.delete('http://127.0.0.1:8001/alunos/6')
    
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
        self.assertIn('Aluno deletado com sucesso', r.json()['message'])

        r_lista = requests.get('http://127.0.0.1:8001/alunos')
        self.assertEqual(r_lista.status_code, 200)
        lista_retornada = r_lista.json()

        achei_matheus = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'Matheus':
                achei_matheus = True

        self.assertFalse(achei_matheus, "O aluno Matheus ainda está na lista de alunos.")
    
    def test_retorna_lista_alunos(self):
        r = requests.get('http://127.0.0.1:8001/alunos')
        if r.status_code == 404:
            return self.fail("Voce nao definiu a pagina '/alunos' no seu server")
            
        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))

#Testes de integração
    def test_campo_aluno_nome_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            'id': '',
            'nome': None,
            'idade': 0,
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
    
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(AlunoTestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()
