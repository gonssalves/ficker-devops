from flask import Blueprint, render_template, request
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
    from forms import IncomeForm
    form = IncomeForm()
    if form.validate_on_submit():
        from models.general import add_income
        return add_income()
    form.process(request.args)
    return render_template('entradas.html', user=current_user, form=form)

@main.route('/incomes/<int:income_id>/delete', methods=['GET'])
@login_required
def delete_incomes(income_id):
        from models.entities import TransacaoEntrada

        income = TransacaoEntrada.show_one(income_id)

        from models.general import delete_income
        return delete_income(income)

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