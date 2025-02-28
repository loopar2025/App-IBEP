from app import db, app

class Departamento(db.Model):
    id = db.Column(db.String(), primary_key=True)
    nome = db.Column(db.String())
    email = db.Column(db.String())
    senha = db.Column(db.String())
    representante = db.Column(db.String())

    def __init__(self, id, nome, email, senha, representante):
        self.id = id
        self.nome = nome 
        self.email = email
        self.senha = senha
        self.representante = representante 

