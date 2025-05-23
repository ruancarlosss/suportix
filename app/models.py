from app import db


# Banco de dados.
class Ticket(db.Model):

    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(100), nullable=False)
    description     = db.Column(db.Text, nullable=False)
    status          = db.Column(db.String(20), default='Aberto')
    created_at      = db.Column(db.DateTime, server_default=db.func.now())


    def __repr__(self):
        return f'<Ticket {self.id} - {self.title}>'