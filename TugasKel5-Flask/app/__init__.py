# app/__init__.py
from flask import Flask

app = Flask(__name__)

# Import routes setelah inisialisasi Flask app
from app import routes
