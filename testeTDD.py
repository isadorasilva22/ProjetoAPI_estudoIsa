import requests
import unittest

class TestStringMethods(unittest.TestCase):

#Testar retorno
    def test_retorna_lista_alunos(self):
        r = requests.get('http://127.0.0.1:5000/alunos')
        if r.status_code == 404:
            return self.fail("Voce nao definiu a pagina '/alunos' no seu server")
            
        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))

    def test_retorna_lista_professores(self):
        r = requests.get('http://127.0.0.1:5000/professor')
        if r.status_code == 404:
            self.fail("Voce nao definiu a pagina '/professor' no seu server")

        try:
            obj_retornado = r.json()
        except:
            self.fail("Era esperado um objeto JSON")
        
        self.assertEqual(type(obj_retornado),type([]))    

    def test_retorna_lista_turma(self):
        r = requests.get('http://127.0.0.1:5000/turma')
        if r.status_code == 404:
            self.fail("Voce nao definiu a pagina '/turma' no seu server")

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
 

# Testar criação
# Testar campos nulos
# Testar Atualizar
# Testar Apagar
