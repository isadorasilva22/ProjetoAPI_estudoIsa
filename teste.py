import os
from config import db, app
from sqlalchemy import inspect

with app.app_context():
    inspector = inspect(db.engine)

    # Listar todas as tabelas
    tabelas = inspector.get_table_names()
    print("Tabelas:", tabelas)

    # Ver colunas de uma tabela específica
    colunas = inspector.get_columns('turma')
    for coluna in colunas:
        print(f"Coluna: {coluna['name']}, Tipo: {coluna['type']}")


# Verificar se o arquivo do banco foi criado
# print("Banco de dados criado?", os.path.exists("app.db"))
# verificação das rotas
# Criar uma função decodificação jwt - validação nas rotas - JWT
# 1° Arrumar os testes
# 2° JTW
# 3° Docker (configuração)
# 4° Deploy 
# --------------------
# - Passar para o MYSQL (Baixar e configurar)
# - Mexer com o Docker
# - Deploy