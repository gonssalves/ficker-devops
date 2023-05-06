from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/home', methods=['GET', 'POST', 'PUT'])
@login_required
def home():
    return 'Recurso ainda não implementado :('

@main.route('/incomes', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def incomes():
    user = current_user
    return render_template('entradas.html', user=user)

@main.route('/expenses', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def expenses():
    return 'Recurso ainda não implementado :('

@main.route('/budgets', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def budgets():
    return 'Recurso ainda não implementado :('

@main.route('/analyzes', methods=['GET'])
@login_required
def analyzes():
    return 'Recurso ainda não implementado :('

@main.route('/profile', methods=['GET', 'PUT'])
@login_required
def profile():
    return 'Recurso ainda não implementado :('

@main.route('/settings')
@login_required
def settings():
    return 'Recurso ainda não implementado :('