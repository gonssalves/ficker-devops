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
    
    def show_all():
        return Usuario.query.all()
    
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
    cod_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    
    categoria_nome = db.relationship('Categoria', backref='transacoes_entrada', lazy=True, viewonly=True)

    # def __repr__(self):
    #     return f'<Transação Entrada: {self.dsc_entrada} | Data: {self.dat_entrada} | Valor: {self.val_entrada}>'
    
    def show_all():
        return TransacaoEntrada.query.all()
    
    def show_one(income_id):
        return TransacaoEntrada.query.get(int(income_id))

    def get_categoria_nome(self):
        if self.categoria_nome is not None:
            return str(self.categoria_nome.dsc_categoria)
        else:
            return 'Sem categoria'

class TransacaoSaida(db.Model):
    __tablename__ = 'transacoes_saida'
    id = db.Column(db.Integer, primary_key=True)
    dsc_saida = db.Column(db.String(64), nullable=False)
    dat_saida = db.Column(db.Date(), nullable=False)
    val_saida = db.Column(db.Float(64))
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    # def __repr__(self):
    #     return f'<Transação Saída: {self.dsc_saida} | Data: {self.dat_saida} | Valor: {self.val_saida}>'

    def show_one(expense_id):
        return TransacaoSaida.query.get(int(expense_id))

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    dsc_categoria = db.Column(db.String(64), nullable=False)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    transacoes_entrada_c = db.relationship('TransacaoEntrada', backref='categoria', lazy=True)

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
   
    # def __repr__(self):
    #     return f'<Transação Cofrinho: {self.tip_transacao} | Data: {self.dat_transacao}> | Valor: {self.val_cofrinho}'