from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Banco de dados. Responsável pela criação dos Tickets
class Ticket(db.Model):

    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(100), nullable=False)
    description     = db.Column(db.Text, nullable=False)
    status          = db.Column(db.String(20), default='Aberto')
    created_at      = db.Column(db.DateTime, server_default=db.func.now())


    def __repr__(self):
        return f'<Ticket {self.id} - {self.title}>'


# tabela do usuário e senha. Com uma criptografia de nível hash. Transformando a senha do usuário um texto aleatório.

class User(db.Model, UserMixin):

    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(150), unique=True, nullable=False)
    password_hash   = db.Column(db.String(128), nullable=False)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)