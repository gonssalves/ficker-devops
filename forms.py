from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class FormEntrar(FlaskForm):
    email = StringField(validatos=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField('Entrar')

class FormCadastrar(FlaskForm):
    name = StringField(validatos=[InputRequired()])
    email = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    password2 = PasswordField(validators=[InputRequired()])
    submit = SubmitField('Cadastrar-se')