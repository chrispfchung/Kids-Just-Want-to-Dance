from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///nycconcertdatabase.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_ECHO"] = True
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

db = SQLAlchemy(server)

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')

from dashpackage.models import *
from dashpackage.routes import *
from dashpackage.dashboard import *
