from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# Configuração do banco de dados
db = SQLAlchemy()

# app = Flask(__name__)

def create_app():
    app = Flask(

        __name__,
        template_folder='templates',
        static_folder='static'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tickets.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    from app.routes import main
    app.register_blueprint(main)

    return app






