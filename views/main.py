from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/home', methods=['GET', 'POST', 'PUT'])
@login_required
def home():
    from forms import PiggyForm
    form = PiggyForm()
    if request.method=='POST':
        from models.general import edit_budget
        return edit_budget()
    return render_template('inicio.html', user=current_user, form=form)

@main.route('/incomes', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def incomes():
    from forms import IncomeForm
    form = IncomeForm()
    if form.validate_on_submit():
        from models.general import add_income
        return add_income()
    return render_template('entradas.html', user=current_user, form=form)

@main.route('/incomes/edit', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def edit_incomes():
    from models.general import edit_income
    
    return edit_income()

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
    from forms import IncomeForm
    form = IncomeForm()
    if form.validate_on_submit():
        from models.general import add_expense
        return add_expense()
    return render_template('saidas.html', user=current_user, form=form)

@main.route('/expenses/edit', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def edit_expenses():
    from models.general import edit_expense

    return edit_expense()

@main.route('/expenses/<int:expense_id>/delete', methods=['GET'])
@login_required
def delete_expenses(expense_id):
        from models.entities import TransacaoSaida
        expense = TransacaoSaida.show_one(expense_id)

        from models.general import delete_expense
        return delete_expense(expense)

@main.route('/budgets', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def budgets():
    from forms import PiggyForm
    form = PiggyForm()
    if form.validate_on_submit():
        from models.general import add_piggy
        return add_piggy()
    return render_template('cofrinho.html', user=current_user, form=form)

@main.route('/budgets/edit', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def edit_budgets():
    from models.general import edit_budget

    return edit_budget()

@main.route('/budgets/<int:budget_id>/delete', methods=['GET'])
@login_required
def delete_budgets(budget_id):
        from models.entities import TransacaoCofrinho
        budget = TransacaoCofrinho.show_one(budget_id)

        from models.general import delete_budget
        return delete_budget(budget)

@main.route('/analyzes', methods=['GET'])
@login_required
def analyzes():
    return render_template('analises.html', user=current_user)

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    from forms import EditAccountForm

    form = EditAccountForm(obj=current_user)
    
    if form.validate_on_submit():
        from models.auth import edit_account
        return edit_account()
    
    return render_template('perfil.html', user=current_user, form=form)

@main.route('/settings')
@login_required
def settings():
    return 'Recurso ainda não implementado :('