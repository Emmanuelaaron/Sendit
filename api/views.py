from flask import Flask, request, jsonify, json
from api.models import *


app = Flask(__name__)
@app.route("/")
def index():
    return "Do you wanna send it?, if yes send it"

@app.route("/api/v1/parcels")
def get_all_parcels():
    return jsonify(orders)
