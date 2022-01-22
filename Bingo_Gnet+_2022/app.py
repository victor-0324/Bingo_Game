from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy  import SQLAlchemy
import mysql.connector
import json
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html') 

'''@app.route('/', methods=['POST'])
def myform():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text'''


@app.route("/cartela/")
def cartela():
    return render_template("/cartela.html/")

@app.route("/narrador")
def narrador():
    return render_template('/narrador.html')

if __name__=='__main__':
    app.run(debug=True)