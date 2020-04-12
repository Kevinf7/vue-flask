from flask import Flask
from config import Config
from flask_cors import CORS

app = Flask(__name__, static_folder='../../dist', static_url_path='/')
CORS(app)
app.config.from_object(Config)


# from app import api1, api2, api3 .. etc
from app import routes
