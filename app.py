from flask import Flask
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__) # 가장 기본적인 flask 앱 설정
    app.config.from_object(Config)

    from .main.routes import main
    app.register_blueprint(main)
    return app