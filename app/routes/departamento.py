from flask import render_template, redirect, session, jsonify, request, make_response, send_file
from app.routes import departamento_bp
from app.models import Departamento
from app import db
import uuid

@departamento_bp.route("/")
def homepage():
    return render_template("index.html")

@departamento_bp.route("/api/create-dep", methods=["POST"])
def criar_departamento():
    data = request.get_json()
    senha = "admin123"
    novo_dep = Departamento(
        id=str(uuid.uuid4()),
        nome=data["nome"],
        email = data["email"],
        senha = senha,
        representante=data["representante"]
    )
    db.session.add(novo_dep)
    db.session.commit()

    return jsonify({
        "msg": "success",
        "id": str(novo_dep.id)
    })

