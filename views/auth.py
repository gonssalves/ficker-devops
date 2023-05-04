from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user

auth = Blueprint('auth', __name__)

#views responsáveis pela autorização

@auth.route('/login', methods=['GET', 'POST'])
def entrar():
    ...

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    ...

@auth.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    ...

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect((url_for('main.index')))