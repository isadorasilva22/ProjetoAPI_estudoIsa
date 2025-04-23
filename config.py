# Contém:
# Configurações do banco de dados
# Chaves secretas 
# Outras variáveis de ambiente necessárias para o funcionamento da aplicação.​

# É usado para acessar variáveis de ambiente do sistema operacional, como configurações de porta e host do servidor Flask
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criação do app Flask
app = Flask(__name__)

# Configurações do servidor
app.config['HOST'] = '0.0.0.0'  # define o IP onde a aplicação escuta (0.0.0.0 = acessível externamente)
app.config['PORT']= 8001        
app.config['DEBUG'] = True      # habilita o modo debug 

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"  # usa SQLcom URL apropriada
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False        # evita alertas desnecessários
# mysql://<username>:<password>@<host>/<db_name> - usar se alterar para o sql

# Criação do objeto db: conecta o SQLAlchemy com a aplicação Flask.
db = SQLAlchemy(app)

# Os arquivos de modelo usam a variável db que foi criada. Isso conecta os modelos diretamente ao banco de dados configurado aqui (no caso, um banco SQLite chamado app.db). 
# Cada modelo define classes que herdam de db.Model, permitindo criar tabelas no banco com campos como id, nome, etc.
