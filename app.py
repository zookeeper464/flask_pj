from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__) # 가장 기본적인 flask 앱 설정
    app.config.from_object(Config)

    db.init_app(app)
    
    from .main.routes import main
    app.register_blueprint(main)
    return app