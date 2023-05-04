from models.entities import Usuario
from flask import request, redirect, url_for, flash
from flask_login import login_user
from app import db, bcrypt
from email_validator import validate_email, EmailNotValidError

def auth_login():
    '''' Verifica se o usuário existe no banco de dados e se a senha está correta. '''
    username = request.form.get('username')
    password = request.form.get('password')
    remember_me = request.form.get('remember_me')

    #verifica se o usuário existe no banco de dados
    user = Usuario.query.filter_by(nom_usuario=username).first()#retorna none se não existir tal usuário

    #deixa somente o nome usuário na requisicão
    req = request.form.copy()
    req.pop('password')
    req.pop('csrf_token')
    req.pop('submit')

    if user:
        if user.verify_password(password):
            login_user(user, remember_me)#uma vez que o usuário é autenticado, ele é logado com essa função | remember-me mantém o usuário logado apos o navegador ser fechado
            return redirect(request.args.get('next') or url_for('main.home'))
    flash('Nome de usuário ou senha inválido')
    return redirect(url_for('auth.login', **req))#**req é usado para enviar a requisição de volta para o formulário, assim o usuário não precisa digitar tudo de novo
    #TODO: pesquisar sobre os parâmetros do url_for

def auth_recovery():
    ...

def auth_signup():
    ''' Valida as informações enviadas e registra o usuário. '''
    real_name = request.form.get('real_name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    req = request.form.copy()
    req.pop('password')
    req.pop('password2')
    req.pop('csrf_token')
    req.pop('submit')

    #usando pacote emal_validator
    try:
        email_info = validate_email(email, check_deliverability=True)#check_deliverability faz queries DNS para verificar o domínio - a parte depois do @ - pode receber o email
        email = email_info.normalized
    except EmailNotValidError as e:
        flash(str(e))
        return redirect(url_for('auth.signup', **req))
    
    if password != password2:
        flash('As senhas precisam ser iguais')
        return redirect(url_for('auth.signup', **req))
    
    verify_email = Usuario.query.filter_by(eml_usuario=email)
    
    if verify_email:
        flash('Email já está cadastrado')
        return redirect(url_for('auth.signup', **req))
    
    verify_username = Usuario.query.filter_by(nom_usuario=username)

    if verify_username:
        flash('Usuário já está cadastrado')

    password = bcrypt.generate_password_hash(password).decode('utf-8')#gera hash da senha

    new_user = Usuario(nom_real=real_name, nom_usuario=username, sen_usuario=password, eml_usuario=email)
    
    #TODO: procurar por exceções sqlalchemy
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        flash('Não foi possível cadastrar-se, por favor tente mais tarde')
        return redirect(url_for('auth.signup', **req))
    
    flash('Você se cadastrou, já pode entrar em sua conta')
    return redirect(url_for('auth.login'))