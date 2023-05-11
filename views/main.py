from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/home', methods=['GET', 'POST', 'PUT'])
@login_required
def home():
    return render_template('inicio.html', user=current_user)
@main.route('/incomes', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def incomes():
    return render_template('entradas.html', user=current_user)

@main.route('/expenses', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def expenses():
    return render_template('saidas.html', user=current_user)

@main.route('/budgets', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def budgets():
    return render_template('cofrinho.html', user=current_user)

@main.route('/analyzes', methods=['GET'])
@login_required
def analyzes():
    return render_template('analises.html', user=current_user)

@main.route('/profile', methods=['GET', 'PUT'])
@login_required
def profile():
    return render_template('perfil.html', user=current_user)

@main.route('/settings')
@login_required
def settings():
    return 'Recurso ainda não implementado :('