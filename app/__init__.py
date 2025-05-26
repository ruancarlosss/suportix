from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager




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
    app.config['SECRET_KEY'] = 'troque_esta_chave_por_uma_secreta!' # Sessões de Login

    db.init_app(app)


    # Configura o Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    



    # Registra Blueprints
    from app.routes import main
    app.register_blueprint(main)
    from app.routes_auth import auth
    app.register_blueprint(auth)


    from app.routes_admin import admin
    app.register_blueprint(admin)

    return app






