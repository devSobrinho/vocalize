from flask import Flask
from flask_cors import CORS
from app.modules.speech.speech_controller import speech_bd

def init_server():
    # Cria a aplicação Flask
    app = Flask(__name__)

    # Configura o CORS para liberar para todas as origens
    CORS(app, resources={r"/*": {"origins": "*"}})
   
    # Registro das blueprints
    app.register_blueprint(speech_bd, url_prefix='/speech')
   
    return app
