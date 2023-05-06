from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Regexp

class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(message='Campo em branco')])
    password = PasswordField('Senha', validators=[InputRequired(), Length(8, message='Senha precisa ter ao menos 8 caracteres')])
    remember_me = BooleanField('Me mantenha conectado')
    submit = SubmitField('Entrar')

class SignupForm(FlaskForm):
    real_name = StringField('Nome Real', validators=[InputRequired(message='Campo em branco')])
    username = StringField(
        validators=[
            InputRequired(), 
            Length(3, message="Nome de usuário precisa ter ao menos 3 caracteres"), 
            Regexp( 
                "^[A-Za-z][A-Za-z0-9_.]*$", 
                0, 
                "Nomes de usuário só podem conter letras, " "números, pontos ou underline"
            )
        ]
    )
    email = StringField(validators=[InputRequired(message='Campo em branco')])
    password = PasswordField('Senha', validators=[InputRequired(), Length(8, message='Senha precisa ter ao menos 8 caracteres')])
    password2 = PasswordField('Repita a senha', validators=[InputRequired(message='Campo em branco')])
    submit = SubmitField('Cadastrar-se')

class RecoveryForm(FlaskForm):
    email = StringField(validators=[InputRequired(message='Campo em branco')])
    submit = SubmitField('Enviar')