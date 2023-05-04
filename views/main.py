from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    ...

@main.route('/home', methods=['GET', 'POST', 'PUT'])
def home():
    ...

@main.route('/incomes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def incomes():
    ...

@main.route('/expenses', methods=['GET', 'POST', 'PUT', 'DELETE'])
def expenses():
    ...

@main.route('/budgets', methods=['GET', 'POST', 'PUT', 'DELETE'])
def budgets():
    ...

@main.route('/analyzes', methods=['GET'])
def analyzes():
    ...

@main.route('/profile', methods=['GET', 'PUT'])
def profile():
    ...

@main.route('/settings')
def settings():
    ...