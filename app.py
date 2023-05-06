from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mailing import Mail
from views.main import main as view_main
from views.auth import auth as view_auth
import os

#caminho relativo
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

from secret import SECRET_KEY, EMAIL_SENDER, EMAIL_PASSWORD

app.config['SECRET_KEY'] = SECRET_KEY
#configura o SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = EMAIL_SENDER
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
app.config['MAIL_TLS'] = True
app.config['MAIL_SSL'] = False

#cria extensões
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

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

if __name__ == '__main__':
    app.run(debug=True)