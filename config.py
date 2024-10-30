from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Konfigurasi MySQL
app.config[ 'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/db_flask_api' 
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()