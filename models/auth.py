from models.entities import Usuario
from flask import request, redirect, url_for, flash
from flask_login import login_user, current_user
from app import db, bcrypt
from email_validator import validate_email, EmailNotValidError
import re
from email.message import EmailMessage
import smtplib
import ssl

def auth_login():
    '''' Verifica se o usuário existe no banco de dados e se a senha está correta. '''
    email = request.form.get('email')
    password = request.form.get('password')
    remember_me = (True if request.form.get('remember_me') else False)

    #verifica se o usuário existe no banco de dados
    user = Usuario.query.filter_by(eml_usuario=email).first()#retorna none se não existir tal usuário

    #deixa somente o nome usuário na requisicão
    req = request.form.copy()
    req.pop('password')
    req.pop('csrf_token')
    req.pop('submit')

    if not user:
        flash('Nome de usuário')
        return redirect(url_for('auth.login', **req))#**req é usado para enviar a requisição de volta para o formulário, assim o usuário não precisa digitar tudo de novo
    
    if not user.verify_password(password) or password == user.sen_usuario:
        flash('Senha inválida')
        return redirect(url_for('auth.login', **req))
        
    login_user(user, remember=remember_me)#uma vez que o usuário é autenticado, ele é logado com essa função | remember-me mantém o usuário logado apos o navegador ser fechado
    return redirect(request.args.get('next') or url_for('main.home'))
    
    #TODO: pesquisar sobre os parâmetros do url_for

def auth_recovery():
    email = request.form.get('email')

    req = request.form.copy()
    req.pop('csrf_token')
    req.pop('submit')

    try:
        emailinfo = validate_email(email, check_deliverability=True)#check_deliverability DNS queries are made to check that the domain name in the email address (the part after the @-sign) can receive mail
        email = emailinfo.normalized#
    except EmailNotValidError as e:
        flash(str(e))
        return redirect(url_for('auth.recovery_password', **req))
    
    user = Usuario.query.filter_by(eml_usuario=email).first()

    if user:
        password = user.sen_usuario
        #Define email sender and receiver
        from secret import EMAIL_SENDER, EMAIL_PASSWORD
        email_sender = EMAIL_SENDER
        email_password = EMAIL_PASSWORD
        email_receiver = email

        #Set the subject and body of the email
        subject = 'Recuperar Senha!'
        body = f'Use essa senha para logar em sua conta: {password}'

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        
        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    flash('Se esse email estiver registrado, você receberá um email. Verifique sua caixa de spam.')
    return redirect(url_for('auth.recovery_password'))

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
    
    if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$', password):
        flash('A senha precisa conter ao menos uma letra, um número e um caractere especial')
        return redirect(url_for('auth.signup', **req))
    
    verify_email = Usuario.query.filter_by(eml_usuario=email).first()
    
    if verify_email:
        flash('Email já está cadastrado')
        return redirect(url_for('auth.signup', **req))
    
    verify_username = Usuario.query.filter_by(nom_usuario=username).first()

    if verify_username:
        flash('Usuário já está cadastrado')
        return redirect(url_for('auth.signup', **req))


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

def edit_account():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    verify_email = Usuario.query.filter(Usuario.id != current_user.id, Usuario.eml_usuario == email).first()

    if verify_email:
        flash('Email já cadastrado')
        return redirect(url_for('main.profile'))
    
    user = Usuario.query.get(int(current_user.id))

    if password:
        if password != password2:
            flash('As senhas precisam ser iguais')
            return redirect(url_for('main.profile'))
        
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$', password):
            flash('A senha precisa conter ao menos uma letra, um número e um caractere especial')
            return redirect(url_for('main.profile'))
        
        user.sen_usuario =  bcrypt.generate_password_hash(password).decode('utf-8')
    
    user.nom_real = name
    user.eml_usuario = email
   
    db.session.add(user)
    db.session.commit()

    flash('Dados atualizados')
    return redirect(url_for('main.profile'))    