import unittest 
import requests

class TurmaTestStringMethods(unittest.TestCase): 
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

    def test_update_turma_successo(self):
        r = requests.post('http://127.0.0.1:8001/turma', json={ 
            "descricao": "Desenvolvimento Mobile",
            "professor_id": 1,
            "ativo": "Ativo"
        })

       
        assert r.status_code == 200
        turma_criado = r.json()
        turma_id = turma_criado['id']

        updated_r = {
            "id": turma_id,
            "descricao": "Desenvolvimento Mobile - Kotlin",
            "professor_id": 1,
            "ativo": "Desativado"
        }
        
        response = requests.put(f'http://127.0.0.1:8001/turma/{turma_id}', json=updated_r, headers={"Content-Type": "application/json"})
        assert response.status_code == 200 

        updated_turma = response.json()
        assert updated_turma['descricao'] == "Desenvolvimento Mobile - Kotlin"
        assert updated_turma['professor_id'] == 1
        assert updated_turma['ativo'] == "Desativado"
        
        get_response = requests.get('http://127.0.0.1:8001/turma')
        assert get_response.status_code == 200 

    def test_delete_turma(self): 
        requests.delete('http://127.0.0.1:8001/turma/4')

        r = requests.post('http://127.0.0.1:8001/turma', json={
            'id': 4,
            'descricao': 'Literatura Portuguesa',
            'professor_id': 3,
            'ativo': "Ativo"
        })
        if r.status_code != 200:
            self.fail(f"Erro ao criar turma literatura portuguesa. Status Code: {r.status_code}")

        turma_criada = r.json()
        turma_id = turma_criada['id']
        r = requests.delete(f'http://127.0.0.1:8001/turma/{turma_id}')
        self.assertEqual(r.status_code, 200)
        self.assertIn('Turma deletada com sucesso.', r.json()['message'])

        r_lista = requests.get('http://127.0.0.1:8001/turma')
        self.assertEqual(r_lista.status_code, 200)
        lista_retornada = r_lista.json()

        literatura_portuguesa = False
        for turma in lista_retornada:
            if turma['descricao'] == 'Literatura Portuguesa':
                literatura_portuguesa = True
                
        
        self.assertFalse(literatura_portuguesa, "A turma Literatura portuguesa ainda está na lista de turmas.")

    def test_retorna_lista_turma(self):
        r = requests.get('http://127.0.0.1:8001/turma')
        if r.status_code == 404:
            self.fail("Voce nao definiu a pagina '/turma' no seu server")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))


# Testes de integração
    def test_campo_turma_descricao_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "descricao": None,
            "professor_id": 1,
            "ativo": "Status"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo descricao informado é obrigatório.', r.json()['error'])

    def test_campo_turma_professor_id_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "descricao": "testes rapidos",
            "professor_id": None,
            "ativo": "Status"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo professor_id informado é obrigatório.', r.json()['error'])

    def test_campo_ativo_descricao_null(self):
        r = requests.post('http://127.0.0.1:8001/alunos', json={
            "descricao": "Probabilidades",
            "professor_id": 1,
            "ativo": None
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo ativo informado é obrigatório.', r.json()['error'])

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TurmaTestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()