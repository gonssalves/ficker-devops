from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nom_usuario} | {self.nom_real}>'
    
class Orcamento(db.Model):
    __tablename__ = 'orcamentos'
    cod_orcamento = db.Column(db.Integer, primary_key=True)
    val_orcamento = db.Column(db.Float(64))
    dat_orcamento = db.Column(db.Date(), nullable=False)

    def __repr__(self):
        return f'<Orcamento {self.val_orcamento} | {self.dat_orcamento}>'
    
class TransacaoEntrada(db.Model):
    __tablename__ = 'transacoes_entrada'
    cod_entrada = db.Column(db.Integer, primary_key=True)
    dsc_entrada = db.Column(db.String(64), nullable=False)
    dat_entrada = db.Column(db.Date(), nullable=False)
    val_entrada = db.Column(db.Float(64))

    def __repr__(self):
        return f'<TransacaoEntrada {self.dsc_entrada} | {self.dsc_entrada} | {self.dsc_entrada}>'
    
class TransacaoSaida(db.Model):
    __tablename__ = 'transacoes_saida'
    cod_saida = db.Column(db.Integer, primary_key=True)
    dsc_saida = db.Column(db.String(64), nullable=False)
    dat_saida = db.Column(db.Date(), nullable=False)
    val_saida = db.Column(db.Float(64))

    def __repr__(self):
        return f'<TransacaoEntrada {self.dsc_saida} | {self.dat_saida} | {self.val_saida}>'

class Categoria(db.Model):
    __tablename__ = 'categorias'
    cod_categoria = db.Column(db.Integer, primary_key=True)
    dsc_categoria = db.Column(db.String(64), nullable=False)
    
    def __repr__(self):
        return f'<Categoria {self.dsc_categoria}>'
    
class Objetivo(db.Model):
    __tablename__ = 'objetivos'
    cod_objetivo = db.Column(db.Integer, primary_key=True)
    dsc_objetivo = db.Column(db.String(64), nullable=False)
    cor_objetivo = db.Column(db.String(64), nullable=True,)
   
    def __repr__(self):
        return f'<Objetivo {self.dsc_objetivo} | {self.cor_objetivo}>'
    
class TransacaoCofrinho(db.Model):
    __tablename__ = 'transacoes_cofrinho'
    cod_cofrinho = db.Column(db.Integer, primary_key=True)
    dat_transacao = db.Column(db.Date(), nullable=False)
    val_cofrinho = db.Column(db.Float(64), nullable=False)

    def __repr__(self):
        return f'<TransacaoCofrinho {self.dat_transacao}> | {self.val_cofrinho}'
    
class Acao(db.Model):
    __tablename__ = 'acoes'
    cod_acao = db.Column(db.Integer, primary_key=True)
    dsc_acao = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'<Acao {self.dsc_acao}>'