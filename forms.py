from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, FloatField
from wtforms.validators import InputRequired, Length, Regexp

class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired()])
    password = PasswordField('Senha', validators=[InputRequired()])
    remember_me = BooleanField('Me mantenha conectado')
    submit = SubmitField('Entrar')

class EditAccountForm(FlaskForm):
    name = StringField(validators=[InputRequired()])
    email = StringField(validators=[InputRequired()])
    password = PasswordField()
    password2 = PasswordField()
    submit = SubmitField('Salvar')

class SignupForm(FlaskForm):
    real_name = StringField('Nome Real', validators=[InputRequired()])
    username = StringField(
        validators=[
            InputRequired(), 
            Length(3), 
            Regexp( 
                "^[A-Za-z][A-Za-z0-9_.]*$", 
                0, 
                "Nomes de usuário só podem conter letras, " "números, pontos ou underline"
            )
        ]
    )
    email = StringField(validators=[InputRequired()])
    password = PasswordField('Senha', validators=[InputRequired(), Length(8)])
    password2 = PasswordField('Repita a senha', validators=[InputRequired()])
    submit = SubmitField('Cadastrar-se')

class RecoveryForm(FlaskForm):
    email = StringField(validators=[InputRequired()])
    submit = SubmitField('Enviar')

class TransactionForm(FlaskForm):
    description = StringField('Descrição', validators=[InputRequired()])
    date = DateField('Data', validators=[InputRequired()])
    new_category = StringField('Categoria')
    value = FloatField('Valor', validators=[InputRequired()])
    submit = SubmitField('Adicionar')
    idd = StringField()

class PiggyForm(FlaskForm):
    description = StringField('Descrição')
    color = StringField('Cor')
    action = StringField('Ação')
    date = DateField('Data', validators=[InputRequired()])
    value = FloatField('Valor', validators=[InputRequired()])
    submit = SubmitField('Adicionar')
    idd = StringField()



