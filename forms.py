from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    email = StringField(validatos=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    remember_me = BooleanField('Me mantenha conectado')
    submit = SubmitField('Entrar')

class SignupForm(FlaskForm):
    real_name = StringField(validatos=[InputRequired()])
    username = StringField(validatos=[InputRequired()])
    email = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    password2 = PasswordField(validators=[InputRequired()])
    submit = SubmitField('Cadastrar-se')

class RecoveryForm(FlaskForm):
    email = StringField(validators=[InputRequired()])
    submit = SubmitField('Enviar')