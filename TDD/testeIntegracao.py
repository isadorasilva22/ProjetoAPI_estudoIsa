# import unittest
# import requests
# import sqlite3
# import os

# class TestIntegracaoComBanco(unittest.TestCase):
#     base_url = "http://127.0.0.1:8001"
#     db_path = os.path.join("instance", "app.db")  

#     def test_criacao_aluno_e_verificacao_no_banco(self):
#         aluno = {
#             "nome": "Maria",
#             "idade": 25,
#             "data_nascimento": "01/01/2000",
#             "nota_primeiro_semestre": 8.5,
#             "nota_segundo_semestre": 9,
#             "media_final": 8.75
#         }

#         r = requests.post(f"{self.base_url}/alunos", json=aluno)
#         self.assertEqual(f"Erro ao criar aluno: {r.status_code}")
#         aluno_api = r.json()
#         aluno_id = aluno_api["id"]

#         # 2. Verifica diretamente no banco
#         verificacao = sqlite3.connect(self.db_path)
#         cursor = verificacao.cursor()
#         cursor.execute("SELECT nome, idade FROM aluno WHERE id = ?", (aluno_id,))
#         row = cursor.fetchone()
#         verificacao.close()

#         # 3. Valida o que foi salvo
#         self.assertIsNotNone(row, "Aluno não encontrado no banco de dados.")
#         self.assertEqual(row[0], aluno["nome"])
#         self.assertEqual(row[1], aluno["idade"])

# if __name__ == "__main__":
#     unittest.main()