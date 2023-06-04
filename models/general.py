from models.entities import Usuario, TransacaoEntrada, TransacaoSaida, Categoria, Objetivo, TransacaoCofrinho, Orcamento
from flask import request, redirect, url_for, flash
from flask_login import current_user
from app import db
from sqlalchemy import exc
from datetime import datetime

def add_income():
    income_description = request.form.get('description')
    date = request.form.get('date')
    value = request.form.get('value')
    selected_option = request.form.get('selected_option')
    category_description = (request.form.get('new_category') if request.form.get('new_category') else 'Sem Categoria')
    
    date = datetime. strptime(date, '%Y-%m-%d')

    user = Usuario.query.get(int(current_user.id))
   
    if selected_option == 'nova':

        query_category = Categoria.query.filter_by(dsc_categoria=category_description, usuario=user).first()

        if query_category:
            new_category = query_category    
        else:
            new_category = Categoria(dsc_categoria=category_description, usuario=user)
      
        new_income = TransacaoEntrada(dsc_entrada=income_description, dat_entrada=date, val_entrada=value, usuario=user, categoria=new_category)

        try:
            db.session.add_all([new_category, new_income])
            db.session.commit()
        except:
            flash('Não foi possível cadastrar sua entrada, por favor tente mais tarde')
            return redirect(url_for('main.incomes'))
    else:
        category = Categoria.query.filter_by(dsc_categoria=selected_option).first()
        new_income = TransacaoEntrada(dsc_entrada=income_description, dat_entrada=date, val_entrada=value, usuario=user, categoria=category)

        try:
            db.session.add(new_income)
            db.session.commit()
        except:
            flash('Não foi possível cadastrar sua entrada, por favor tente mais tarde')
            return redirect(url_for('main.incomes'))
        
    flash('Entrada cadastrada com sucesso')
    return redirect(url_for('main.incomes'))

def delete_income(old_income):
    try:
        db.session.delete(old_income)
        db.session.commit()
    except:
        flash('Não foi possível excluir a entrada, por favor tente mais tarde')
        return redirect(url_for('main.incomes'))
    
    flash('Entrada excluída')
    return redirect(url_for('main.incomes'))

def edit_income():
    income_description = request.form.get('description')
    date = request.form.get('date')
    value = request.form.get('value')
    idd = request.form.get('idd')
    selected_option = request.form.get('selected_option')
    
    date = datetime.strptime(date, '%Y-%m-%d')
    date1 = str(date)
    date1 = date1[:10]

    
    user = Usuario.query.get(int(current_user.id))

    edit_income = TransacaoEntrada.query.get(int(idd))
    
    x = ''
    x += ('true' if edit_income.dsc_entrada == income_description else 'false')
    x += ('true' if edit_income.val_entrada == float(value) else 'false')    
    x += ('true' if str(edit_income.dat_entrada) == date1 else 'false')
    x += ('true' if edit_income.get_categoria_nome() == str(selected_option) else 'false')
 
    if not 'false' in x:
        flash('Nenhum campo foi alterado')
        return redirect(url_for('main.incomes'))
        
    if selected_option == 'nova':
        category_description = request.form.get('new_category')
        query_category = Categoria.query.filter_by(dsc_categoria=category_description, usuario=user).first()
        
        if query_category:
            new_category = query_category
            print('if')    
        else:
            new_category = Categoria(dsc_categoria='Sem Categoria', usuario=user)
            print('else')    

        edit_income.dsc_entrada = income_description 
        edit_income.dat_entrada = date 
        edit_income.val_entrada = value 
        edit_income.categoria = new_category
        
        try:
            db.session.add(edit_income)
            db.session.commit()
        except:
            flash('Não foi possível alterar a entrada, por favor tente mais tarde')
            return redirect(url_for('main.incomes'))
    else:
        category = Categoria.query.filter_by(dsc_categoria=selected_option).first()

        edit_income.dsc_entrada = income_description 
        edit_income.dat_entrada = date 
        edit_income.val_entrada = value 
        edit_income.categoria = category
        
        try:
            db.session.add(edit_income)
            db.session.commit()
        except:
            flash('Não foi possível alterar a entrada, por favor tente mais tarde')
            return redirect(url_for('main.incomes'))
    
    flash('Entrada alterada')
    return redirect(url_for('main.incomes'))


def add_expense():
    expense_description = request.form.get('description')
    date = request.form.get('date')
    value = request.form.get('value')
    
    date = datetime. strptime(date,  '%Y-%m-%d')

    user = Usuario.query.get(int(current_user.id))

    new_expense = TransacaoSaida(dsc_saida=expense_description, dat_saida=date, val_saida=value, usuario=user)

    try:
        db.session.add(new_expense)
        db.session.commit()
    except:
        flash('Não foi possível cadastrar sua saída, por favor tente mais tarde')
        return redirect(url_for('main.incomes'))
        
    flash('Saída cadastrada com sucesso')
    return redirect(url_for('main.expenses'))

def delete_expense(old_expense):
    try:
        db.session.delete(old_expense)
        db.session.commit()
    except:
        flash('Não foi possível excluir a saída, por favor tente mais tarde')
        return redirect(url_for('main.expenses'))
    
    flash('Saída excluída')
    return redirect(url_for('main.expenses'))

def edit_expense():
    expense_description = request.form.get('description')
    date = request.form.get('date')
    value = request.form.get('value')
    idd = request.form.get('idd')
    
    date = datetime.strptime(date, '%Y-%m-%d')
    date1 = str(date)
    date1 = date1[:10]
    
    edit_expense = TransacaoSaida.query.get(int(idd))
    
    x = ''
    x += ('true' if edit_expense.dsc_saida == expense_description else 'false')
    x += ('true' if edit_expense.val_saida == float(value) else 'false')    
    x += ('true' if str(edit_expense.dat_saida) == date1 else 'false')

    print(x)

    if not 'false' in x:
        flash('Nenhum campo foi alterado')
        return redirect(url_for('main.expenses'))
    
    edit_expense.dsc_saida = expense_description 
    edit_expense.dat_saida = date 
    edit_expense.val_saida = value 

    try:
        db.session.add(edit_expense)
        db.session.commit()
    except:
        flash('Não foi possível alterar a saida, por favor tente mais tarde')
        return redirect(url_for('main.expenses'))
        
    flash('Saída alterada')
    return redirect(url_for('main.expenses'))

def add_piggy():
    description = request.form.get('description')
    color = request.form.get('color')
    action = request.form.get('action')
    date = request.form.get('date')
    value = request.form.get('value')

    user = Usuario.query.get(int(current_user.id))

    date = datetime.strptime(date, '%Y-%m-%d')
    date1 = str(date)
    date1 = date1[:10]

    if description:
        search_objective = Objetivo.query.filter_by(nom_objetivo=description).first()

        if search_objective:
            new_piggy = TransacaoCofrinho(tip_transacao=action, dat_transacao=date, val_cofrinho=value, usuario=user, objetivo=search_objective)
            db.session.add(new_piggy)
        else:
            new_objective = Objetivo(nom_objetivo=description, cor_objetivo=color, usuario=user)
            new_piggy = TransacaoCofrinho(tip_transacao=action, dat_transacao=date, val_cofrinho=value, usuario=user, objetivo=new_objective)
            db.session.add_all([new_objective, new_piggy])

        try:
            db.session.commit()
        except:
            flash('Não foi possível concluir a transação, por favor tente mais tarde')
            return redirect(url_for('main.piggy'))
        
        flash('Transação adicionada')
        return redirect(url_for('main.piggy'))


    selected_option = request.form.get('selected_option')

    if not selected_option:
        flash('Nenhum objetivo foi selecionado')
        return redirect(url_for('main.piggy'))
    
    objective = Objetivo.query.filter_by(nom_objetivo=selected_option).first()
    
    new_piggy = TransacaoCofrinho(tip_transacao=action, dat_transacao=date, val_cofrinho=value, usuario=user, objetivo=objective)

    try:
        db.session.add(new_piggy)
        db.session.commit()
    except:
        flash('Não foi possível concluir a transação, por favor tente mais tarde')
        return redirect(url_for('main.piggy'))
    
    flash('Transação adicionada')
    return redirect(url_for('main.piggy'))

def edit_piggy():
    #return str(request.form)
    selected_option = request.form.get('selected_option')
    description = request.form.get('description')
    color = request.form.get('color')
    action = request.form.get('action')
    date = request.form.get('date')
    value = request.form.get('value')
    idd = request.form.get('idd')
    
    date = datetime.strptime(date, '%Y-%m-%d')
    date1 = str(date)
    date1 = date1[:10]
    
    user = Usuario.query.get(int(current_user.id))

    edit_budget = TransacaoCofrinho.query.get(int(idd))
    
    x = ''
    x += ('true' if edit_budget.tip_transacao == action else 'false')
    x += ('true' if edit_budget.val_cofrinho == float(value) else 'false')    
    x += ('true' if str(edit_budget.dat_transacao) == date1 else 'false')

    if description == '':

        objective = Objetivo.query.filter_by(nom_objetivo=selected_option).first()

        x += ('true' if str(edit_budget.cod_objetivo) == str(objective.id) else 'false')
        
        if not 'false' in x:
            flash('Nenhum campo foi alterado')
            return redirect(url_for('main.piggy'))
        
        edit_budget.tip_transacao = action
        edit_budget.dat_transacao = date 
        edit_budget.val_cofrinho = value
        edit_budget.cod_objetivo = objective.id
        
        try:
            db.session.add(edit_budget)
            db.session.commit()
        except:
            flash('Não foi possível alterar a transação, por favor tente mais tarde')
            return redirect(url_for('main.piggy'))
            
        flash('Transação alterada')
        return redirect(url_for('main.piggy'))
    
    else:
        search_objective = Objetivo.query.filter_by(nom_objetivo=description).first()

        if search_objective:
            edit_budget.cod_objetivo = search_objective.id
            db.session.add(edit_budget)
        else:
            new_objective = Objetivo(nom_objetivo=description, cor_objetivo=color, usuario=user)
            edit_budget.objetivo = new_objective
            db.session.add_all([new_objective, edit_budget])

        try:
            db.session.commit()
        except:
            flash('Não foi possível alterar a transação, por favor tente mais tarde')
            return redirect(url_for('main.piggy'))
            
        flash('Transação alterada')
        return redirect(url_for('main.piggy'))

def delete_piggy(old_piggy):
    try:
        db.session.delete(old_piggy)
        db.session.commit()
    except:
        flash('Não foi possível excluir a transação, por favor tente mais tarde')
        return redirect(url_for('main.piggy'))
    
    flash('Transação excluída')
    return redirect(url_for('main.piggy'))


def edit_budget():
    #return str(request.form)
    value = request.form.get('value')

    user = Usuario.query.get(int(current_user.id))

    for orcamento in user.orcamentos_u:
        if orcamento.mes_orcamento == 'Junho':
            orcamento.val_orcamento_previsto = value

    try:
        db.session.commit()
    except:
        flash('Não foi possível editar o orçamento, por favor tente mais tarde')
        return redirect(url_for('main.home'))
    
    return redirect(url_for('main.home'))