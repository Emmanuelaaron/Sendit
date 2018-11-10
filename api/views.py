from flask import Flask, request, jsonify, json
from api.models import *


app = Flask(__name__)
@app.route("/")
def index():
    return "Do you wanna send it?, if yes send it"

@app.route("/api/v1/parcels")
def get_all_parcels():
    data = request.get_json()
    item = data.get("item")
    pickup_location = data.get("pickup_location")
    destination = data.get("destination")
    myOrders = Order(item, pickup_location, destination)

    message = myOrders.get_all_orders()
    return jsonify(message), 200

@app.route("/api/v1/parcels/<int:parcelId>")
def get_specific_parcel(parcelId):
    data = request.get_json()
    item = data.get("item")
    pickup_location = data.get("pickup_location")
    destination = data.get("destination")
    myOrders = Order(item, pickup_location, destination)

    return jsonify(myOrders.get_specific_order(parcelId)), 200

@app.route("/api/v1/users/<int:userId>/parcels")
def get_all_orders_specific_user_(userId):
    data = request.get_json()
    item = data.get("item")
    pickup_location = data.get("pickup_location")
    destination = data.get("destination")
    myOrders = Order(item, pickup_location, destination)
    message = myOrders.get_all_orders_specific_user(userId)

    return jsonify(message), 200
