from flask import Blueprint
from flask_login import login_required


main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    ...

@main.route('/home', methods=['GET', 'POST', 'PUT'])
@login_required
def home():
    ...

@main.route('/incomes', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def incomes():
    ...

@main.route('/expenses', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def expenses():
    ...

@main.route('/budgets', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def budgets():
    ...

@main.route('/analyzes', methods=['GET'])
@login_required
def analyzes():
    ...

@main.route('/profile', methods=['GET', 'PUT'])
@login_required
def profile():
    ...

@main.route('/settings')
@login_required
def settings():
    ...