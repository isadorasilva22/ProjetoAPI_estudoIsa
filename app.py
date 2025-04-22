# É o ponto de entrada da aplicação Flask. Contém:
# Importações necessárias do Flask
# Inicialização da aplicação Flask
# Definição das rotas principais da API
# Execução da aplicação com app.run()

# É usado para acessar variáveis de ambiente do sistema operacional, como configurações de porta e host do servidor Flask
import os

# Configurações da aplicação
from config import app, db  

# Rotas organizadas (blueprints) dos controllers
from controller.routesAlunos import alunos_bp
from controller.routesProfessor import professor_bp
from controller.routesTurma import turma_bp

# Registrar os blueprints / associa cada conjunto de rotas à aplicação
app.register_blueprint(alunos_bp)
app.register_blueprint(professor_bp)
app.register_blueprint(turma_bp)

# Criação de tabelas no banco (se ainda não existirem)
with app.app_context():
    db.create_all()
    
# Inicia o servidor Flask com as configurações de host, porta e modo debug definidos no config.py.
if __name__ == '__main__':
    app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'])

