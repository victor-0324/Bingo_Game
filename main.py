from flask import Flask, render_template, request, redirect, Response
import mysql.connector
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIOS']= True
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root@localhost/usuario'

# login_manager = LoginManager(app)
db = SQLAlchemy(app)


# class Usuario(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nome= db.Column(db.String(50))
#     email = db.Column(db.String(100))

# db.create_all()

# Tela de Erro 404 
# @app.errorhandler(404) 
# def not_found(e):
#     return render_template("404.html")


@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


# Tela Iniciarl
@app.route("/", methods=["GET","POST"])
def index():
    return render_template('index.html') 
    nome_jogador = request.form('name')


# Tela Das Cartelas
@app.route("/cartela/", methods=["GET","POST"])
def cartela():
    usuario = request.form.get('name')
    return render_template("/cartela.html",nome=usuario.upper())



# Tela do jogo da velha 
@app.route("/jogodavelha/", methods=["GET","POST"])
def velha():
    usuarios1 = request.form.get('name')
    return render_template("/indexx.html",nome1=usuarios1.upper())




# Tela do narrador 
@app.route("/narrador/")
def narrador():
    return render_template('/narrador.html')




# iniciar Servidor
if __name__=='__main__':
    app.run(debug=True)