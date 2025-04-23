import unittest 
import requests

class ProfessorTestStringMethods(unittest.TestCase):   
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
    
    def test_update_professor_successo(self):
        r = requests.post('http://127.0.0.1:8001/professor', json={ 
            "nome": "Romário",
            "idade": 30,
            "materia": "Desenvolvimento Web",
            "observacoes": "Nenhuma"
        })
        
        assert r.status_code == 200
        professor_criado = r.json()
        professor_id = professor_criado['id']
        

        updated_r = {
            "id": professor_id,
            "nome": "Romário Silva",
            "idade": 30,
            "materia": "Desenvolvimento Web",
            "observacoes": "Nenhuma"
        }
        
        response = requests.put(f'http://127.0.0.1:8001/professor/{professor_id}', json=updated_r, headers={"Content-Type": "application/json"})
        assert response.status_code == 200 

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

    
    def test_retorna_lista_professores(self):
        r = requests.get('http://127.0.0.1:8001/professor')
        if r.status_code == 404:
            self.fail("Voce nao definiu a pagina '/professor' no seu server")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))   


#Arrumar para integração
    def test_campo_professor_nome_null(self):
        r = requests.post('http://127.0.0.1:8001/professor', json={
            "nome": None,
            "idade": 0,
            "materia": "Nome da materia",
            "observacoes": "Observacao sobre o professor"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo nome informado é obrigatório.', r.json()['error'])

    def test_campo_professor_idade_null(self):
        r = requests.post('http://127.0.0.1:8001/professor', json={
            "nome": "Priscilla",
            "idade": None,
            "materia": "Nome da materia",
            "observacoes": "Observacao sobre o professor"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo idade informado é obrigatório.', r.json()['error'])

    def test_campo_professor_materia_null(self):
        r = requests.post('http://127.0.0.1:8001/professor', json={
            "nome": "Marcos",
            "idade": 0,
            "materia": None,
            "observacoes": "Observacao sobre o professor"
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo materia informado é obrigatório.', r.json()['error'])

    def test_campo_professor_obervacoes_null(self):
        r = requests.post('http://127.0.0.1:8001/professor', json={
            "nome": "Lima",
            "idade": 0,
            "materia": "Fisica",
            "observacoes": None
        })
        self.assertEqual(r.status_code, 400)
        self.assertIn('O campo observacoes informado é obrigatório.', r.json()['error'])

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ProfessorTestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()