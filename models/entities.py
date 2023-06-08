from app import db, bcrypt
from flask_login import UserMixin

#criação das tabelas
class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)
    
    #cria uma nova propriedade que vai apontar para classes que recebem a pk do Usuario e carregar vários instâncias
    orcamentos_u = db.relationship('Orcamento', backref='usuario', lazy=True)
    transacoes_entrada_u = db.relationship('TransacaoEntrada', backref='usuario', lazy=True)
    transacoes_saida_u = db.relationship('TransacaoSaida', backref='usuario', lazy=True)
    categorias_u = db.relationship('Categoria', backref='usuario', lazy=True)
    objetivos_u = db.relationship('Objetivo', backref='usuario', lazy=True)
    transacoes_cofrinho_u = db.relationship('TransacaoCofrinho', backref='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuário: {self.nom_usuario}>'
    
    def verify_password(self, password):
        return bcrypt.check_password_hash(self.sen_usuario, password)
    
    @staticmethod
    def show_all():
        return Usuario.query.all()
    
    def monthly(self):
        lista = []

        if len(self.transacoes_entrada_u) == 0 or len(self.transacoes_saida_u) == 0:
            return 'no transactions'
        
        income_jan = 0 
        income_feb = 0 
        income_mar = 0
        income_apr = 0
        income_may = 0
        income_jun = 0
        income_jul = 0
        income_aug = 0
        income_sep = 0
        income_oct = 0
        income_nov = 0
        income_dec = 0
        expense_jan = 0
        expense_feb = 0
        expense_mar = 0
        expense_apr = 0
        expense_may = 0
        expense_jun = 0
        expense_jul = 0
        expense_aug = 0
        expense_sep = 0
        expense_oct = 0
        expense_nov = 0
        expense_dec = 0
        
        for transacao in self.transacoes_entrada_u: 
            if transacao.dat_entrada.month == 1: income_jan += transacao.val_entrada
            elif transacao.dat_entrada.month == 2: income_feb += transacao.val_entrada
            elif transacao.dat_entrada.month == 3: income_mar += transacao.val_entrada
            elif transacao.dat_entrada.month == 4: income_apr += transacao.val_entrada
            elif transacao.dat_entrada.month == 5: income_may += transacao.val_entrada
            elif transacao.dat_entrada.month == 6: income_jun += transacao.val_entrada
            elif transacao.dat_entrada.month == 7: income_jul += transacao.val_entrada
            elif transacao.dat_entrada.month == 8: income_aug += transacao.val_entrada
            elif transacao.dat_entrada.month == 9: income_sep += transacao.val_entrada
            elif transacao.dat_entrada.month == 10: income_oct += transacao.val_entrada
            elif transacao.dat_entrada.month == 11: income_nov += transacao.val_entrada
            elif transacao.dat_entrada.month == 12: income_dec += transacao.val_entrada
        
        for transacao in self.transacoes_saida_u: 
            if transacao.dat_saida.month == 1: expense_jan += transacao.val_saida
            elif transacao.dat_saida.month == 2: expense_feb += transacao.val_saida
            elif transacao.dat_saida.month == 3: expense_mar += transacao.val_saida
            elif transacao.dat_saida.month == 4: expense_apr += transacao.val_saida
            elif transacao.dat_saida.month == 5: expense_may += transacao.val_saida
            elif transacao.dat_saida.month == 6: expense_jun += transacao.val_saida
            elif transacao.dat_saida.month == 7: expense_jul += transacao.val_saida
            elif transacao.dat_saida.month == 8: expense_aug += transacao.val_saida
            elif transacao.dat_saida.month == 9: expense_sep += transacao.val_saida
            elif transacao.dat_saida.month == 10: expense_oct += transacao.val_saida
            elif transacao.dat_saida.month == 11: expense_nov += transacao.val_saida
            elif transacao.dat_saida.month == 12: expense_dec += transacao.val_saida
            
            dicio_incomes = {'jan': income_jan,"feb": income_feb, "mar": income_mar, "apr": income_apr, "may": income_may,"jun": income_jun,"jul": income_jul,"aug": income_aug,"sep": income_sep,"oct": income_oct,"nov": income_nov,"dec": income_dec}
            dicio_expenses = {'jan': expense_jan,"feb": expense_feb, "mar": expense_mar, "apr": expense_apr, "may": expense_may,"jun": expense_jun,"jul": expense_jul,"aug": expense_aug,"sep": expense_sep,"oct": expense_oct,"nov": expense_nov,"dec": expense_dec}
        
            lista = [dicio_incomes, dicio_expenses]
        
        return lista
    
    def total(self):
        entrada = 0
        saida = 0
        cofrinho = 0

        for transacao in self.transacoes_entrada_u: 
            entrada += 1

        for transacao in self.transacoes_saida_u: 
            saida += 1
        
        for transacao in self.transacoes_cofrinho_u: 
            cofrinho += 1

        total = entrada + saida + cofrinho

        dicio =	{ "entrada": entrada, "saida": saida, "cofrinho": cofrinho, "total": total }

        return dicio
    
    def most_recents(self):

        transactions = []

        for transacao in self.transacoes_entrada_u: 
            dicio = {'date': transacao.dat_entrada, 'value': transacao.val_entrada, 'type': 'Entrada'}
            transactions.append(dicio)

        for transacao in self.transacoes_saida_u:
            dicio = {'date': transacao.dat_saida, 'value': transacao.val_saida, 'type': 'Saída'}
            transactions.append(dicio)

        for transacao in self.transacoes_cofrinho_u:
            dicio = {'date': transacao.dat_transacao, 'value': transacao.val_cofrinho, 'type': f'Cofrinho - {transacao.tip_transacao}'}
            transactions.append(dicio)

        most_recents = sorted(transactions, key=lambda x: x['date'], reverse=True)[:5]

        return most_recents

    def piggies(self):
        l = []
    
        for objetivo in self.objetivos_u:
            total = 0
            for transacao in self.transacoes_cofrinho_u: 
                if objetivo.id == transacao.cod_objetivo:
                    if transacao.tip_transacao == 'Guardar':
                        total += transacao.val_cofrinho
                        dicio = {'name': objetivo.nom_objetivo, 'value': total, 'color': objetivo.cor_objetivo}
                    else:
                        total -= transacao.val_cofrinho
                        dicio = {'name': objetivo.nom_objetivo, 'value': total, 'color': objetivo.cor_objetivo}
            l.append(dicio)
               
        return l
                
             
class Orcamento(db.Model):
    __tablename__ = 'orcamentos'
    id = db.Column(db.Integer, primary_key=True)
    val_orcamento_real = db.Column(db.Float(64))
    val_orcamento_previsto = db.Column(db.Float(64))
    mes_orcamento = db.Column(db.String(), nullable=False)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
     
class TransacaoEntrada(db.Model):
    __tablename__ = 'transacoes_entrada'
    id = db.Column(db.Integer, primary_key=True)
    dsc_entrada = db.Column(db.String(64), nullable=False)
    dat_entrada = db.Column(db.Date(), nullable=False)
    val_entrada = db.Column(db.Float(64))
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))    

    # def __repr__(self):
    #     return f'<Transação Entrada: {self.dsc_entrada} | Data: {self.dat_entrada} | Valor: {self.val_entrada}>'
    
    def show_all():
        return TransacaoEntrada.query.all()
    
    def show_one(income_id):
        return TransacaoEntrada.query.get(int(income_id))

class TransacaoSaida(db.Model):
    __tablename__ = 'transacoes_saida'
    id = db.Column(db.Integer, primary_key=True)
    dsc_saida = db.Column(db.String(64), nullable=False)
    dat_saida = db.Column(db.Date(), nullable=False)
    val_saida = db.Column(db.Float(64))
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    cod_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    
    categoria_nome = db.relationship('Categoria', backref='transacoes_saida', lazy=True, viewonly=True)

    # def __repr__(self):
    #     return f'<Transação Saída: {self.dsc_saida} | Data: {self.dat_saida} | Valor: {self.val_saida}>'

    @staticmethod
    def show_one(expense_id):
        return TransacaoSaida.query.get(int(expense_id))
    
    @staticmethod
    def show_all():
        return TransacaoEntrada.query.all()
    
    def get_categoria_nome(self):
        if self.categoria_nome is not None:
            return str(self.categoria_nome.dsc_categoria)
        else:
            return 'Sem categoria'

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    dsc_categoria = db.Column(db.String(64), nullable=False)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    transacoes_saida_c = db.relationship('TransacaoSaida', backref='categoria', lazy=True)

    def __repr__(self):
        return f'<Categoria: {self.dsc_categoria}>'
    
class Objetivo(db.Model):
    __tablename__ = 'objetivos'
    id = db.Column(db.Integer, primary_key=True)
    nom_objetivo = db.Column(db.String(64), nullable=False)
    cor_objetivo = db.Column(db.String(64), nullable=True)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
   
    transacoes_cofrinho_o = db.relationship('TransacaoCofrinho', backref='objetivo', lazy=True)

    # def __repr__(self):
    #     return f'<Objetivo: {self.dsc_objetivo} | Cor: {self.cor_objetivo}>'
    
class TransacaoCofrinho(db.Model):
    __tablename__ = 'transacoes_cofrinho'
    id = db.Column(db.Integer, primary_key=True)
    tip_transacao = db.Column(db.String(64), nullable=False)
    dat_transacao = db.Column(db.Date(), nullable=False)
    val_cofrinho = db.Column(db.Float(64), nullable=False)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    cod_objetivo = db.Column(db.Integer, db.ForeignKey('objetivos.id'))

    @staticmethod
    def show_one(budget_id):
        return TransacaoCofrinho.query.get(int(budget_id))
    
    #objetivos_c = db.relationship('Objetivo', backref='transacao_cofrinho', lazy=True)

        
    # def __repr__(self):
    #     return f'<Transação Cofrinho: {self.tip_transacao} | Data: {self.dat_transacao}> | Valor: {self.val_cofrinho}'