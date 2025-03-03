from flask import Blueprint

departamento_bp = Blueprint('departamento', __name__)

from app.routes import departamento