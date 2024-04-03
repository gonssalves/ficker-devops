from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mailing import Mail
import sqlalchemy
from views.main import main as view_main
from views.auth import auth as view_auth
from dotenv import load_dotenv
from sqlalchemy import text

import os, sentry_sdk

# Função para conectar ao banco de dados usando um socket Unix
def connect_unix_socket():
    """Inicializa um pool de conexão usando um socket Unix para uma instância do Cloud SQL do PostgreSQL."""
    db_user = os.environ["DB_USER"]  # Substitua pelo nome de usuário do seu banco de dados
    db_pass = os.environ["DB_PASS"]  # Substitua pela senha do seu banco de dados
    db_name = os.environ["DB_NAME"]  # Substitua pelo nome do seu banco de dados
    unix_socket_path = os.environ["INSTANCE_UNIX_SOCKET"]  # Substitua pelo caminho do soquete Unix da sua instância do Cloud SQL

    pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=db_user,
            password=db_pass,
            database=db_name,
            query={"unix_sock": f"{unix_socket_path}/.s.PGSQL.5432"},
        )
    )
    return pool

# Função para criar o aplicativo Flask
def create_app():
    app = Flask(__name__)

    # Carrega variáveis de ambiente do arquivo .env
    load_dotenv()

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    # Configura o SQLite
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    

    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_SENDER')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')
    app.config['MAIL_TLS'] = True
    app.config['MAIL_SSL'] = False

    # Configuração do sentry
    sentry_sdk.init(
        dsn="https://307d0e84cf2281bab01212d9862c73b1@o4506650077822976.ingest.sentry.io/4506650093813760",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )

    return app

# Cria o aplicativo Flask
app = create_app()

# Cria a instância do SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

from models.entities import *

#define a view responsável por login e ajuda a previnir o roubo da sessão do usuário
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    ''' Atualiza o objeto usuário com a ID do usuário armazenada na sessão. '''
    from models.entities import Usuario
    return Usuario.query.get(int(user_id))

#registra o blueprint (blueprints lidam com as rotas)
app.register_blueprint(view_main)
app.register_blueprint(view_auth)

@app.route('/migrate-db', methods=['POST'])
def migrate_db():
    if request.method == 'POST':
        try:
            # Aplicar migrações ao banco de dados
            with app.app_context():
                db.session.execute(text("CREATE DATABASE IF NOT EXISTS ficker_db;"))
                db.create_all()
                return 'Migrações do banco de dados aplicadas com sucesso!', 200
        except Exception as e:
            return f'Erro ao aplicar migrações do banco de dados: {str(e)}', 500
    else:
        return 'Método não suportado', 405
    
if __name__ == '__main__':
    import os
    if os.getenv('FLASK_ENV') == 'development':
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        # Executa o aplicativo Flask usando o Gunicorn para produção
        os.system('gunicorn -b 0.0.0.0:8080 app:app')
        db_pool = connect_unix_socket()