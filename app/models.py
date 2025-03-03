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

class Documento(db.Model):
    url = db.Column(db.String(), primary_key=True)
    departamento = db.Column(db.String()) # Qual tipo de departamento esse documento pertence 
    tipo = db.Column(db.String()) # Oficio, planilha...
    nome = db.Column(db.String())

    def __init__(self, url, departamento, tipo, nome):
        self.url = url
        self.departamento = departamento
        self.tipo = tipo
        self.nome = nome 

class Voluntario(db.Model):
    id = db.Column(db.String(), primary_key=True)
    nome = db.Column(db.String())
    cargo = db.Column(db.String())
    departamento = db.Column(db.String())
    email = db.Column(db.String())
    cidade = db.Column(db.String()) # Ex.: Elísio Medrado/Bahia
    ingresso = db.Column(db.String()) # Data que entrou 
    fim = db.Column(db.String()) # Fim do voluntariado 
    observacoes = db.Column(db.String())

    def __init__(self, id, nome, cargo, departamento, email, cidade, ingresso, fim, observacoes):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.departamento = departamento
        self.email = email
        self.cidade = cidade
        self.ingresso = ingresso 
        self.fim = fim 
        self.observacoes = observacoes

class Compromisso(db.Model):
    id = db.Column(db.String(), primary_key=True)
    titulo = db.Column(db.String())
    descricao = db.Column(db.String())
    data = db.Column(db.DateTime())
    tipo = db.Column(db.String()) # Coletivo ou Presidente ou departamento especifico

    def __init__(self, id, titulo, descricao, data, tipo):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.tipo = tipo

class Task(db.Model):
    id = db.Column(db.String(), primary_key=True)
    titulo = db.Column(db.String())
    area = db.Column(db.String()) # Departamento
    check = db.Column(db.Boolean())

class Entidade(db.Model):
    nome = db.Column(db.String(), primary_key=True)
    responsavel = db.Column(db.String())
    localidade = db.Column(db.String())
    numero = db.Column(db.Integer)
    instagram = db.Column(db.String())
    email = db.Column(db.String())

class Projetos(db.Model):
    nome = db.Column(db.String(), primary_key=True)
    responsavel = db.Column(db.String())
    contato = db.Column(db.String())
    instagram = db.Column(db.String())
    objetivo = db.Column(db.Text)


with app.app_context():
	db.create_all()