from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data-learnloop-6.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'
app.config["PERMANENT_SESSION_LIFETIME"] = 3600 * 24 * 7  # 7 dias

db = SQLAlchemy(app)

CORS(app, resources={
    r"/api/gerar-artigo-ai": {"origins": "http://learnloop.site"}
    })


    # Importe e registre as blueprints (rotas) da sua aplicação
from app.routes import departamento_bp, voluntariado_bp, documentos_bp, agenda_bp