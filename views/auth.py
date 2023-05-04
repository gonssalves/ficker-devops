from flask import Blueprint, redirect, url_for, request, render_template
from flask_login import login_required, logout_user

auth = Blueprint('auth', __name__)

#views responsáveis pela autorização

@auth.route('/login', methods=['GET', 'POST'])
def login():
    from forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        from models.auth import auth_login
        return auth_login()
    form.process(request.args)
    return render_template('', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    from forms import SignupForm
    form = SignupForm()
    if form.validate_on_submit():
        from models.auth import auth_signup
        return auth_signup()
    form.process(request.args)
    return render_template('', form=form)

@auth.route('/recovery-password', methods=['GET', 'POST'])
def recovery_password():
    from forms import RecoveryForm
    form = RecoveryForm()
    if form.validate_on_submit():
        from models.auth import auth_recovery
        return auth_recovery()
    form.process(request.args)
    return render_template('', form=form)

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect((url_for('main.index')))