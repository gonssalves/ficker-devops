from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/test', methods=['GET'])
def test():
    return 'Hello, world!'

@main.route('/', methods=['GET'])
def index():
    if '_user_id' in session:
         return redirect(url_for('main.home'))
    return render_template('index.html')

@main.route('/home', methods=['GET', 'POST', 'PUT'])
@login_required
def home():
    from forms import PiggyForm
    form = PiggyForm()
    if request.method=='POST':
        from models.general import edit_piggy
        return edit_piggy()
    return render_template('inicio.html', user=current_user, form=form)

@main.route('/home/edit-budget', methods=['POST'])
@login_required
def home_edit_budget():
    from models.general import edit_budget
    
    return edit_budget()

@main.route('/incomes', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def incomes():
    from forms import TransactionForm
    form = TransactionForm()
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

        from models.general import delete_transaction
        return delete_transaction(income, 'entrada', 'incomes')

@main.route('/expenses', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def expenses():
    from forms import TransactionForm
    form = TransactionForm()
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

        from models.general import delete_transaction
        return delete_transaction(expense, 'saída', 'expenses')

@main.route('/piggy-bank', methods=['GET', 'POST'])
@login_required
def piggy():
    from forms import PiggyForm
    form = PiggyForm()
    if form.validate_on_submit():
        from models.general import add_piggy
        return add_piggy()
    return render_template('cofrinho.html', user=current_user, form=form)

@main.route('/piggy-bank/edit', methods=['GET', 'POST'])
@login_required
def edit_piggy():
    from models.general import edit_piggy

    return edit_piggy()

@main.route('/piggy-bank/<int:piggy_id>/delete', methods=['GET'])
@login_required
def delete_piggy(piggy_id):
        from models.entities import TransacaoCofrinho
        piggy = TransacaoCofrinho.show_one(piggy_id)

        from models.general import delete_transaction
        return delete_transaction(piggy, 'transação do cofrinho', 'piggy')

@main.route('/analyzes', methods=['GET'])
@login_required
def analyzes():
    from models.entities import Usuario

    total = Usuario.total(current_user)

    most_recents = Usuario.most_recents(current_user)

    lista =  Usuario.monthly(current_user)
    print(lista)
    if lista == 'no transactions':
         return render_template('analises_vazio.html', user=current_user)
    
    return render_template('analises.html', user=current_user, incomes=total['entrada'], expenses=total['saida'], budgets=total['cofrinho'], total=total['total'], most_recents=most_recents, lista=lista)

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