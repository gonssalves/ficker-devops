from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class FormEntrar(FlaskForm):
    email = StringField(validatos=[InputRequired()])
    senha = PasswordField(validators=[InputRequired()])
    enviar = SubmitField('Entrar')

class FormCadastrar(FlaskForm):
    nome = StringField(validatos=[InputRequired()])
    email = StringField(validators=[InputRequired()])
    senha = PasswordField(validators=[InputRequired()])
    senha2 = PasswordField(validators=[InputRequired()])
    enviar = SubmitField('Cadastrar-se')