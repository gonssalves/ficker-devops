from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.name}>'
    
class Orcamento(db.Model):
    __tablename__ = 'orcamentos'
    cod_orcamento = db.Column(db.Integer, primary_key=True)
    val_orcamento = db.Column(db.Float(64))
    dat_orcamento = db.Column(db.Date(64), nullable=False)

    def __repr__(self):
        return f'<Orcamento {self.name}>'
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.name}>'
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.name}>'
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.name}>'
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.name}>'
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.name}>'
    
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nom_real = db.Column(db.String(64), nullable=False)
    nom_usuario = db.Column(db.String(64), unique=True,)
    sen_usuario = db.Column(db.String(), nullable=False)
    eml_usuario = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.name}>'