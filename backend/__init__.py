from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from backend.usuario_routes import usuario_bp
from backend.post_routes import post_bp

app.register_blueprint(usuario_bp, url_prefix='/api')
app.register_blueprint(post_bp, url_prefix='/api')
