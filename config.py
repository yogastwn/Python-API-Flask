from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Konfigurasi MySQL
# app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/db_flask_api'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://flaskapiv1_progressat:f0ffb3988e7eb72005ea2fd4e3874c0f4e92d131@hwkqo.h.filess.io:3307/flaskapiv1_progressat' 

app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()
